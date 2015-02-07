__author__ = 'tux'

from tkinter import *
import math

class Convert(object):
    def cart_to_cyl(x, y, z):
        r = abs(math.sqrt(x ** 2 + y ** 2))
        phi = math.atan(y / x)
        z = z
        return [r, phi, z]

    def cart_to_sph(x, y, z):
        r = abs(math.sqrt(x ** 2 + y ** 2 + z ** 2))
        theta = math.atan(abs(math.sqrt(x ** 2 + y ** 2)) / z)
        phi = math.atan(y / x)
        return [r, theta, phi]

    def cyl_to_cart(r, phi, z):
        x = r * math.cos(phi)
        y = r * math.sin(phi)
        z = z
        return [x, y, z]

    def cyl_to_sph(r, phi, z):
        x = abs(math.sqrt(r ** 2 + z ** 2))
        y = math.atan(r / z)
        z = phi
        return [x, y, z]

    def sph_to_cart(r, theta, phi):
        x = r * math.sin(theta) * math.cos(phi)  # r*cos(theta)sin(phi)
        y = r * math.sin(theta) * math.sin(phi)  # r*sin(theta)sin(phi)
        z = r * math.cos(theta)  # r*cos(theta)
        return [x, y, z]

    def sph_to_cyl(r, theta, phi):
        x = r * math.sin(theta)  # R*sin(theta)
        y = phi  # phi
        z = r * math.cos(theta)  # R*cos(theta)
        return [x, y, z]

def GetRectCoordinates():
    rectangular_list = entry_1.get() + "," + entry_4.get() + "," + entry_7.get()

    print(rectangular_list)

    if entry_1.get() != '':
        rect_list = rectangular_list.split(',')
        rect = [float(x.strip()) for x in rect_list]
        cyli = Convert.cart_to_cyl(rect[0], rect[1], rect[2])
        sphe = Convert.cart_to_sph(rect[0], rect[1], rect[2])

    print('Cartesian:   (' + "%.4f" % rect[0] + ', ' + "%.4f" % rect[1] + ', ' + "%.4f" % rect[2] + ').')
    print('Cylindrical: (' + "%.4f" % cyli[0] + ', ' + "%.4f" % cyli[1] + ', ' + "%.4f" % cyli[2] + ').')
    print('Spherical:   (' + "%.4f" % sphe[0] + ', ' + "%.4f" % sphe[1] + ', ' + "%.4f" % sphe[2] + ').')

    entry_2.delete(0, END)
    entry_2.insert(0, cyli[0])
    entry_5.delete(0, END)
    entry_5.insert(0, cyli[1])
    entry_8.delete(0, END)
    entry_8.insert(0, cyli[2])

    entry_3.delete(0, END)
    entry_3.insert(0, sphe[0])
    entry_6.delete(0, END)
    entry_6.insert(0, sphe[1])
    entry_9.delete(0, END)
    entry_9.insert(0, sphe[2])

def GetCyliCoordinates():
    cylindrical_list = entry_2.get() + "," + entry_5.get() + "," + entry_8.get()

    print(cylindrical_list)

    if entry_1.get() != '':
        cyli_list = cylindrical_list.split(',')
        cyli = [float(x.strip()) for x in cyli_list]
        rect = Convert.cyl_to_cart(cyli[0], cyli[1], cyli[2])
        sphe = Convert.cyl_to_sph(cyli[0], cyli[1], cyli[2])

    print('Cartesian:   (' + "%.4f" % rect[0] + ', ' + "%.4f" % rect[1] + ', ' + "%.4f" % rect[2] + ').')
    print('Cylindrical: (' + "%.4f" % cyli[0] + ', ' + "%.4f" % cyli[1] + ', ' + "%.4f" % cyli[2] + ').')
    print('Spherical:   (' + "%.4f" % sphe[0] + ', ' + "%.4f" % sphe[1] + ', ' + "%.4f" % sphe[2] + ').')

    entry_1.delete(0, END)
    entry_1.insert(0, rect[0])
    entry_4.delete(0, END)
    entry_4.insert(0, rect[1])
    entry_7.delete(0, END)
    entry_7.insert(0, rect[2])

    entry_3.delete(0, END)
    entry_3.insert(0, sphe[0])
    entry_6.delete(0, END)
    entry_6.insert(0, sphe[1])
    entry_9.delete(0, END)
    entry_9.insert(0, sphe[2])

