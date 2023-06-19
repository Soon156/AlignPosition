import time
import csv
import psutil
import win32process
import win32api
import win32gui

filename = 'app_use_times.csv'
condition = True  # To control thread
# Create a dictionary to store app use times
app_use_times = {}
active_time = 0


def tracking():
    global active_time
    # Load existing app use times from the CSV file, if it exists
    try:
        with open(filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                app_name = row['App Name']
                use_time = int(row['Use Time (seconds)'])
                app_use_times[app_name] = use_time
    except FileNotFoundError:
        print(f"No existing app use time data found in '{filename}'")  # link to GUI

    while condition:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]
        p = psutil.Process(pid)
        ExecutablePath = p.exe()
        langs = win32api.GetFileVersionInfo(ExecutablePath, r'\VarFileInfo\Translation')
        key = r'StringFileInfo\%04x%04x\FileDescription' % (langs[0][0], langs[0][1])
        name = (win32api.GetFileVersionInfo(ExecutablePath, key))
        start_time = time.time()
        print(name)  # Test purpose

        if name in app_use_times:
            last_active_time = app_use_times[name]
            print(f"Recorded Time: {last_active_time}")  # Test purpose

        if name != 'Windows Explorer':
            while pid == win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]:
                time.sleep(1)
                active_time = int(time.time() - start_time)
                print(active_time)  # Test purpose
            print(f"{name} was used for {active_time} seconds")  # Test purpose
            # Add the new use time to the existing use time for the app
            if name in app_use_times:
                app_use_times[name] += active_time
            else:
                app_use_times[name] = active_time

        update_app_use_time()

        if name in app_use_times:
            print(f"latest use time: {app_use_times[name]}")  # Test purpose

        time.sleep(1)

    update_app_use_time()  # Test Purpose


def update_app_use_time():
    # Write the updated app use times to the CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['App Name', 'Use Time (seconds)']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for app_name, use_time in app_use_times.items():
            writer.writerow({'App Name': app_name, 'Use Time (seconds)': use_time})


'''
# Track Use Time
def computer_time(rest_time):
    global rest_timer
    rest = use_time - rest_timer
    if rest >= (rest_time * 60):
        active_notification(1)
        rest_timer = use_time'''
