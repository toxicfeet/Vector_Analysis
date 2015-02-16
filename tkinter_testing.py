__author__ = 'tux'

import tkinter as tk
import Convert
import sympy

cos, sin, tan = sympy.cos, sympy.sin, sympy.tan
acos, asin, atan = sympy.acos, sympy.asin, sympy.atan
sqrt = sympy.sqrt


class Convert():
    def cart_to_cyl(x, y, z):
        r = abs(sqrt(x ** 2 + y ** 2))
        phi = atan(y / x)
        z = z
        return [r, phi, z]

    def cart_to_sph(x, y, z):
        r = abs(sqrt(x ** 2 + y ** 2 + z ** 2))
        theta = atan(abs(sqrt(x ** 2 + y ** 2)) / z)
        phi = atan(y / x)
        return [r, theta, phi]

    def cyl_to_cart(r, phi, z):
        x = r * cos(phi)
        y = r * sin(phi)
        z = z
        return [x, y, z]

    def cyl_to_sph(r, phi, z):
        x = abs(sqrt(r ** 2 + z ** 2))
        y = atan(r / z)
        z = phi
        return [x, y, z]

    def sph_to_cart(r, theta, phi):
        x = r * sin(theta) * cos(phi)  # r*cos(theta)sin(phi)
        y = r * sin(theta) * sin(phi)  # r*sin(theta)sin(phi)
        z = r * cos(theta)  # r*cos(theta)
        return [x, y, z]

    def sph_to_cyl(r, theta, phi):
        x = r * sin(theta)  # R*sin(theta)
        y = phi  # phi
        z = r * cos(theta)  # R*cos(theta)
        return [x, y, z]


