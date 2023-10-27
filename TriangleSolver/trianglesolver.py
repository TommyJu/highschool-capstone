#Python 3

from __future__ import division
from math import *
from tkinter import *
from PIL import Image, ImageTk
import turtle




# ---------------Input GUI---------------
root = Tk()
root.title("Triangle Solver")
root.geometry("1100x600")

#Canvas
canvas = Canvas(root, width=1500, height=1000)
canvas.place(x=0, y=0, relwidth = 1, relheight = 1)

#Images
background = Image.open("background.png")

background = ImageTk.PhotoImage(background)
label_background = Label(canvas, image = background)
label_background.place(x=0, y=0, relwidth = 1, relheight = 1)


#data entry (angles)

anglesframe = Frame(canvas, width = 600, height = 500, bg = "black" )
anglesframe.place(x=100, y = 100)

angletext = Label(anglesframe, font = ("Courier", 14) , text = "Angles (In Degrees):", bg = "black", fg="white")
angletext.pack()

A_entry = Entry(anglesframe)
B_entry = Entry(anglesframe)
C_entry = Entry(anglesframe)


Atext = Label(anglesframe, font = ("Courier", 14) , text = "A", bg = "black", fg="white")

Btext = Label(anglesframe, font = ("Courier", 14) , text = "B", bg = "black", fg="white")

Ctext = Label(anglesframe, font = ("Courier", 14) , text = "C", bg = "black", fg="white")


Atext.pack()
A_entry.pack()
Btext.pack()
B_entry.pack()
Ctext.pack()
C_entry.pack()


def getAngleData(): #Receives input from entry widgets
    A = A_entry.get()
    B = B_entry.get()
    C = C_entry.get()
    return [A, B, C]

#data entry (sides)

sidesframe = Frame(canvas, width = 600, height = 500, bg = "black" )
sidesframe.place(x=100, y = 300)

sidetext = Label(sidesframe, font = ("Courier", 14) , text = "Side Lengths:", bg = "black", fg="white")
sidetext.pack()

a_entry = Entry(sidesframe)
b_entry = Entry(sidesframe)
c_entry = Entry(sidesframe)


atext = Label(sidesframe, font = ("Courier", 14) , text = "a", bg = "black", fg="white")

btext = Label(sidesframe, font = ("Courier", 14) , text = "b", bg = "black", fg="white")

ctext = Label(sidesframe, font = ("Courier", 14) , text = "c", bg = "black", fg="white")


atext.pack()
a_entry.pack()
btext.pack()
b_entry.pack()
ctext.pack()
c_entry.pack()

def getSideData(): #Receives input from entry widgets
    a = a_entry.get()
    b = b_entry.get()
    c = c_entry.get()
    return [a, b, c]

#Letter labels for the middle triangle in input GUI
triangleA = Label(canvas, font = ("Courier", 28) , text = "A", fg = "white", bg = "black")
triangleA.place(x=380, y=380)
triangleB = Label(canvas, font = ("Courier", 28) , text = "B", fg = "white", bg = "black")
triangleB.place(x=733, y=380)
triangleC = Label(canvas, font = ("Courier", 28) , text = "C", fg = "white", bg = "black")
triangleC.place(x=556.5, y=105)


#--------------Triangle Solver Program---------------------

#_________Functions________


#General ---------------------------------
def solve(): #Allows for Tkinter button to call both functions, checkTriangle which solves and
#drawTurtle which creates the popup triangle
    checkTriangle()
    drawTurtle()

def solve180(A,B): #Uses 180 degree triangle rule to find third angle IN DEGREES
    C = (180 - float(A) - float(B))
    return C

def checkTriangle(): #Function that utilizes all other functions to solve triangle

    angles = getAngleData()
    A = angles[0]
    B = angles[1] #Assigns values from list created by "getAngleData"
    C = angles[2]

    sides = getSideData() #so we can use the a variable to ensure that if statement won't be triggered by no input.
    a = sides[0]
    b = sides[1]
    c = sides[2]

# conditional statements check the variables to find out what kind of triangle the user wants to solve.
    if A == "" and B == "" and C == "" and a != "" and b !="" and c!="": #SSS

