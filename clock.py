from tkinter import *
from threading import *
import datetime
import time
from funcs import play_alarm


# create window
root = Tk()
root.geometry('400x300')
root.title('Alarm Clock')
root.config(bg='#700CB3', border=10, borderwidth=20)

# Threading
def Threading():
    t1 = Thread(target=set_alarm)
    t1.start()

# Adding widgets
Label(root, text='Alarm Clock', font=('Times 20 bold'),
      bg='#700CB3', anchor='w').pack(pady=5)
Label(root, text='Set Alarm Time in 24hr format:', font=('Times 14 bold'),
      bg='#700CB3', anchor='w').pack(pady=5)
error_label = Label(root, text='', font=('Times 15 bold'),bg='#700CB3')
time_var = StringVar()
time_entry = Entry(root, width=50, font=('ds-digital 35 bold'), bg='#CF9FFF',
                   justify=CENTER, textvariable=time_var)
time_var.set('00:00:00')
time_entry.pack()
frame = Frame(root)
frame.pack()
Button(root, text='Set Alarm', font=('Times 14 bold'), bg='#700CB3',
       fg='#ffffff', command=Threading).pack(pady=20)


def set_alarm():
    while True:
        # get alarm time
        input_time = time_var.get()
        # Disable text field when clicked set alarm button is clicked
        time_entry.configure(state='disabled')
        # one second wait time
        time.sleep(1)
        # Get current time
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        # Validate Time Format HH:MM:SS in 24hrs
        try:
            time.strptime(input_time[:8], '%H:%M:%S')

        except ValueError:
            error_label.config(text='Wrong Time Format !')
            error_label.config(fg='red')
            error_label.pack()
            time.sleep(5)
            root.destroy()
        else:
            error_label.config(text='')
            error_label.pack()

            if len(input_time) != 8:
                error_label.config(text='Wrong Time Format !')
                error_label.config(fg='red')
                error_label.pack()
                time.sleep(5)
                root.destroy()
            else:
                alarm_time = input_time

        # current time equals alarm
        if current_time == alarm_time:
            # Playing random music
            play_alarm()
            error_label.pack()