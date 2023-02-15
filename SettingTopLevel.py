import tkinter
import customtkinter
import initialize as i
import FaceDistanceMeasurement as fm


# Calibrate Focal Length
def calibrate_attribute(distance_entry):
    try:
        values = i.get_val()
        values['Distance'] = float(distance_entry.get())
        i.save_value(str(values))
        fm.calibration()
    except Exception as e:
        tkinter.messagebox.showerror(title='Unaccepted input', message=e)


# Update focal length (get input from user)
def set_config(focal_entry):
    try:
        values = i.get_val()
        values['Focal'] = float(focal_entry.get())
        i.save_value(str(values))
    except Exception as e:
        tkinter.messagebox.showerror(title='Unaccepted input', message=e)


# Detection Setting Top Level
class create_toplevel:

    def __init__(self, main):
        super().__init__()
        values = i.get_val()

        # Window attributes
        self.window = tkinter.Toplevel(main)
        self.window.geometry("400x500")
        self.window.title("Settings")
        self.window.iconbitmap('Resources/logo.ico')
        self.window.grab_set()

        main = customtkinter.CTkFrame(self.window, corner_radius=0)
        main.pack(fill="both", expand=True)

        frame = customtkinter.CTkFrame(master=main, corner_radius=0)
        frame.grid(row=0, column=0, rowspan=9, padx=10, pady=10)

        title = customtkinter.CTkLabel(master=frame, font=("Arial", 15),
                                       text='Input info to calibrate distance')
        title.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.width = customtkinter.CTkLabel(master=frame,
                                            text='Distance between centre of eyes (mm): ' + str(values.get('Width')))
        self.width.grid(row=1, column=0, padx=20, pady=(0, 5))

        width_slider = customtkinter.CTkSlider(master=frame,
                                               command=self.slider_callback,
                                               from_=43, to=74, number_of_steps=31)
        width_slider.grid(row=2, column=0, padx=20, pady=(5, 10))
        width_slider.set(float(values.get('Width')))

        distance = customtkinter.CTkLabel(master=frame,
                                          text='Distance between object & camera(cm):')
        distance.grid(row=3, column=0, padx=20, pady=(10, 5))

        distance_entry = customtkinter.CTkEntry(master=frame)
        distance_entry.insert(0, values.get('Distance'))
        distance_entry.grid(row=4, column=0, padx=20, pady=(5, 5))

        calibration = customtkinter.CTkButton(master=frame,
                                              command=lambda: calibrate_attribute(distance_entry),
                                              text='Calibrate')
        calibration.grid(row=5, column=0, padx=20, pady=(5, 5))
        title = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                       text="Press 'q' to exit")
        title.grid(row=6, column=0, padx=20, pady=(0, 10))

        focal = customtkinter.CTkLabel(master=frame,
                                       text='Average Focal Length: ')
        focal.grid(row=7, column=0, padx=20, pady=(30, 10))

        focal_entry = customtkinter.CTkEntry(master=frame)
        focal_entry.insert(0, values.get('Focal'))
        focal_entry.grid(row=8, column=0, padx=20, pady=(0, 10))

        submit = customtkinter.CTkButton(master=frame,
                                         command=lambda: set_config(focal_entry),
                                         text='Apply')
        submit.grid(row=9, column=0, padx=20, pady=(5, 20))

    # Set slider input
    def slider_callback(self, value):
        self.width.configure(text='Distance between centre of eyes (mm): ' + ('%d' % float(value)))
        values = i.get_val()
        values['Width'] = float(value)
        i.save_value(str(values))