#Uses a function to return a list, each element is configured into the output labels.
        solution = solveSSS()
        solution = [float(x) for x in solution]

        ans1.config(text = "a = "+str(solution[0]))
        ans2.config(text = "b = "+str(solution[1]))
        ans3.config(text = "c = "+str(solution[2]))
        ans4.config(text = "A = "+str(solution[3]))
        ans5.config(text = "B = "+str(solution[4]))
        ans6.config(text = "C = "+str(solution[5]))

        return solution

    elif A == "" and B == "" or A == "" and C == "" or B=="" and C=="":#SSA
        solution = solveSSA()
        solution = [float(x) for x in solution]

        ans1.config(text = "a = "+str(solution[0]))
        ans2.config(text = "b = "+str(solution[1]))
        ans3.config(text = "c = "+str(solution[2]))
        ans4.config(text = "A = "+str(solution[3]))
        ans5.config(text = "B = "+str(solution[4]))
        ans6.config(text = "C = "+str(solution[5]))

        return solution

    elif A == "" or B == "" or C =="":#AAS
        solution = solveAAS()
        solution = [float(x) for x in solution]

        ans1.config(text = "a = "+str(solution[0]))
        ans2.config(text = "b = "+str(solution[1]))
        ans3.config(text = "c = "+str(solution[2]))
        ans4.config(text = "A = "+str(solution[3]))
        ans5.config(text = "B = "+str(solution[4]))
        ans6.config(text = "C = "+str(solution[5]))

        return solution

    else:
        print ("Please enter a triangle that has at least 3 data points that are not all angles")



def sineSolveSideSSA(knownSide, knownAngle, missingSideAngle): #uses sine law to find side

    missingSide = (float(knownSide) / (sin(radians(float(knownAngle))))) * (sin(radians(float(missingSideAngle))))
    return missingSide       #Must use radians() to convert input (in degrees) into radians so that the sin() function can work properly!!!!
#Turtle Graphics-------------------------------------------------------------

def drawTurtle():

#Takes solution and scales side lengths by turning the sides into a percentage of total and multiplying by scale value (800)
    values = checkTriangle() #values list in a,b,c,A,B,C format
    A = values[3]
    B = values[4]
    C = values[5]

    a = values[0]
    b = values[1]
    c = values[2]

    total = a + b + c
    a = a/total * 800
    b = b/total * 800
    c = c/total * 800

    turtle.reset()
    turtle.clearscreen()
    window = turtle.Screen()
    turtle.setup(600,600)
    turtle.penup()
    turtle.setx(-200)
    turtle.sety(-200)
    turtle.fillcolor("light blue")
    turtle.begin_fill()
    turtle.pendown()

    turtle.forward(c)
    turtle.left((180-B))
    turtle.forward(a)
    turtle.left(180-C)
    turtle.forward(b)

    turtle.end_fill()
    turtle.done() #prevents screen from closing

#SSS-----------------------------------------------------------------------

#Math Domain Error if sum of 2 sides not equal to third.
def solveSSS(): #Uses cosine law to find all 3 angles.

    sides = getSideData()
    a = float(sides[0])
    b = float(sides[1])
    c = float(sides[2])
    A = degrees(acos((b**2 + c**2 - a**2)/(2*b*c)))
    B = degrees(acos((a**2 + c**2 - b**2)/(2*a*c)))
    C = solve180(A,B)
    return [a,b,c,A,B,C]

#AAS ----------------------------------------------------------------------
def solveAAS(): #For AAS triangles and sine law

    angles = getAngleData()
    A = angles[0]
    B = angles[1]
    C = angles[2]
    sides = getSideData()
    a = sides[0]
    b = sides[1]
    c = sides[2]
