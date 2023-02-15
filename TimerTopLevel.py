import tkinter
import customtkinter
import initialize as i


# Customization setting
class create_toplevel:
    def __init__(self, main):
        super().__init__()
        # window attribute
        values = i.get_val()
        window = tkinter.Toplevel(main)
        window.geometry("400x550")
        window.title("Settings")
        window.iconbitmap('Resources/logo.ico')
        window.grab_set()
        main = customtkinter.CTkFrame(window, corner_radius=0)
        main.pack(fill="both", expand=True)

        frame = customtkinter.CTkFrame(master=main, corner_radius=0)
        frame.grid(rowspan=9, padx=10, pady=10)

        self.range = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                            text='Distance Sensitivity (cm): ' + str(values.get('Range')))
        self.range.grid(row=0, column=0, padx=20, pady=(15, 5))

        range_slider = customtkinter.CTkSlider(master=frame,
                                               command=self.range_callback,
                                               from_=5, to=20, number_of_steps=15)
        range_slider.grid(row=1, column=0, padx=20, pady=(0, 10))
        range_slider.set(float(values.get('Range')))

        self.time = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                           text='Distance Sensitivity (s): ' + str(values.get('Position')))
        self.time.grid(row=2, column=0, padx=20, pady=(5, 5))

        time_slider = customtkinter.CTkSlider(master=frame,
                                              command=self.position_callback,
                                              from_=5, to=20, number_of_steps=15)
        time_slider.grid(row=3, column=0, padx=20, pady=(0, 15))
        time_slider.set(float(values.get('Position')))

        rest = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                      text='Rest Time (m):')
        rest.grid(row=4, column=0, padx=20, pady=(0, 5))

        self.rest_entry = customtkinter.CTkEntry(master=frame)
        self.rest_entry.insert(0, values.get('Rest'))
        self.rest_entry.grid(row=5, column=0, padx=20, pady=(0, 15))

        idle = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                      text='Idle Time (s):')
        idle.grid(row=6, column=0, padx=20, pady=(0, 5))

        self.idle_entry = customtkinter.CTkEntry(master=frame)
        self.idle_entry.insert(0, values.get('Idle'))
        self.idle_entry.grid(row=7, column=0, padx=20, pady=(0, 15))

        button_3 = customtkinter.CTkButton(master=frame,
                                           command=self.apply_config,
                                           text='Apply')
        button_3.grid(row=8, column=0, padx=20, pady=(5, 5))

        explain = customtkinter.CTkTextbox(master=frame, width=400, corner_radius=0)
        explain.grid(row=9, column=0, sticky="nsew", pady=(10, 15))
        explain.insert("0.0", "Distance Sensitivity as DS (cm):\n"
                              "User will be notify when ("+str(values.get('Distance') - values.get('Range')) +
                              ") > Object distance\n\n"
                              "Distance Sensitivity as DS (s): \n"
                              "User will be notify after "+str(values.get('Position'))
                              + " sec when above condition true\n\n"
                              "Rest Time (m):\n"
                              "User will be notify when use time is more than "+str(values.get('Rest'))+"\n\n"
                              "Idle Time (s):\n"
                              "Use time counter will stop after "+str(values.get('Idle'))+" when face are not detect")

    # Update (Rest, Idle) when button click
    def apply_config(self):
        try:
            values = i.get_val()
            values['Rest'] = float(self.rest_entry.get())
            values['Idle'] = float(self.idle_entry.get())
            i.save_value(str(values))
        except Exception as e:
            tkinter.messagebox.showerror(title='Unaccepted input', message=e)

    # slider callback
    def range_callback(self, value):
        values = i.get_val()
        self.range.configure(text='Distance Sensitivity (cm): ' + ('%d' % float(value)))
        values['Range'] = float(value)
        i.save_value(str(values))

    # slider callback
    def position_callback(self, value):
        values = i.get_val()
        self.time.configure(text='Distance Sensitivity (s): ' + ('%d' % float(value)))
        values['Position'] = float(value)
        i.save_value(str(values))
