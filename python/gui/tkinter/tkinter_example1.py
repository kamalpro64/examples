from tkinter import *
from tkinter.ttk import *
import subprocess



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

# start button function
def clicked():
 
   year = year_textbox.get()
   month = month_combobox.get()
   day = day_spinbox.get()

   print(f'Month: {month}, Day: {day}, Year: {year}\n')
   
   '''
   print('Starting python script.')
   python_filename = ''
   # run a python script and pass in parameters
   cmd = 'python ' + python_filename + ' ' + year + ' ' + month + ' ' + day
   completed = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   print('stdout:')
   print(completed.stdout.decode())  #print output of python script
   print('stderr:')
   print(completed.stderr.decode())  #print output of python stderror
   # run python script
   print('Finished python script.')
   '''

# Start Button
start_button = Button(window, text="Start", command=clicked)
start_button.grid(column=2, row=7)

# Run GUI Main Loop
window.mainloop()