#Each pair of angles has 3 possibilities
#sineSolveSideSSA() takes 3 args - known side, known side angle, missing side angle)
#possibilities given angles A and B
    if A != "" and B !="" and a !="": #missing side = b
        b = sineSolveSideSSA(a,A,B)
        C = solve180(A,B)
        c = sineSolveSideSSA(a,A,C)
        return [a,b,c,A,B,C]
    elif A!="" and B !="" and b !="": #missing side = a
        a = sineSolveSideSSA(b,B,A)
        C = solve180(A,B)
        c = sineSolveSideSSA(b,B,C)
        return [a,b,c,A,B,C]

    elif A!="" and B !="" and c !="":
        C = solve180(A,B)
        a = sineSolveSideSSA(c,C,A)
        b = sineSolveSideSSA(c,C,B)
        return [a,b,c,A,B,C]

#possibilities given angles A and C
    elif A!="" and C !="" and a !="": #missing side = c
        c = sineSolveSideSSA(a,A,C)
        B = solve180(A,C)
        b = sineSolveSideSSA(a,A,B)
        return [a,b,c,A,B,C]

    elif A!="" and C !="" and c !="": #missing side = a
        a = sineSolveSideSSA(c,C,A)
        B = solve180(A,C)
        b = sineSolveSideSSA(c,C,B)
        return [a,b,c,A,B,C]

    elif A!="" and C !="" and b !="":
        B = solve180(A,C)
        c = sineSolveSideSSA(b,B,C)
        a = sineSolveSideSSA(b,B,A)
        return [a,b,c,A,B,C]

#possibilities given angles B and C
    elif B!="" and C !="" and c !="": #missing side = b
        b = sineSolveSideSSA(c,C,B)
        A = solve180(B,C)
        a = sineSolveSideSSA(c,C,A)
        return [a,b,c,A,B,C]

    elif B!="" and C !="" and b !="": #missing side = c
        c = sineSolveSideSSA(b,B,C)
        A = solve180(B,C)
        a = sineSolveSideSSA(b,B,A)
        return [a,b,c,A,B,C]

    elif B!="" and C !="" and a !="":
        A = solve180(B,C)
        b = sineSolveSideSSA(a,A,B)
        c = sineSolveSideSSA(a,A,C)
        return [a,b,c,A,B,C]

 #AAS to AASS
#function not used
"""
def sineSolveSide():
    list = checkSolveableSide() # turns output of checkSolveableSide into list
    missingSideAngle = list[0]
    knownSide = list[1]
    knownAngle = list[2]
    missingSide = (float(knownSide) / (sin(radians(float(knownAngle))))) * (sin(radians(float(missingSideAngle))))
    print(float(missingSide))       #Must use radians() to convert input (in degrees) into radians so that the sin() function can work properly!!!!
"""

#SSA -----------------------------------------------------------------------------
def includedAngle(): #When given SSA, you need to use cos for to solve for included triangle and sin for non-included
#This function returns false when not included, but when included it is used to return values to other functions needed to solve.
    angles = getAngleData()
    A = angles[0]
    B = angles[1]
    C = angles[2]
    sides = getSideData()
    a = sides[0]
    b = sides[1]
    c = sides[2]

#solves for a
    if A != "" and b!= "" and c!="": #A = included angle
        return [A, b, c, 1] #['incl ang, incl ang side, known side] solve for side using coslaw
#solves for b
    elif B != "" and c!="" and a!="":
        return [B, c, a, 2]
#index 1 and 2 = known sides, index 0 = included angle
#solves for c
    elif C != "" and a!= "" and b != "":
        return [C, a, b, 3]
#Index 3 is for the conditional statements in "solveSSA"
    else:
        return False

# Non included ----------------------------------------------------------------


#angside = angle's side (opposite of angle),
def sineLawAngle(ang, angside,side):
    angle = degrees(asin(float(side) * sin(radians(float(ang))) / float(angside)))
    return angle

def solveSSAnotincluded(): #for each angle there are 2 possiblilities for sides

    angles = getAngleData()
    A = angles[0]
    B = angles[1]
    C = angles[2]


    sides = getSideData()
    a = sides[0]
    b = sides[1]
    c = sides[2]

