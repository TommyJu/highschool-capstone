# Math Pre - calc calculator (parabolas)
#python 2.7


#Makes sure that when you divide you get a full float value and not an integer
from __future__ import division



#so we can square root numbers
import math
from math import sqrt

print "\n\n\n\n\nPick the corresponding number of your desired calculation type:\n"
print "  1. Convert standard form (ax^2 + bx + c) to vertex form (y = a(x-p)^2 + q)"
print "  2. Find variable 'a' given the equation and point line passes through on graph"
print "  3. Find the y-intercept of an equation in vertex form"
print "  4. Find the x-intercept of an equation in vertex form"
print "  5. Find the x-intercept of an equation in standard form (Quadratic Formula) \n"


#Chooses which equation user wants to perform
calc_type = raw_input ("> ")

#if user picks '1' perform this operation
if calc_type == "1":
    print "\n      y = ax^2 + bx + c\n"
    print "You can type decimals: '2.7' OR fractions '5/7'"
    print "\n*If no variable given use '0'"
    print "\n*If 'a' not given use '1'\n"

    #Getting user input
    a = float(input("What is a?  "))
    b = float(input("What is b?  "))
    c = float(input("What is c?  "))

    #divides 'bx' by 'a' and stores as new var
    b = b/a
    #ensures that b2 is always positive by using 'absolute' function
    #b2 is used to get d and d2 in "a(x^2 + bx + d)-d2 + c" <-- game plan
    b2 = abs(b)

    #getting var d by dividing and squaring 'bx' by 2
    d_dividedby2 = b2/2
    d = d_dividedby2**2
    #takes negative d and multiplies by a
    d2 = -1*d*a

   # a(x^2 + bx + d) + d3     'd3' = c + d2 or ultimately the q variable in vertex formula
    d3 = d2 + c
    # used sqrt of d to factor d represented in comment above
    squarerootofd = math.sqrt(d)

    # if statement determines whether factor should be positive or negative
    if b > 0:
        print "\n\n-------------- Answer --------------"
        print "y = %s(x + %s)^2 + %s" % (a, squarerootofd, d3)
        print "\nvertex coordinates = (%s, %s)\n" % (squarerootofd*-1, d3)# because +p shifts vertex towards the left so x coordinate has to be negative
        print "Axis of symmetry: x = %s" % (squarerootofd*-1)

    else:
        print "\n\n-------------- Answer --------------"
        print "y = %s(x - %s)^2 + %s" % (a, squarerootofd, d3)
        print "\nvertex coordinates = (%s, %s)\n" % (squarerootofd, d3)
        print "Axis of symmetry: x = %s" % (squarerootofd)


    if a > 0:
        print "Min value = %s" % (d3)
        print "Range = Any number greater than or equal to ", d3
    elif a < 0:
        print "Max value = %s" % (d3)
        print "Range = Any number less than or equal to ", d3
    else:
        print "Min value = %s" % (d3)
        print "Range = Any number greater than or equal to ", d3


    print "Domain = All real numbers\n"



 # Finding a in vertex formula
elif calc_type == "2":
    print "\n      y = a(x - p)^2 + q\n"
    x = float(input("What is x in formula or x coordinate of given point?  "))
    y = float(input("What is y in formula or y coordinate of given point?  "))
    p = float(input("What is p? (if no variable given use 0) "))
    q = float(input("What is q? (if no variable given use 0) "))
    # Solves for a given variables in the equation
    answer = (y-q)/(x+p)**2
    print "\n\n-------------- Answer --------------\n\n", answer, "\n"

#Finding the y-intercept of a vertex equation
elif calc_type == "3":
    print "\n      y = a(x - p)^2 + q\n"
    print "You can type decimals: '2.7' OR fractions '5/7'"
    print "\n*If no variable given use '0'"
    print "\n*If 'a' not given use '1'\n"

    # To find y-intercept, let x = 0
    a = float(input("What is a?  "))
    p = float(input("What is p?  "))**2
    q = float(input("What is q?  "))
    answer = a*(p+q)
    print answer

# Finding x-intercept(s) of a vertex equation
elif calc_type == "4":
    print "\n      y = a(x - p)^2 + q\n"
    print "You can type decimals: '2.7' OR fractions '5/7'"
    print "\n*If no variable given use '0'"
    print "\n*If 'a' not given use '1'\n"

    #To find x-intercept, let y = 0
    a = float(input("What is a?  "))
    p = float(input("What is p?  "))*-1 # move p to other side of equation and change the sign to find vertex x value (line 122)
    q = float(input("What is q?  ")) # we dont need to turn q into a negative after moving q to the other side of the equation because on line 125 - 126 we use the absolute value of q to find the x-interceptS which == squareroot q + p and squareroot q * 1 + q
    if a > 0 and q > 0:
        print "There are no x-intercepts" # If and elif statements determine if there even is an x-intercept or not
    elif a < 0 and q < 0:
        print "There are no x-intercepts"
    elif q == 0:
        print "The x-intercept = ", p

    else:

    # Going from y = a(x - p)^2 + q to (square root -q/a) - p = x    in order to find x-intercepts
        firstXintercept = math.sqrt(abs(q)/a) + p
        secondXintercept = math.sqrt(abs(q)/a) * -1 + p
        print "\n\n-------------- Answer --------------\n"
        print "First x-intercept: ", firstXintercept
        print "Second x-intercept: ", secondXintercept
        print "\n"

#Finding the x-intercepts of an equation in standard form
elif calc_type == "5":
    try:
        print "\n     ax^2 + bx + c\n"
        print "You can type decimals: '2.7' OR fractions '5/7'"
        print "If variable is missing, input 0"
        print "If 'a' is missing, input 1"

        a = float(raw_input("\n\nWhat is a?"))
        b = float(raw_input("\n\nWhat is b?"))
        c = float(raw_input("\n\nWhat is c?"))

    # Quadratic function: x = -b plusminus sqrt.(b^2 - 4ac) divided by 2a
        print "\n\n-------------- Answer --------------\n"
        print "First x-intercept = " + str((-b + sqrt(b**2 - 4*a*c))/(2*a))
        print "Second x-intercept = " + str((-b - sqrt(b**2 - 4*a*c))/(2*a))

    except:
        print "There are no x-intercepts"




else:
    print "Please enter a valid number"
