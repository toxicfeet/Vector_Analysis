__author__ = 'tux'
"""
Program Name: ELE 370 Vector Conversion Program
Program Start Date: 27Jan2015
Purpose of Program: This program will prompt and convert various coordinate systems for homework.

Currently in the process of cleaning up the code and learning how to use git.
"""
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
        vector_input = input('Enter Coordinate system and the three values separated by commas, ie. \'2, 1, 4, 5\' or q'
                             ' to quit:')
        vector_list = vector_input.split(',')
        if vector_list[0] == '1':
            del vector_list[0]
            cart = [float(x.strip()) for x in vector_list]
            cyl = Convert.cart_to_cyl(cart[0], cart[1], cart[2])
            sph = Convert.cart_to_sph(cart[0], cart[1], cart[2])
            break
        elif vector_list[0] == '2':
            del vector_list[0]
            cyl = [float(x.strip()) for x in vector_list]
            cart = Convert.cyl_to_cart(cyl[0], cyl[1], cyl[2])
            sph = Convert.cyl_to_sph(cyl[0], cyl[1], cyl[2])
            break
        elif vector_list[0] == '3':
            del vector_list[0]
            sph = [float(x.strip()) for x in vector_list]
            cart = Convert.sph_to_cart(sph[0], sph[1], sph[2])
            cyl = Convert.sph_to_cyl(sph[0], sph[1], sph[2])
            break
        elif vector_list[0] == 'q' or 'Q' or 'quit' or 'QUIT':
            print('Thank you for using the Vector Simplification Program.')
            quit()
        else:
            print('You entered an incorrect option!')
        print()

    print('Given the coordinates provided, here are the %s, %s, and %s coordinates:' % ('Cartesian', 'Cylindrical',
                                                                                        'Spherical'))
    print()
    print('Cartesian:   (' + "%.4f" % cart[0] + ', ' + "%.4f" % cart[1] + ', ' + "%.4f" % cart[2] + ').')
    print('Cylindrical: (' + "%.4f" % cyl[0] + ', ' + "%.4f" % cyl[1] + ', ' + "%.4f" % cyl[2] + ').')
    print('Spherical:   (' + "%.4f" % sph[0] + ', ' + "%.4f" % sph[1] + ', ' + "%.4f" % sph[2] + ').')
    print()
    cart = [0, 0, 0]
    cyl = [0, 0, 0]
    sph = [0, 0, 0]