# sineLawAngle(ang, angside,side)
# sineSolveSideSSA(knownSide, knownAngle, missingSideAngle)
    if A != "" and a != "" and b != "":

        B = sineLawAngle(A,a,b)
        C = solve180(A, B)
        c = sineSolveSideSSA(a,A,C)
        return [a,b,c,A,B,C]

    if A != "" and a != "" and c != "":

        C = sineLawAngle(A,a,c)
        B = solve180(A, C)
        b = sineSolveSideSSA(a,A,B)
        return [a,b,c,A,B,C]

    if B != "" and b != "" and a != "":

        A = sineLawAngle(B,b,a)
        C = solve180(A, B)
        c = sineSolveSideSSA(a,A,C)
        return [a,b,c,A,B,C]

    if B != "" and b != "" and c != "":

        C = sineLawAngle(B,b,c)
        A = solve180(C, B)
        a = sineSolveSideSSA(b,B,A)
        return [a,b,c,A,B,C]

    if C != "" and c != "" and b != "":

        B = sineLawAngle(C,c,b)
        A = solve180(C, B)
        a = sineSolveSideSSA(c,C,A)
        return [a,b,c,A,B,C]

    if C != "" and c != "" and a != "":

        A = sineLawAngle(C,c,a)
        B = solve180(A, C)
        b = sineSolveSideSSA(c,C,B)
        return [a,b,c,A,B,C]


# Included --------------------------------------------------------------------
#kside = known side, ang = included angle
def cosFormula(kside, kside2, ang):
    return sqrt(kside**2 + kside2**2 - 2*kside*kside2*cos(radians(ang)))


def solveSSAincluded():
#solves for SSA by finding side using cos law
# list 'values' - [Included angle, known side, known side, missing side, integer used to identify which case given]

    values = includedAngle()

    if values[3] == 1:
        A = float(values[0])
        b = float(values[1])
        c = float(values[2])
        a = cosFormula(b,c,A)
        return solveSSSA(a,b,c)

    elif values[3] == 2:
        B = float(values[0])
        c = float(values[1])
        a = float(values[2])
        b = cosFormula(a,c,B)
        return solveSSSA(a,b,c)


    elif values[3] ==3:
        C = float(values[0])
        a = float(values[1])
        b = float(values[2])
        c = cosFormula(a,b,C)
        return solveSSSA(a,b,c)



def solveSSSA(a, b, c): #Uses cosine law to find all 3 angles of SSSA once we use cos to find 1 more side

    A = degrees(acos((b**2 + c**2 - a**2)/(2*b*c)))
    B = degrees(acos((a**2 + c**2 - b**2)/(2*a*c)))
    C = solve180(A,B)
    return [a,b,c,A,B,C]
#----------------------------------------------

def solveSSA(): #Pickes between solveSSAincluded and solveSSAnotincluded functions
    if includedAngle() == False:
        return solveSSAnotincluded()
    else:
        return solveSSAincluded()


#----------------- GUI OUTPUT ------------------------------
background2 = Image.open("solution.jpg")
background2 = background2.resize((1980,1000))
background2 = ImageTk.PhotoImage(background2)


solutionframe = Frame(canvas, width = 600, height = 500, bg = "black")

ans1 = Label(solutionframe, font = ("Courier", 20), text = "a = " , bg = "black", fg="white")
ans2 = Label(solutionframe, font = ("Courier", 20) , text = "b = " ,bg = "black", fg="white")
ans3 = Label(solutionframe, font = ("Courier", 20) ,text = "c = " , bg = "black", fg="white")
ans4 = Label(solutionframe, font = ("Courier", 20) , text = "A = ")
ans5 = Label(solutionframe, font = ("Courier", 20) ,text = "B = " )
ans6 = Label(solutionframe, font = ("Courier", 20) ,text = "C = ")
ans1.pack(fill = X)
ans2.pack(fill = X)
ans3.pack(fill = X)
ans4.pack(fill = X)
ans5.pack(fill = X)
ans6.pack(fill = X)
solutionframe.place(x=800, y = 225)
#--------------------------------------------------------------




solvebutton = Button(text="Solve Triangle", font = ("Courier", 22),activeforeground="light blue", command = solve) #make sure to 'command =' to initiate program
solvebutton.place(x=472, y=425) #button has to be placed after functions are defined

canvas.mainloop()
