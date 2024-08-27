import math
age = 45
height = 1.79
comp = 1+3j

base = input("Enter Base: ")
height = input ("Enter Height: ")
print ("The area of triangel is : ", 0.5*float(base)*float(height))

a = float(input ("enter a: "))
b = float (input ("enter b: "))
c = float(input ("enter c: "))
perimeter_triangle = a +b +c
print ("permeter of triangle: ",perimeter_triangle)

length = float(input ("enter length: "))
width = float(input ("enter width: "))
area_rectangle = length * width
primeter_rectangle = 2 * (length + width)
print ("area of rectangle: ", area_rectangle)
print ("perimeter of rectangle: ", primeter_rectangle)

radius = float(input ("enter radius: "))
area_circle = 3.14 *radius**2
print ("area of circle: ", area_circle)
circumference_circle = 2 *3.14*radius
print ("circumference of circle: ", circumference_circle)

print ("slope of y = 2x - 2 is calculated by y= mx + c , so according to this, slope is 2")
x1 = 2
y1 = 2
x2 = 6
y2 = 10
m = (y2-y1)/(x2-x1)
print ("slope = ",m)
distance = math.sqrt((y1-x1)**2 + (y2-x2)**2)
print ("distance = ", distance)

print ("slope comparison: ", m -2)

while (True):
    x = float (input ("enter x: "))
    y = x**2 + 6*x + 9
    if y == 0:
        break
    else:
        continue


if (len("dragon") != len ("python")):
    print ("length are same")

if ("on" in "python" and "on" in "dragon"):
    print ("yes it is present")

print ("I hope this course is not full of jargon: ", "jargon" in "I hope this course is not full of jargon")

print ("There is no 'on' in both dragon and python")

print ("lenth of python in float: ", float(len("python")))
print ("lenth of python in string: ", str(float(len("python"))))

number = float (input ("enter n: "))
if (number %2==0):
    print ("even number")
else:
    print ("odd number")

if (7//3 == int (2.7)):
    print ("yes it is")
else:
    print ("no it is not")

if (type ('10')==type(10)):
    print ("types are equal")
else:
    print ("types are not equal")

print ("Check if int('9.8') is equal to 10: ", int(9.8)==10)

hours = float (input ("enter hours: "))
rate_per_hour = float(input ("enter rate per hour: "))
print ("pay per person: ", hours * rate_per_hour)

no_of_years = float (input ("enter number of years: "))
print ("you have lived: ",no_of_years*12*30*24*60*60, "seconds")

print ("1 1 1 1 1")
print ("2 1 2 4 8")
print ("3 1 3 9 27")
print ("4 1 4 16 64")
print ("5 1 5 25 125")

    
    

