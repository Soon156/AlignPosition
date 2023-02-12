import tkinter
import customtkinter
import initialize as i


class create_toplevel:
    def __init__(self, main):
        super().__init__()
        values = i.get_val()
        window = tkinter.Toplevel(main)
        window.geometry("400x500")
        window.title("Settings")
        window.iconbitmap('Resources/logo.ico')
        window.grab_set()
        frame = customtkinter.CTkFrame(master=window, corner_radius=0)
        frame.pack(fill="both", expand=True)
        self.range = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                            text='Position Sensitivity (cm): ' + str(values.get('Range')))
        self.range.pack(pady=10, padx=10)
        range_slider = customtkinter.CTkSlider(master=frame,
                                               command=self.range_callback,
                                               from_=5, to=20, number_of_steps=15)
        range_slider.pack(pady=10, padx=10)
        range_slider.set(float(values.get('Range')))

        self.time = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                           text='Position Sensitivity (s): ' + str(values.get('Position')))
        self.time.pack(pady=10, padx=10)
        time_slider = customtkinter.CTkSlider(master=frame,
                                              command=self.position_callback,
                                              from_=5, to=20, number_of_steps=15)
        time_slider.pack(pady=10, padx=10)
        time_slider.set(float(values.get('Position')))

        rest = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                      text='Rest Time (m):')
        rest.pack(pady=10, padx=10)

        self.rest_entry = customtkinter.CTkEntry(master=frame)
        self.rest_entry.insert(0, values.get('Rest'))
        self.rest_entry.pack(pady=10, padx=10)

        idle = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                      text='Idle Time (s):')
        idle.pack(pady=10, padx=10)

        self.idle_entry = customtkinter.CTkEntry(master=frame)
        self.idle_entry.insert(0, values.get('Idle'))
        self.idle_entry.pack(pady=10, padx=10)

        button_3 = customtkinter.CTkButton(master=frame,
                                           command=self.apply_config,
                                           text='Apply')
        button_3.pack(pady=10, padx=10)

    def apply_config(self):
        try:
            values = i.get_val()
            values['Rest'] = float(self.rest_entry.get())
            values['Idle'] = float(self.idle_entry.get())
            i.save_value(str(values))
        except Exception as e:
            tkinter.messagebox.showerror(title='Unaccepted input', message=e)

    def range_callback(self, value):
        values = i.get_val()
        self.range.configure(text='Position Sensitivity (cm): ' + ('%d' % float(value)))
        values['Range'] = float(value)
        i.save_value(str(values))

    def position_callback(self, value):
        values = i.get_val()
        self.time.configure(text='Position Sensitivity (s): ' + ('%d' % float(value)))
        values['Position'] = float(value)
        i.save_value(str(values))