def GetSpheCoordinates():

    spherical_list = entry_3.get() + "," + entry_6.get() + "," + entry_9.get()

    print(spherical_list)

    if entry_1.get() != '':
        sphe_list = spherical_list.split(',')
        sphe = [float(x.strip()) for x in sphe_list]
        rect = Convert.sph_to_cart(sphe[0], sphe[1], sphe[2])
        cyli = Convert.sph_to_cyl(sphe[0], sphe[1], sphe[2])

    print('Cartesian:   (' + "%.4f" % rect[0] + ', ' + "%.4f" % rect[1] + ', ' + "%.4f" % rect[2] + ').')
    print('Cylindrical: (' + "%.4f" % cyli[0] + ', ' + "%.4f" % cyli[1] + ', ' + "%.4f" % cyli[2] + ').')
    print('Spherical:   (' + "%.4f" % sphe[0] + ', ' + "%.4f" % sphe[1] + ', ' + "%.4f" % sphe[2] + ').')

    entry_1.delete(0, END)
    entry_1.insert(0, rect[0])
    entry_4.delete(0, END)
    entry_4.insert(0, rect[1])
    entry_7.delete(0, END)
    entry_7.insert(0, rect[2])

    entry_2.delete(0, END)
    entry_2.insert(0, cyli[0])
    entry_5.delete(0, END)
    entry_5.insert(0, cyli[1])
    entry_8.delete(0, END)
    entry_8.insert(0, cyli[2])

root = Tk()

label_1 = Label(root, text="Rectangular:")
label_2 = Label(root, text="Cylindrical:")
label_3 = Label(root, text="Spherical:")
entry_1 = Entry(root)
entry_2 = Entry(root)
entry_3 = Entry(root)
entry_4 = Entry(root)
entry_5 = Entry(root)
entry_6 = Entry(root)
entry_7 = Entry(root)
entry_8 = Entry(root)
entry_9 = Entry(root)
entry_main = Entry(root)

calculate_rect = Button(root, text="Calculate", command=GetRectCoordinates).grid(row=1, column=4)
calculate_cyli = Button(root, text="Calculate", command=GetCyliCoordinates).grid(row=2, column=4)
calculate_sphe = Button(root, text="Calculate", command=GetSpheCoordinates).grid(row=3, column=4)

label_1.grid(row=1)
label_2.grid(row=2)
label_3.grid(row=3)
entry_main.grid(row=0, column=1)
entry_1.grid(row=1, column=1)
entry_4.grid(row=1, column=2)
entry_7.grid(row=1, column=3)
entry_2.grid(row=2, column=1)
entry_5.grid(row=2, column=2)
entry_8.grid(row=2, column=3)
entry_3.grid(row=3, column=1)
entry_6.grid(row=3, column=2)
entry_9.grid(row=3, column=3)

new_order = (entry_1, entry_4, entry_7, entry_2, entry_5, entry_8, entry_3, entry_6, entry_9)
for widget in new_order:
    widget.lift()

root.mainloop()

"""
import tkinter.messagebox

tkinter.messagebox.showinfo('Window Title', 'Monkeys can live up to 300 years.')

answer = tkinter.messagebox.askquestion('Question 1', 'Are you seated?')

if answer == 'yes':
    print(':D')
else:
    print(':(')

def doNothing():
    print("ok ok I won't...")

root = Tk()


# ***** Main Menu *****

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)

# ***** TOOLBAR *****

toolbar = Frame(root, bg="blue")

insertButton = Button(toolbar, text="Insert Image", command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** Status Bar *****

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
"""
"""
class DavidsButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this actually works!")
root = Tk()
a = DavidsButtons(root)
b = DavidsButtons(root)
root.mainloop()
-----------------------------------------------

def leftClick(event):
    print("Left")

def middleClick(event):
    print("Middle")

def rightClick(event):
    print("Right")

frame = Frame(root, width=300, height=500)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

-----------------------------------


def printName(event):
    print("Chello my name is David!")

button_1 = Button(root, text="Print Hello.")
button_1.bind("<Button-1>", printName)
button_1.pack()

-----------------------------------

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=W)
label_2.grid(row=1, sticky=S)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)


"""