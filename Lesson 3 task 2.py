# 1 - rectangle
# 2 - triangle
# 3 - circle
import math
choices = {1:"Rectangle",2:"Triangle",3:"Circle"}

user_choice = input("Please enter type of shape: 1-Rectangle, 2-Triangle, 3-Circle :")

if user_choice == 1:

    side_a = input("PLease input side a: ")
    side_b = input("Please input side b: ")
    shape_area = side_a*side_b
elif user_choice == 2:
    basis = input("PLease input basis: ")
    height = input("Pleae input heght:")
    shape_area = (basis*height)/2
elif user_choice == 3.0:
    radius = input ("Please input radius: ")
    shape_area = math.pi*(radius**2)

print ("Your shape is {}. The area is {:.1f}".format(choices[user_choice], shape_area))