class MainWindow(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.window()


    def window(self):
        windowvector1 = tk.Button(self, text="Input Vector A", command=vector1.windowrun)
        windowvector1.grid(row=1)
        windowvector2 = tk.Button(self, text="Input Vector B", command=vector2.windowrun)
        windowvector2.grid(row=2)


class CoordConvert(tk.Tk):
    def __init__(self, parent):
        self.parent = parent
        self.x = 0
        self.y = 0
        self.z = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.i = 0
        self.j = 0
        self.k = 0

    def window(self):
        self.label_1 = tk.Label(self, text="Rectangular:")
        self.label_2 = tk.Label(self, text="Cylindrical:")
        self.label_3 = tk.Label(self, text="Spherical:")
        self.entry_1 = tk.Entry(self)
        self.entry_2 = tk.Entry(self)
        self.entry_3 = tk.Entry(self)
        self.entry_4 = tk.Entry(self)
        self.entry_5 = tk.Entry(self)
        self.entry_6 = tk.Entry(self)
        self.entry_7 = tk.Entry(self)
        self.entry_8 = tk.Entry(self)
        self.entry_9 = tk.Entry(self)
        self.entry_main = tk.Label(self, text=self)
        self.endwindow = tk.Button(self, text="Save Vector", command=self.destroy).grid(row=0, column=4)
        self.calculate_rect = tk.Button(self, text="Calculate", command=self.GetRectCoordinates).grid(row=1, column=4)
        self.calculate_cyli = tk.Button(self, text="Calculate", command=self.GetCyliCoordinates).grid(row=2, column=4)
        self.calculate_sphe = tk.Button(self, text="Calculate", command=self.GetSpheCoordinates).grid(row=3, column=4)

        self.entry_1.delete(0, tk.END)
        self.entry_1.insert(0, self.x)
        self.entry_4.delete(0, tk.END)
        self.entry_4.insert(0, self.y)
        self.entry_7.delete(0, tk.END)
        self.entry_7.insert(0, self.z)

        self.entry_2.delete(0, tk.END)
        self.entry_2.insert(0, self.a)
        self.entry_5.delete(0, tk.END)
        self.entry_5.insert(0, self.b)
        self.entry_8.delete(0, tk.END)
        self.entry_8.insert(0, self.c)

        self.entry_3.delete(0, tk.END)
        self.entry_3.insert(0, self.i)
        self.entry_6.delete(0, tk.END)
        self.entry_6.insert(0, self.j)
        self.entry_9.delete(0, tk.END)
        self.entry_9.insert(0, self.k)

        new_order = (self.entry_1, self.entry_4, self.entry_7,
                     self.entry_2, self.entry_5, self.entry_8,
                     self.entry_3, self.entry_6, self.entry_9)

        for widget in new_order:
            widget.lift()

        self.label_1.grid(row=1)
        self.label_2.grid(row=2)
        self.label_3.grid(row=3)
        self.entry_main.grid(row=0, column=1)
        self.entry_1.grid(row=1, column=1)
        self.entry_4.grid(row=1, column=2)
        self.entry_7.grid(row=1, column=3)
        self.entry_2.grid(row=2, column=1)
        self.entry_5.grid(row=2, column=2)
        self.entry_8.grid(row=2, column=3)
        self.entry_3.grid(row=3, column=1)
        self.entry_6.grid(row=3, column=2)
        self.entry_9.grid(row=3, column=3)

    def GetRectCoordinates(self):
        rectangular_list = self.entry_1.get() + "," + self.entry_4.get() + "," + self.entry_7.get()

        print(rectangular_list)

        if self.entry_1.get() != '':
            rect_list = rectangular_list.split(',')
            rect = [float(x.strip()) for x in rect_list]
            cyli = Convert.cart_to_cyl(rect[0], rect[1], rect[2])
            sphe = Convert.cart_to_sph(rect[0], rect[1], rect[2])

        print('Cartesian:   (' + "%.4f" % rect[0] + ', ' + "%.4f" % rect[1] + ', ' + "%.4f" % rect[2] + ').')
        print('Cylindrical: (' + "%.4f" % cyli[0] + ', ' + "%.4f" % cyli[1] + ', ' + "%.4f" % cyli[2] + ').')
        print('Spherical:   (' + "%.4f" % sphe[0] + ', ' + "%.4f" % sphe[1] + ', ' + "%.4f" % sphe[2] + ').')

        self.entry_2.delete(0, tk.END)
        self.entry_2.insert(0, cyli[0])
        self.entry_5.delete(0, tk.END)
        self.entry_5.insert(0, cyli[1])
        self.entry_8.delete(0, tk.END)
        self.entry_8.insert(0, cyli[2])

        self.entry_3.delete(0, tk.END)
        self.entry_3.insert(0, sphe[0])
        self.entry_6.delete(0, tk.END)
        self.entry_6.insert(0, sphe[1])
        self.entry_9.delete(0, tk.END)
        self.entry_9.insert(0, sphe[2])

        self.x, self.y, self.z = rect[0], rect[1], rect[2]
        self.a, self.b, self.c = cyli[0], cyli[1], cyli[2]
        self.i, self.j, self.k = sphe[0], sphe[1], sphe[2]


    def GetCyliCoordinates(self):
        cylindrical_list = self.entry_2.get() + "," + self.entry_5.get() + "," + self.entry_8.get()

        print(cylindrical_list)

        if self.entry_1.get() != '':
            cyli_list = cylindrical_list.split(',')
            cyli = [float(x.strip()) for x in cyli_list]
            rect = Convert.cyl_to_cart(cyli[0], cyli[1], cyli[2])
            sphe = Convert.cyl_to_sph(cyli[0], cyli[1], cyli[2])

        print('Cartesian:   (' + "%.4f" % rect[0] + ', ' + "%.4f" % rect[1] + ', ' + "%.4f" % rect[2] + ').')
        print('Cylindrical: (' + "%.4f" % cyli[0] + ', ' + "%.4f" % cyli[1] + ', ' + "%.4f" % cyli[2] + ').')
        print('Spherical:   (' + "%.4f" % sphe[0] + ', ' + "%.4f" % sphe[1] + ', ' + "%.4f" % sphe[2] + ').')

        self.entry_1.delete(0, tk.END)
        self.entry_1.insert(0, rect[0])
        self.entry_4.delete(0, tk.END)
        self.entry_4.insert(0, rect[1])
        self.entry_7.delete(0, tk.END)
        self.entry_7.insert(0, rect[2])

        self.entry_3.delete(0, tk.END)
        self.entry_3.insert(0, sphe[0])
        self.entry_6.delete(0, tk.END)
        self.entry_6.insert(0, sphe[1])
        self.entry_9.delete(0, tk.END)
        self.entry_9.insert(0, sphe[2])

        self.x, self.y, self.z = rect[0], rect[1], rect[2]
        self.a, self.b, self.c = cyli[0], cyli[1], cyli[2]
        self.i, self.j, self.k = sphe[0], sphe[1], sphe[2]

    def GetSpheCoordinates(self):

        spherical_list = self.entry_3.get() + "," + self.entry_6.get() + "," + self.entry_9.get()

        print(spherical_list)

        if self.entry_1.get() != '':
            sphe_list = spherical_list.split(',')
            sphe = [float(x.strip()) for x in sphe_list]
            rect = Convert.sph_to_cart(sphe[0], sphe[1], sphe[2])
            cyli = Convert.sph_to_cyl(sphe[0], sphe[1], sphe[2])

        print('Cartesian:   (' + "%.4f" % rect[0] + ', ' + "%.4f" % rect[1] + ', ' + "%.4f" % rect[2] + ').')
        print('Cylindrical: (' + "%.4f" % cyli[0] + ', ' + "%.4f" % cyli[1] + ', ' + "%.4f" % cyli[2] + ').')
        print('Spherical:   (' + "%.4f" % sphe[0] + ', ' + "%.4f" % sphe[1] + ', ' + "%.4f" % sphe[2] + ').')

        self.entry_1.delete(0, tk.END)
        self.entry_1.insert(0, rect[0])
        self.entry_4.delete(0, tk.END)
        self.entry_4.insert(0, rect[1])
        self.entry_7.delete(0, tk.END)
        self.entry_7.insert(0, rect[2])

        self.entry_2.delete(0, tk.END)
        self.entry_2.insert(0, cyli[0])
        self.entry_5.delete(0, tk.END)
        self.entry_5.insert(0, cyli[1])
        self.entry_8.delete(0, tk.END)
        self.entry_8.insert(0, cyli[2])

        self.x, self.y, self.z = rect[0], rect[1], rect[2]
        self.a, self.b, self.c = cyli[0], cyli[1], cyli[2]
        self.i, self.j, self.k = sphe[0], sphe[1], sphe[2]

    def windowrun(self):
        tk.Tk.__init__(self)
        self.window()
        self.window()


vector1 = CoordConvert(None)
vector2 = CoordConvert(None)
root = MainWindow(None)
root.mainloop()