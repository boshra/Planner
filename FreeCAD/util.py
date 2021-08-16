import math
from tkinter import *


def cal_grid_center(cylinder_r=9,cylinder_h=15,hole_r=0.5,hole_d=1.5,angle=0,rotation=0):

	# convert angle
	rotation = rotation*math.pi/180
	angle    = angle*math.pi/180

	n = math.ceil(cylinder_r/hole_d)
	x_grid = [x*hole_d/math.cos(angle) for x in range(-n,n+1)]
	y_grid = x_grid

	x_mm = []
	y_mm = []


	offset_top = cylinder_h * math.tan(angle)
	for x in x_grid:
		for y in y_grid:
			if ((x**2 + y**2)<(cylinder_r-hole_r)**2) and (((x+offset_top*math.cos(rotation))**2 + (y+offset_top*math.sin(rotation))**2)<(cylinder_r-hole_r)**2):
				x_mm.append(x)
				y_mm.append(y)

	return (x_mm,y_mm)


class GetParameters(object):
	def __init__(self):
		# creating main tkinter window/toplevel
		self.master = Tk()
		  
		# this wil create a label widget
		l1 = Label(self.master, text = "grid hole radius (mm)")
		l2 = Label(self.master, text = "inter-grid distance (mm)")
		l3 = Label(self.master, text = "grid angle")
		l4 = Label(self.master, text = "grid rotation")
		  
		# grid method to arrange labels in respective
		# rows and columns as specified
		l1.grid(row = 0, column = 0, sticky = W, pady = 2)
		l2.grid(row = 1, column = 0, sticky = W, pady = 2)
		l3.grid(row = 2, column = 0, sticky = W, pady = 2)
		l4.grid(row = 3, column = 0, sticky = W, pady = 2)
		  
		# entry widgets, used to take entry from user
		self.e1 = Entry(self.master,width = 5)
		self.e2 = Entry(self.master,width = 5)
		self.e3 = Entry(self.master,width = 5)
		self.e4 = Entry(self.master,width = 5)

		# default value
		self.e1.insert(0,0.5)
		self.e2.insert(0,1.5)
		self.e3.insert(0,0)
		self.e4.insert(0,0)
		  
		# this will arrange entry widgets
		self.e1.grid(row = 0, column = 1, pady = 2)
		self.e2.grid(row = 1, column = 1, pady = 2)
		self.e3.grid(row = 2, column = 1, pady = 2)
		self.e4.grid(row = 3, column = 1, pady = 2)

		# okay button
		b = Button(self.master, text="Done", command=self.outputVar)
		b.grid(row = 4, column = 0)

		self.master.mainloop()
	
	def outputVar(self):
		self.master.quit()

