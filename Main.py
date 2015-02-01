__author__ = 'tux'
"""
Program Name: ELE 370 Vector Conversion Program
Program Start Date: 27Jan2015
Purpose of Program: This program will prompt and convert various coordinate systems for homework.
"""
import math

class convert():

    def cart_to_cyl():
        global cyl_phi, cyl_r, cyl_z
        cyl_r = abs(math.sqrt(cart_x**2+cart_y**2))
        cyl_phi = math.atan(cart_y/cart_x)
        cyl_z = cart_z

    def cart_to_sph():
        global sph_theta, sph_r, sph_phi
        sph_r = abs(math.sqrt(cart_x**2 + cart_y**2 + cart_z**2))
        sph_theta = math.atan(abs(math.sqrt(cart_x**2 + cart_y**2))/cart_z)
        sph_phi = math.atan(cart_y/cart_x)

    def cyl_to_cart(r, phi, z):
        x = r*math.cos(phi)
        y = r*math.sin(phi)
        z = z
        return {x, y, z}

    def cyl_to_sph():
        global sph_theta, sph_r, sph_phi
        sph_r = abs(math.sqrt(cyl_r**2+cyl_z**2))
        sph_theta = math.atan(cyl_r/cyl_z)
        sph_phi = cyl_phi

    def sph_to_cart():
        global cart_x, cart_y, cart_z
        cart_x = sph_r*math.sin(sph_theta)*math.cos(sph_phi)  # r*cos(theta)sin(phi)
        cart_y = sph_r*math.sin(sph_theta)*math.sin(sph_phi)  # r*sin(theta)sin(phi)
        cart_z = sph_r*math.cos(sph_theta)  # r*cos(theta)

    def sph_to_cyl():
        global cyl_phi, cyl_r, cyl_z
        cyl_phi = sph_r*math.sin(sph_theta)  # R*sin(theta)
        cyl_r = sph_phi  # phi
        cyl_z = sph_r*math.cos(sph_theta)  # R*cos(theta)

print()
print('Welcome to ELE 370 Vector Simplification Program.')
print('The purpose of this program is to convert various coordinate systems for homework.')
print('Please note this version is still in the works and all angles are in radians. Answers not guaranteed')
print()

while True:
    print('These options will turn a provided set of coordinates into the other two forms.')
    print()
    print('Please select an option from the following:')
    print('1. Enter %s Coordinates.' % "Cartesian")
    print('2. Enter %s Coordinates.' % "Cylindrical")
    print('3. Enter %s Coordinates.' % "Spherical")
    print()

    while True:
        main_menu_selection = input("Please enter a selection (press 'q' to quit):")
        if main_menu_selection == '1':
            cart_x = float(input('What is the value of x: '))
            cart_y = float(input('What is the value of y: '))
            cart_z = float(input('What is the value of z: '))
            print('Then entered values for (x, y, z) are (%s, %s, %s).' % (cart_x, cart_y, cart_z))
            convert.cart_to_cyl()
            convert.cart_to_sph()
            break
        elif main_menu_selection == '2':
            cyl_r = float(input('What is the value of r: '))
            cyl_phi = float(input('What is the value of phi: '))
            cyl_z = float(input('What is the value of z: '))
            print('Then entered values for (r, phi, z) are (%s, %s, %s).' % (cyl_r, cyl_phi, cyl_z))
            cart_x, cart_y, cart_z = convert.cyl_to_cart(cyl_r, cyl_phi, cyl_z)
            convert.cyl_to_sph()
            break
        elif main_menu_selection == '3':
            sph_r = float(input('What is the value of r: '))
            sph_theta = float(input('What is the value of theta: '))
            sph_phi = float(input('What is the value of phi: '))
            print('Then entered values for (r, phi, z) are (%s, %s, %s).' % (sph_r, sph_theta, sph_phi))
            convert.sph_to_cart()
            convert.sph_to_cyl()
            break
        elif main_menu_selection == 'q':
            print('Thank you for using the Vector Simplification Program.')
            quit()
        else:
            print('You entered an incorrect option!')
        print()

    print('Given the coordinates provided, here are the %s, %s, and %s coordinates:' % ('Cartesian', 'Cylindrical', 'Spherical'))
    print()
    print('Cartesian:   (' + "%.3f" % cart_x + ', ' + "%.3f" % cart_y + ', ' + "%.3f" % cart_z + ').')
    print('Cylindrical: (' + "%.3f" % cyl_r + ', ' + "%.3f" % cyl_phi + ', ' + "%.3f" % cyl_z + ').')
    print('Spherical:   (' + "%.3f" % sph_r + ', ' + "%.3f" % sph_theta + ', ' + "%.3f" % sph_phi + ').')
    print()
    cart_x, cart_y, cart_z = 0, 0, 0
    sph_phi, sph_theta, sph_r = 0, 0, 0
    cyl_phi, cyl_z, cyl_r = 0, 0, 0