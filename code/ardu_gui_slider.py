from Tkinter import *
import time
import pyfirmata

board = pyfirmata.Arduino('/dev/ttyACM0')
led_pin = board.get_pin('d:10:p')

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=100, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, duty):
        led_pin.write(float(duty) / 100.0)

root = Tk()
root.wm_title('PWM Power Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()

