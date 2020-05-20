# Updates tkinter gui display every 1 sec
# tkinter gui is running the main thread (looking for event changes such as user button clicks)
# A second thread is run to update the gui display every sec in parallel
# Note: This method uses global variables to share common variables across both threads
#       Currently no thread-safe programming is used.


from tkinter import *
from tkinter.ttk import *
import threading
import time
import random


#global variables used across threads
random_num = 0
bool_update = False
rand_textbox = None

#initialize gui window
window = Tk()
window.title('Title')
window.geometry('450x200')

# display version info
gui_version = '1.0'
version_textbox = Entry(window, width=12)
version_textbox.insert(0, 'Ver: ' + gui_version)
version_textbox.config(state=DISABLED)
version_textbox.grid(column=4, row=0)

# blank row
blank_label1 = Label(window, text=' ')
blank_label1.grid(column=0, row=1)

# Month Combobox
month_label = Label(window, text='  Month: ')
month_label.grid(column=1, row=3)
month_combobox = Combobox(window, width=8)
month_combobox['values']= ('Jan', 'Feb', 'Mar')
month_combobox.current(0) #set the selected item
month_combobox.grid(column=2, row=3)

# Entry textbox
year_label = Label(window, text='  Year: ')
year_label.grid(column=4, row=3)
year_textbox = Entry(window, width=12)
year_textbox.insert(0, '2000')
year_textbox.grid(column=5, row=3)

# Rand Num
rand_label = Label(window, text='Random #: ')
rand_label.grid(column=4, row=4)
rand_textbox = Entry(window, width=12)
rand_textbox.insert(0, '0')
rand_textbox.grid(column=5, row=4)

# Day
day_label = Label(window, text='  Day: ')
day_label.grid(column=1, row=4)
var = IntVar()
var.set(1)
day_spinbox = Spinbox(window, from_=1, to=31, width=8, textvariable=var)
day_spinbox.grid(column=2,row=4)

# blank row
blank_label2 = Label(window, text=' ')
blank_label2.grid(column=0, row=6)

# blank column
blank_label = Label(window, text=' ')
blank_label.grid(column=0, row=7)


# New Thread Functions
def thread_rand():
   #print('started thread_rand\n')
   #print('bool_update: ', bool_update)
   while(bool_update == True):
      #print('running inside thread\n')
      random_num = random.random() * 100
      rand_textbox.insert(0, random_num)
      time.sleep(1)


# Button Functions
def print_status():
   year = year_textbox.get()
   month = month_combobox.get()
   day = day_spinbox.get()
   print(f'Month: {month}, Day: {day}, Year: {year}\n')

def display_rand():
   print('update random number every 1 second')
   global bool_update
   bool_update = True
   # Call New Thread
   (threading.Thread(target=thread_rand)).start()

def stop_rand():
   print('stop updating random number')
   global bool_update
   bool_update = False


# Buttons
# Print
print_button = Button(window, text="Print", command=print_status)
print_button.grid(column=2, row=7)

# Rand
rand_button = Button(window, text="Rand", command=display_rand)
rand_button.grid(column=2, row=8)

# Stop
stop_button = Button(window, text="Stop", command=stop_rand)
stop_button.grid(column=2, row=9)


# Run GUI main loop
window.mainloop()