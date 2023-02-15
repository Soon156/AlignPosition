import tkinter
import customtkinter
import initialize as i


# Change window theme color
def change_appearance_mode_event(new_appearance_mode: str):
    values = i.get_val()
    values['Appearance'] = new_appearance_mode
    i.save_value(str(values))
    customtkinter.set_appearance_mode(new_appearance_mode)


# Allow app to run background
def background_switch(btn):
    values = i.get_val()
    if values.get('Background'):
        values['Background'] = False
    else:
        values['Background'] = True
    i.save_value(str(values))
    update_background(btn)


# Allow app to notify user
def notification_switch(btn):
    values = i.get_val()
    if values.get('Notifications'):
        values['Notifications'] = False
    else:
        values['Notifications'] = True
    i.save_value(str(values))
    update_notification(btn)


# Update GUI
def update_background(btn):
    values = i.get_val()
    if values.get('Background'):
        btn.configure(text='Deactivate Background')
    else:
        btn.configure(text='Activate Background')


# Update GUI
def update_notification(btn):
    values = i.get_val()
    if values.get('Notifications'):
        btn.configure(text='Close Notification')
    else:
        btn.configure(text='Open Notification')


# App setting
def create_toplevel(frame):
    # window attribute
    window = tkinter.Toplevel(frame)
    window.geometry("200x300")
    window.title("Settings")
    window.iconbitmap('Resources/logo.ico')
    window.grab_set()

    main = customtkinter.CTkFrame(window, corner_radius=0)
    main.pack(fill="both", expand=True)

    frame = customtkinter.CTkFrame(master=main, corner_radius=0)
    frame.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

    background = customtkinter.CTkButton(master=frame, command=lambda: background_switch(background),
                                         text='Background')
    update_background(background)
    background.grid(row=0, column=0, padx=20, pady=(15, 5))

    notification_button = customtkinter.CTkButton(master=frame,
                                                  command=lambda: notification_switch(notification_button),
                                                  text='Notification')
    update_notification(notification_button)
    notification_button.grid(row=1, column=0, padx=20, pady=5)

    reset_setting = customtkinter.CTkButton(master=frame, command=i.create_config, text='Reset Config')
    reset_setting.grid(row=2, column=0, padx=20, pady=5)

    appearance_mode_label = customtkinter.CTkLabel(frame, text="Appearance Mode:", anchor="w")
    appearance_mode_label.grid(row=3, column=0, padx=20, pady=(10, 0))

    appearance_mode_optionemenu = customtkinter.CTkOptionMenu(frame,
                                                              values=["Light", "Dark", "System"],
                                                              command=change_appearance_mode_event)
    appearance_mode_optionemenu.grid(row=4, column=0, padx=20, pady=(5, 15))

    appearance_mode_optionemenu.set(i.get_val().get('Appearance'))



