import tkinter
import customtkinter
import initialize as i


def change_appearance_mode_event(new_appearance_mode: str):
    values = i.get_val()
    values['Appearance'] = new_appearance_mode
    i.save_value(str(values))
    customtkinter.set_appearance_mode(new_appearance_mode)


def update_background(btn):
    values = i.get_val()
    if values.get('Background'):
        btn.configure(text='Deactivate Background')
    else:
        btn.configure(text='Activate Background')


def update_notification(btn):
    values = i.get_val()
    if values.get('Notifications'):
        btn.configure(text='Close Notification')
    else:
        btn.configure(text='Open Notification')


def background_switch(btn):
    values = i.get_val()
    if values.get('Background'):
        values['Background'] = False
    else:
        values['Background'] = True
    i.save_value(str(values))
    update_background(btn)


def notification_switch(btn):
    values = i.get_val()
    if values.get('Notifications'):
        values['Notifications'] = False
    else:
        values['Notifications'] = True
    i.save_value(str(values))
    update_notification(btn)


def create_toplevel(frame):
    window = tkinter.Toplevel(frame)
    window.geometry("400x400")
    window.title("Settings")
    window.iconbitmap('Resources/logo.ico')
    window.grab_set()
    frame = customtkinter.CTkFrame(master=window, corner_radius=0)
    frame.pack(fill="both", expand=True)

    background = customtkinter.CTkButton(master=frame, command=lambda: background_switch(background),
                                         text='Background')
    update_background(background)
    background.pack(pady=10, padx=10)

    notification_button = customtkinter.CTkButton(master=frame,
                                                  command=lambda: notification_switch(notification_button),
                                                  text='Notification')
    update_notification(notification_button)
    notification_button.pack(pady=10, padx=10)

    reset_setting = customtkinter.CTkButton(master=frame, command=i.create_config, text='Reset Config')
    reset_setting.pack(pady=10, padx=10)

    appearance_mode_label = customtkinter.CTkLabel(frame, text="Appearance Mode:", anchor="w")
    appearance_mode_label.pack(pady=10, padx=10)

    appearance_mode_optionemenu = customtkinter.CTkOptionMenu(frame,
                                                              values=["Light", "Dark", "System"],
                                                              command=change_appearance_mode_event)
    appearance_mode_optionemenu.pack(pady=10, padx=10)

    appearance_mode_optionemenu.set(i.get_val().get('Appearance'))



