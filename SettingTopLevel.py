import tkinter
import customtkinter
import initialize as i
import FaceDistanceMeasurement as fm


def calibrate_attribute(distance_entry):
    try:
        values = i.get_val()
        values['Distance'] = float(distance_entry.get())
        i.save_value(str(values))
        fm.calibration()
    except Exception as e:
        tkinter.messagebox.showerror(title='Unaccepted input', message=e)


def set_config(focal_entry):
    try:
        values = i.get_val()
        values['Distance'] = float(focal_entry.get())
        i.save_value(str(values))
    except Exception as e:
        tkinter.messagebox.showerror(title='Unaccepted input', message=e)


class create_toplevel:
    def __init__(self, main):
        super().__init__()
        values = i.get_val()
        self.window = tkinter.Toplevel(main)
        self.window.geometry("400x500")
        self.window.title("Settings")
        self.window.iconbitmap('Resources/logo.ico')
        self.window.grab_set()
        frame = customtkinter.CTkFrame(master=self.window, corner_radius=0)
        frame.pack(fill="both", expand=True)

        title = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                       text='Input info to calibrate distance')
        title.pack(pady=10, padx=10)

        self.width = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                            text='Distance between centre of eyes (mm): ' + str(values.get('Width')))
        self.width.pack(pady=10, padx=10)

        width_slider = customtkinter.CTkSlider(master=frame,
                                               command=self.slider_callback,
                                               from_=43, to=74, number_of_steps=31)
        width_slider.pack(pady=10, padx=10)
        width_slider.set(float(values.get('Width')))

        distance = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                          text='Distance between object & camera(cm):')
        distance.pack(pady=10, padx=10)

        distance_entry = customtkinter.CTkEntry(master=frame)
        distance_entry.insert(0, values.get('Distance'))
        distance_entry.pack(pady=10, padx=10)

        calibration = customtkinter.CTkButton(master=frame,
                                              command=lambda: calibrate_attribute(distance_entry),
                                              text='Calibrate')
        calibration.pack(pady=10, padx=10)
        title = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                       text="Press 'q' to exit")
        title.pack(pady=10, padx=10)

        focal = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                       text='Average Focal Length: ')
        focal.pack(pady=10, padx=10)

        focal_entry = customtkinter.CTkEntry(master=frame)
        focal_entry.insert(0, values.get('Focal'))
        focal_entry.pack(pady=10, padx=10)

        submit = customtkinter.CTkButton(master=frame,
                                         command=lambda: set_config(focal_entry),
                                         text='Apply')
        submit.pack(pady=10, padx=10)

    def slider_callback(self, value):
        self.width.configure(text='Distance between centre of eyes (mm): ' + ('%d' % float(value)))
        values = i.get_val()
        values['Width'] = float(value)
        i.save_value(str(values))
