fall2013turtlehack
==================

A library to have more fun with Turtles

## Purpose
`turtlehack` = :turtle: + :boom:

## Usage

```
import turtle
import turtlehack
import random

cruz = turtle.Turtle()

cruz.speed(10)

for i in range(random.randint(0,10)):
  
  # random_location gets you just that
  turtlehack.random_location(cruz, 300, 300)
    
    # random_color() returns just that
    cruz.color(turtlehack.random_color())
      
      # random_circles() draws random circles
      turtlehack.random_circle(cruz, 5, 15)
      
      turtlehack.random_location(cruz, 0, 0)
      cruz.color(turtlehack.random_color())
      turtlehack.random_circle(cruz, 5, 15)
```

Generates:
![](http://puu.sh/4M5Yh.png)

## Contributions
Contributions welcome!  Open an issue to discuss if you're thinking of something weird.  Otherwise, just shoot a pull request and I'll merge it.  Open issues are fair game as well.

All contributions should be polite and have tests. Or else!  dun-dun duhh

### Tests

Tests are runnable via `test.py`:
```
>>> python test.py
Testing random_color()
Testing colored_circle()
-- problem with colored_circle()
Testing colored_square()
-- problem with colored_square
Testing random_circle()
-- problem with random_circle()
Testing random_location()
-- problem with random_location()
End of tests
```

Find a good spot on the test screen to add your function name and sample output.

Please contribute tests for your enhancements if they aren't already there.

## License

This software is provided under an MIT License.  (c) 2013 Elliott Hauser and contributors.
