# Lesson 5
# A basic GUI program

from Tkinter import *

# Create the main window for our program
top = Tk()
top.minsize(300,300) # 300 x 300 is our x and y sizes
top.title('Feet to Meters Calculator') # This is our title
top.configure(bg='DarkGrey') # This is the background color

lbl_one = Label (top, text='Enter your Value in Feet Below')
lbl_one.pack()

feet_input = Entry(top)
feet_input.pack()

lbl_two = Label(top, text='Click Calculate to get result')
lbl_two.pack

convert_btn = Button(top, text='Calculate')
convert_btn.pack()

lbl_result = Label(top)
lbl_result.pack()

btn_exit = Button(top, text='Exit', command=quit)
btn_exit.pack(side=BOTTOM)

# To make Python Display the window, run a main loop:
top.mainloop()
