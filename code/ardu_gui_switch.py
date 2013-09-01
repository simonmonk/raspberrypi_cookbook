from Tkinter import *
import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')
led_pin = board.get_pin('d:10:o')

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.check_var = BooleanVar()
        check = Checkbutton(frame, text='Pin 10', 
                 command=self.update,
                 variable=self.check_var, onvalue=True, offvalue=False)
        check.grid(row=1)

    def update(self):
        led_pin.write(self.check_var.get())

root = Tk()
root.wm_title('On / Off Switch')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()
