import turtle
import random

# A function that takes a turtle, a radius, a color, and an optional thickness and draws a circle
#def colored_circle(turtle, radius, color, thickness = 1):
	# TODO: write this function 


# A function that takes a side length and a color and makes a square. 
#ef colored_square(turtle, side_length, color):
	# TODO: write this function 

# A function that takes a number and makes that many random sized circles
#def random_circle(turtle, number_of_circles):
	# TODO: write this function

# A function that changes the turtle's color to a random color
def random_color():
	'''
	returns a random hex value
	'''
	color_value = format(random.randint(0,16777215),'06x')
	return "#" +color_value

# A function that takes a turtle and a pair of numbers and sets the turtle to a random location from x to -x and y to -y
#def random_location(turtle, x, y):
	# TODO: write this function 
