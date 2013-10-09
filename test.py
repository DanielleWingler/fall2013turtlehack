import turtle
import turtlehack

test_turtle = turtle.Turtle()

# Reset function for in between tests
def reset(turtle):
  turtle.color('black')
  turtle.setpos(0,0)

# random_color() test
try:
  print "Testing random_color()"
  test_turtle.color(turtlehack.random_color())
  test_turtle.circle(5)
  
except:
  print "-- problem with random_color()"

reset(test_turtle)

# colored_circle() test
try:
  print "Testing colored_circle()"
  turtlehack.colored_circle(test_turtle, 10, 'red')

except:
  print "-- problem with colored_circle()"

reset(test_turtle)

# colored_square() test
try:
  print "Testing colored_square()"
  turtlehack.colored_square(test_turtle, 20, 'blue')

except:
  print "-- problem with colored_square"

reset(test_turtle)

# random_circle() test
try:
  print "Testing random_circle()"
  test_turtle.color('green')
  turtlehack.random_circle(test_turtle, 5, 25)
except:
  print "-- problem with random_circle()"

reset(test_turtle)

# random_location() test
try:
  print "Testing random_location()"
  test_turtle.color('purple')
  turtlehack.random_location(test_turtle, 50, 50)
except:  
  print "-- problem with random_location()"


####################
print "End of tests"

reset(test_turtle)



turtle.done()
