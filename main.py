#Chess game
import turtle
import time
from os import system


#objects
scr = turtle.Screen()
draw = turtle.Turtle()





#screen
scr.setup(870,870)

#white is upper, black lowercase
P1 = turtle.Turtle()
P2 = turtle.Turtle()
P3 = turtle.Turtle()
P4 = turtle.Turtle()
P5 = turtle.Turtle()
P6 = turtle.Turtle()
P7 = turtle.Turtle()
P8 = turtle.Turtle()
R1 = turtle.Turtle()
R2 = turtle.Turtle()
N1 = turtle.Turtle()
N2 = turtle.Turtle()
Bi1 = turtle.Turtle()
Bi2 = turtle.Turtle()
Q = turtle.Turtle()
K = turtle.Turtle()


#black
p1 = turtle.Turtle()
p2 = turtle.Turtle()
p3 = turtle.Turtle()
p4 = turtle.Turtle()
p5 = turtle.Turtle()
p6 = turtle.Turtle()
p7 = turtle.Turtle()
p8 = turtle.Turtle()
r1 = turtle.Turtle()
r2 = turtle.Turtle()
n1 = turtle.Turtle()
n2 = turtle.Turtle()
bi1 = turtle.Turtle()
bi2 = turtle.Turtle()
q = turtle.Turtle()
k = turtle.Turtle()

#IMAGES TAKEN FROM::#
##https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent##
scr.addshape('wPawn.png')
scr.addshape('bPawn.png')
scr.addshape('wBishop.png')
scr.addshape('bBishop.png')
scr.addshape('wRook.png')
scr.addshape('bRook.png')
scr.addshape('wKnight.png')
scr.addshape('bKnight.png')
scr.addshape('wQueen.png')
scr.addshape('bQueen.png')
scr.addshape('wKing.png')
scr.addshape('bKing.png')


#attributes for turtles
P1.speed(0)
P2.speed(0)
P3.speed(0)
P4.speed(0)
P5.speed(0)
P6.speed(0)
P7.speed(0)
P8.speed(0)
R1.speed(0)
R2.speed(0)
N1.speed(0)
N2.speed(0)
Bi1.speed(0)
Bi2.speed(0)
K.speed(0)
Q.speed(0)
p1.speed(0)
p2.speed(0)
p3.speed(0)
p4.speed(0)
p5.speed(0)
p6.speed(0)
p7.speed(0)
p8.speed(0)
r1.speed(0)
r2.speed(0)
n1.speed(0)
n2.speed(0)
bi1.speed(0)
bi2.speed(0)
k.speed(0)
q.speed(0)

P1.setheading(90)
P2.setheading(90)
P3.setheading(90)
P4.setheading(90)
P5.setheading(90)
P6.setheading(90)
P7.setheading(90)
P8.setheading(90)
R1.setheading(90)
R2.setheading(90)
Bi1.setheading(90)
Bi2.setheading(90)
N1.setheading(90)
N2.setheading(90)
K.setheading(90)
Q.setheading(90)
p1.setheading(90)
p2.setheading(90)
p3.setheading(90)
p4.setheading(90)
p5.setheading(90)
p6.setheading(90)
p7.setheading(90)
p8.setheading(90)
bi1.setheading(90)
bi2.setheading(90)
r1.setheading(90)
r2.setheading(90)
n1.setheading(90)
n2.setheading(90)
k.setheading(90)
q.setheading(90)


P1.pu()
P2.pu()
P3.pu()
P4.pu()
P5.pu()
P6.pu()
P7.pu()
P8.pu()
R1.pu()
R2.pu()
N1.pu()
N2.pu()
Bi1.pu()
Bi2.pu()
K.pu()
Q.pu()
p1.pu()
p2.pu()
p3.pu()
p4.pu()
p5.pu()
p6.pu()
p7.pu()
p8.pu()
r1.pu()
r2.pu()
n1.pu()
n2.pu()
bi1.pu()
bi2.pu()
k.pu()
q.pu()


#for drawing board
draw.ht()
draw.pu()


#Drawing turtle specs
draw.pensize(2)
draw.color("black")
draw.speed('fastest')

#quickens turtle/time for drawing board
scr.tracer(0)

def makeBoard(lightColor, darkColor): 
  '''makes the chess board'''
  count = 0
  draw.pu()
  draw.goto(-400,400)
  draw.setheading(0)
  #checker pattern
  for i in range(8):
    for l in range(8):
      for n in range(4):
        draw.begin_fill()
        draw.color('black')
        draw.forward(100)
        draw.right(90)
      if count % 2 == 0:
        draw.color(lightColor)
      else:
        draw.color(darkColor)
      draw.end_fill()
      count += 1
      draw.color('black')
      draw.forward(100)
    count += 1
    draw.right(90)
    draw.forward(100)
    draw.right(90)
    draw.forward(800)
    draw.right(180)
  draw.pensize(4)
  draw.pu()
  draw.goto(-400,400)
  draw.pd()
  for i in range(4):
    draw.forward(800)
    draw.right(90)
  draw.pu()
  draw.goto(-420,-350)
  for i in range(4,12):
    draw.write(rows[i], font = FONT)
    draw.goto(draw.xcor(), draw.ycor() + 100)
  draw.goto(-350,-420)
  for i in range(3,11):
    draw.write(columns[i], font = FONT)
    draw.goto(draw.xcor() + 100, draw.ycor())

def setPiecesWhite():
  '''puts all white pieces in position'''
  P1.goto(-350,-250)
  P2.goto(-250,-250)
  P3.goto(-150,-250)
  P4.goto(-50,-250)
  P5.goto(50,-250)
  P6.goto(150,-250)
  P7.goto(250,-250)
  P8.goto(350,-250)
  R1.goto(-350,-350)
  R2.goto(350,-350)
  N1.goto(-250,-350)
  N2.goto(250,-350)
  Bi1.goto(-150,-350)
  Bi2.goto(150,-350)
  K.goto(50,-350)
  Q.goto(-50,-350)
  p1.goto(-350,250)
  p2.goto(-250,250)
  p3.goto(-150,250)
  p4.goto(-50,250)
  p5.goto(50,250)
  p6.goto(150,250)
  p7.goto(250,250)
  p8.goto(350,250)
  r1.goto(-350,350)
  r2.goto(350,350)
  bi1.goto(-150,350)
  bi2.goto(150,350)
  n1.goto(-250,350)
  n2.goto(250,350)
  k.goto(50,350)
  q.goto(-50,350)


def setShapes(): 
  '''gives turtles their images'''
  P1.shape('wPawn.png')
  P2.shape('wPawn.png')
  P3.shape('wPawn.png')
  P4.shape('wPawn.png')
  P5.shape('wPawn.png')
  P6.shape('wPawn.png')
  P7.shape('wPawn.png')
  P8.shape('wPawn.png')
  R1.shape('wRook.png')
  R2.shape('wRook.png')
  Bi1.shape('wBishop.png')
  Bi2.shape('wBishop.png')
  N1.shape('wKnight.png')
  N2.shape('wKnight.png')
  K.shape('wKing.png')
  Q.shape('wQueen.png')
  
  p1.shape('bPawn.png')
  p2.shape('bPawn.png')
  p3.shape('bPawn.png')
  p4.shape('bPawn.png')
  p5.shape('bPawn.png')
  p6.shape('bPawn.png')
  p7.shape('bPawn.png')
  p8.shape('bPawn.png')
  r1.shape('bRook.png')
  r2.shape('bRook.png')
  bi1.shape('bBishop.png')
  bi2.shape('bBishop.png')
  n1.shape('bKnight.png')
  n2.shape('bKnight.png')
  k.shape('bKing.png')
  q.shape('bQueen.png')



def check(x,y):
  '''what SQUARE is clicked: returns square if empty, returns turtle if occupied'''
  
  global clickCounter
  global spot
  if x > -400 and x < -300:
    if y > -400 and y < -300:#a1
      if places['a1'] != 'none':
        spot = places['a1']
      elif places['a1'] == 'none':
        spot = 'a1'
    elif y > -300 and y < -200:#a2
      if places['a2'] != 'none':
        spot = places['a2']
      elif places['a2'] == 'none':
        spot = 'a2'
    elif y > -200 and y < -100:#a3
      if places['a3'] != 'none':
        spot = places['a3']
      elif places['a3'] == 'none':
        spot = 'a3'
    elif y > -100 and y < 0:#a4
      if places['a4'] != 'none':
        spot = places['a4']
      elif places['a4'] == 'none':
        spot = 'a4'
    elif y > 0 and y < 100:#a5
      if places['a5'] != 'none':
        spot = places['a5']
      elif places['a5'] == 'none':
        spot = 'a5'
    elif y > 100 and y < 200:#a6
      if places['a6'] != 'none':
        spot = places['a6']
      elif places['a6'] == 'none':
        spot = 'a6'
    elif y > 200 and y < 300:#a7
      if places['a7'] != 'none':
        spot = places['a7']
      elif places['a7'] == 'none':
        spot = 'a7'
    elif y > 300 and y < 400:#a8
      if places['a8'] != 'none':
        spot = places['a8']
      elif places['a8'] == 'none':
        spot = 'a8'
  elif x > -300 and x < -200:
    if y > -400 and y < -300:#b1
      if places['b1'] != 'none':
        spot = places['b1']
      elif places['b1'] == 'none':
        spot = 'b1'
    elif y > -300 and y < -200:#b2
      if places['b2'] != 'none':
        spot = places['b2']
      elif places['b2'] == 'none':
        spot = 'b2'
    elif y > -200 and y < -100:#b3
      if places['b3'] != 'none':
        spot = places['b3']
      elif places['b3'] == 'none':
        spot = 'b3'
    elif y > -100 and y < 0:#b4
      if places['b4'] != 'none':
        spot = places['b4']
      elif places['b4'] == 'none':
        spot = 'b4'
    elif y > 0 and y < 100:#b5
      if places['b5'] != 'none':
        spot = places['b5']
      elif places['b5'] == 'none':
        spot = 'b5'
    elif y > 100 and y < 200:#b6
      if places['b6'] != 'none':
        spot = places['b6']
      elif places['b6'] == 'none':
        spot = 'b6'
    elif y > 200 and y < 300:#b7
      if places['b7'] != 'none':
        spot = places['b7']
      elif places['b7'] == 'none':
        spot = 'b7'
    elif y > 300 and y < 400:#b8
      if places['b8'] != 'none':
        spot = places['b8']
      elif places['b8'] == 'none':
        spot = 'b8'
  elif x > -200 and x < -100:
    if y > -400 and y < -300:#c1
      if places['c1'] != 'none':
        spot = places['c1']
      elif places['c1'] == 'none':
        spot = 'c1'
    elif y > -300 and y < -200:#c2
      if places['c2'] != 'none':
        spot = places['c2']
      elif places['c2'] == 'none':
        spot = 'c2'
    elif y > -200 and y < -100:#c3
      if places['c3'] != 'none':
        spot = places['c3']
      elif places['c3'] == 'none':
        spot = 'c3'
    elif y > -100 and y < 0:#c4
      if places['c4'] != 'none':
        spot = places['c4']
      elif places['c4'] == 'none':
        spot = 'c4'
    elif y > 0 and y < 100:#c5
      if places['c5'] != 'none':
        spot = places['c5']
      elif places['c5'] == 'none':
        spot = 'c5'
    elif y > 100 and y < 200:#c6
      if places['c6'] != 'none':
        spot = places['c6']
      elif places['c6'] == 'none':
        spot = 'c6'
    elif y > 200 and y < 300:#c7
      if places['c7'] != 'none':
        spot = places['c7']
      elif places['c7'] == 'none':
        spot = 'c7'
    elif y > 300 and y < 400:#c8
      if places['c8'] != 'none':
        spot = places['c8']
      elif places['c8'] == 'none':
        spot = 'c8'
  elif x > -100 and x < 0:
    if y > -400 and y < -300:#d1
      if places['d1'] != 'none':
        spot = places['d1']
      elif places['d1'] == 'none':
        spot = 'd1'
    elif y > -300 and y < -200:#d2
      if places['d2'] != 'none':
        spot = places['d2']
      elif places['d2'] == 'none':
        spot = 'd2'
    elif y > -200 and y < -100:#d3
      if places['d3'] != 'none':
        spot = places['d3']
      elif places['d3'] == 'none':
        spot = 'd3'
    elif y > -100 and y < 0:#d4
      if places['d4'] != 'none':
        spot = places['d4']
      elif places['d4'] == 'none':
        spot = 'd4'
    elif y > 0 and y < 100:#d5
      if places['d5'] != 'none':
        spot = places['d5']
      elif places['d5'] == 'none':
        spot = 'd5'
    elif y > 100 and y < 200:#d6
      if places['d6'] != 'none':
        spot = places['d6']
      elif places['d6'] == 'none':
        spot = 'd6'
    elif y > 200 and y < 300:#d7
      if places['d7'] != 'none':
        spot = places['d7']
      elif places['d7'] == 'none':
        spot = 'd7'
    elif y > 300 and y < 400:#d8
      if places['d8'] != 'none':
        spot = places['d8']
      elif places['d8'] == 'none':
        spot = 'd8'
  elif x > 0 and x < 100:
    if y > -400 and y < -300:#e1
      if places['e1'] != 'none':
        spot = places['e1']
      elif places['e1'] == 'none':
        spot = 'e1'
    elif y > -300 and y < -200:#e2
      if places['e2'] != 'none':
        spot = places['e2']
      elif places['e2'] == 'none':
        spot = 'e2'
    elif y > -200 and y < -100:#e3
      if places['e3'] != 'none':
        spot = places['e3']
      elif places['e3'] == 'none':
        spot = 'e3'
    elif y > -100 and y < 0:#e4
      if places['e4'] != 'none':
        spot = places['e4']
      elif places['e4'] == 'none':
        spot = 'e4'
    elif y > 0 and y < 100:#e5
      if places['e5'] != 'none':
        spot = places['e5']
      elif places['e5'] == 'none':
        spot = 'e5'
    elif y > 100 and y < 200:#e6
      if places['e6'] != 'none':
        spot = places['e6']
      elif places['e6'] == 'none':
        spot = 'e6'
    elif y > 200 and y < 300:#e7
      if places['e7'] != 'none':
        spot = places['e7']
      elif places['e7'] == 'none':
        spot = 'e7'
    elif y > 300 and y < 400:#e8
      if places['e8'] != 'none':
        spot = places['e8']
      elif places['e8'] == 'none':
        spot = 'e8'
  elif x > 100 and x < 200:
    if y > -400 and y < -300:#f1
      if places['f1'] != 'none':
        spot = places['f1']
      elif places['f1'] == 'none':
        spot = 'f1'
    elif y > -300 and y < -200:#f2
      if places['f2'] != 'none':
        spot = places['f2']
      elif places['f2'] == 'none':
        spot = 'f2'
    elif y > -200 and y < -100:#f3
      if places['f3'] != 'none':
        spot = places['f3']
      elif places['f3'] == 'none':
        spot = 'f3'
    elif y > -100 and y < 0:#f4
      if places['f4'] != 'none':
        spot = places['f4']
      elif places['f4'] == 'none':
        spot = 'f4'
    elif y > 0 and y < 100:#f5
      if places['f5'] != 'none':
        spot = places['f5']
      elif places['f5'] == 'none':
        spot = 'f5'
    elif y > 100 and y < 200:#f6
      if places['f6'] != 'none':
        spot = places['f6']
      elif places['f6'] == 'none':
        spot = 'f6'
    elif y > 200 and y < 300:#f7
      if places['f7'] != 'none':
        spot = places['f7']
      elif places['f7'] == 'none':
        spot = 'f7'
    elif y > 300 and y < 400:#f8
      if places['f8'] != 'none':
        spot = places['f8']
      elif places['f8'] == 'none':
        spot = 'f8'
  elif x > 200 and x < 300:
    if y > -400 and y < -300:#g1
      if places['g1'] != 'none':
        spot = places['g1']
      elif places['g1'] == 'none':
        spot = 'g1'
    elif y > -300 and y < -200:#g2
      if places['g2'] != 'none':
        spot = places['g2']
      elif places['g2'] == 'none':
        spot = 'g2'
    elif y > -200 and y < -100:#g3
      if places['g3'] != 'none':
        spot = places['g3']
      elif places['g3'] == 'none':
        spot = 'g3'
    elif y > -100 and y < 0:#g4
      if places['g4'] != 'none':
        spot = places['g4']
      elif places['g4'] == 'none':
        spot = 'g4'
    elif y > 0 and y < 100:#g5
      if places['g5'] != 'none':
        spot = places['g5']
      elif places['g5'] == 'none':
        spot = 'g5'
    elif y > 100 and y < 200:#g6
      if places['g6'] != 'none':
        spot = places['g6']
      elif places['g6'] == 'none':
        spot = 'g6'
    elif y > 200 and y < 300:#g7
      if places['g7'] != 'none':
        spot = places['g7']
      elif places['g7'] == 'none':
        spot = 'g7'
    elif y > 300 and y < 400:#g8
      if places['g8'] != 'none':
        spot = places['g8']
      elif places['g8'] == 'none':
        spot = 'g8'
  elif x > 300 and x < 400:
    if y > -400 and y < -300:#h1
      if places['h1'] != 'none':
        spot = places['h1']
      elif places['h1'] == 'none':
        spot = 'h1'
    elif y > -300 and y < -200:#h2
      if places['h2'] != 'none':
        spot = places['h2']
      elif places['h2'] == 'none':
        spot = 'h2'
    elif y > -200 and y < -100:#h3
      if places['h3'] != 'none':
        spot = places['h3']
      elif places['h3'] == 'none':
        spot = 'h3'
    elif y > -100 and y < 0:#h4
      if places['h4'] != 'none':
        spot = places['h4']
      elif places['h4'] == 'none':
        spot = 'h4'
    elif y > 0 and y < 100:#h5
      if places['h5'] != 'none':
        spot = places['h5']
      elif places['h5'] == 'none':
        spot = 'h5'
    elif y > 100 and y < 200:#h6
      if places['h6'] != 'none':
        spot = places['h6']
      elif places['h6'] == 'none':
        spot = 'h6'
    elif y > 200 and y < 300:#h7
      if places['h7'] != 'none':
        spot = places['h7']
      elif places['h7'] == 'none':
        spot = 'h7'
    elif y > 300 and y < 400:#h8
      if places['h8'] != 'none':
        spot = places['h8']
      elif places['h8'] == 'none':
        spot = 'h8'
  else:
    spot = 'none'

def wInList(piece):
  '''if occupied square piece is: 0 - same, 1 - empty, 2- opposite color'''
  if piece in wPieces:
    return 0
  if piece in bPieces:
    return 2
  return 1

def bInList(piece):
  '''same as white, except backwards'''
  if piece in bPieces:
    return 0
  if piece in wPieces:
    return 2
  return 1
  
def find(piece):
  '''finds and returns position of turt'''
  if piece == 'P1':
    return locations1[P1.pos()]
  elif piece == 'P2':
    return locations1[P2.pos()]
  elif piece == 'P3':
    return locations1[P3.pos()]
  elif piece == 'P4':
    return locations1[P4.pos()]
  elif piece == 'P5':
    return locations1[P5.pos()]
  elif piece == 'P6':
    return locations1[P6.pos()]
  elif piece == 'P7':
    return locations1[P7.pos()]
  elif piece == 'P8':
    return locations1[P8.pos()]
  elif piece == 'R1':
    return locations1[R1.pos()]
  elif piece == 'R2':
    return locations1[R2.pos()]
  elif piece == 'Bi1':
    return locations1[Bi1.pos()]
  elif piece == 'Bi2':
    return locations1[Bi2.pos()]
  elif piece == 'N1':
    return locations1[N1.pos()]
  elif piece == 'N2':
    return locations1[N2.pos()]
  elif piece == 'K':
    return locations1[K.pos()]
  elif piece == 'Q':
    return locations1[Q.pos()]
  elif piece == 'p1':
    return locations1[p1.pos()]
  elif piece == 'p2':
    return locations1[p2.pos()]
  elif piece == 'p3':
    return locations1[p3.pos()]
  elif piece == 'p4':
    return locations1[p4.pos()]
  elif piece == 'p5':
    return locations1[p5.pos()]
  elif piece == 'p6':
    return locations1[p6.pos()]
  elif piece == 'p7':
    return locations1[p7.pos()]
  elif piece == 'p8':
    return locations1[p8.pos()]
  elif piece == 'r1':
    return locations1[r1.pos()]
  elif piece == 'r2':
    return locations1[r2.pos()]
  elif piece == 'bi1':
    return locations1[bi1.pos()]
  elif piece == 'bi2':
    return locations1[bi2.pos()]
  elif piece == 'n1':
    return locations1[n1.pos()]
  elif piece == 'n2':
    return locations1[n2.pos()]
  elif piece == 'k':
    return locations1[k.pos()]
  elif piece == 'q':
    return locations1[q.pos()]




def pawn1(x,y):
  '''for black pawn 1'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('p1')
  r = 0
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '7':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) + 1) or var2[1] == str(int(spot[1]) + 2)):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p1'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p1'
            places[spot] = 'none'
            count = 0
            return
          else:
            p1.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p1'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p1'
          places[spot] = 'none'
          count = 0
          return
        p1.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) + 1):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p1'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p1'
            places[spot] = 'none'
            count = 0
            return
          else:
            p1.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p1'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p1'
          places[spot] = 'none'
          count = 0
          return
        p1.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1])-1) == var3[1]:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'p1'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p1'
          places[var3] = 'none'
          count = 0
          return
        else:
          p1.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'p1'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'p1'
        places[var3] = 'none'
        count = 0
        return
      p1.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def pawn2(x,y):
  '''black pawn 2'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('p2')
  r = 1
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '7':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) + 1) or var2[1] == str(int(spot[1]) + 2)):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p2'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p2'
            places[spot] = 'none'
            count = 0
            return
          else:
            p2.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p2'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p2'
          places[spot] = 'none'
          count = 0
          return
        p2.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) + 1):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p2'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p2'
            places[spot] = 'none'
            count = 0
            return
          else:
            p2.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p2'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p2'
          places[spot] = 'none'
          count = 0
          return
        p2.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1])-1) == var3[1]:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'p2'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p2'
          places[var3] = 'none'
          count = 0
          return
        else:
          p2.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'p2'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'p2'
        places[var3] = 'none'
        count = 0
        return
      p2.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def pawn3(x,y):
  '''black pawn 3'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('p3')
  r = 2
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '7':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) + 1) or var2[1] == str(int(spot[1]) + 2)):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p3'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p3'
            places[spot] = 'none'
            count = 0
            return
          else:
            p3.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p3'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p3'
          places[spot] = 'none'
          count = 0
          return
        p3.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) + 1):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p3'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p3'
            places[spot] = 'none'
            count = 0
            return
          else:
            p3.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p3'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p3'
          places[spot] = 'none'
          count = 0
          return
        p3.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1])-1) == var3[1]:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'p3'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p3'
          places[var3] = 'none'
          count = 0
          return
        else:
          p3.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'p3'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'p3'
        places[var3] = 'none'
        count = 0
        return
      p3.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def pawn4(x,y):
  '''black pawn 4'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('p4')
  r = 3
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '7':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) + 1) or var2[1] == str(int(spot[1]) + 2)):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p4'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p4'
            places[spot] = 'none'
            count = 0
            return
          else:
            p4.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p4'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p4'
          places[spot] = 'none'
          count = 0
          return
        p4.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) + 1):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p4'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p4'
            places[spot] = 'none'
            count = 0
            return
          else:
            p4.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p4'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p4'
          places[spot] = 'none'
          count = 0
          return
        p4.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1])-1) == var3[1]:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'p4'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p4'
          places[var3] = 'none'
          count = 0
          return
        else:
          p4.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'p4'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'p4'
        places[var3] = 'none'
        count = 0
        return
      p4.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def pawn5(x,y):
  '''black pawn 5'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('p5')
  r = 4
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '7':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) + 1) or var2[1] == str(int(spot[1]) + 2)):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p5'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p5'
            places[spot] = 'none'
            count = 0
            return
          else:
            p5.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p5'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p5'
          places[spot] = 'none'
          count = 0
          return
        p5.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) + 1):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p5'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p5'
            places[spot] = 'none'
            count = 0
            return
          else:
            p5.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p5'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p5'
          places[spot] = 'none'
          count = 0
          return
        p5.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1])-1) == var3[1]:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'p5'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p5'
          places[var3] = 'none'
          count = 0
          return
        else:
          p5.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'p5'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'p5'
        places[var3] = 'none'
        count = 0
        return
      p5.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def pawn6(x,y):
  '''black pawn 6'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('p6')
  r = 5
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '7':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) + 1) or var2[1] == str(int(spot[1]) + 2)):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p6'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p6'
            places[spot] = 'none'
            count = 0
            return
          else:
            p6.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p6'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p6'
          places[spot] = 'none'
          count = 0
          return
        p6.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) + 1):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p6'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p6'
            places[spot] = 'none'
            count = 0
            return
          else:
            p6.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p6'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p6'
          places[spot] = 'none'
          count = 0
          return
        p6.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1])-1) == var3[1]:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'p6'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p6'
          places[var3] = 'none'
          count = 0
          return
        else:
          p6.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'p6'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'p6'
        places[var3] = 'none'
        count = 0
        return
      p6.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def pawn7(x,y):
  '''black pawn 7'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('p7')
  r = 6
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '7':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) + 1) or var2[1] == str(int(spot[1]) + 2)):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p7'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p7'
            places[spot] = 'none'
            count = 0
            return
          else:
            p7.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p7'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p7'
          places[spot] = 'none'
          count = 0
          return
        p7.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) + 1):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p7'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p7'
            places[spot] = 'none'
            count = 0
            return
          else:
            p7.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p7'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p7'
          places[spot] = 'none'
          count = 0
          return
        p7.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1])-1) == var3[1]:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'p7'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p7'
          places[var3] = 'none'
          count = 0
          return
        else:
          p7.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'p7'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'p7'
        places[var3] = 'none'
        count = 0
        return
      p7.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def pawn8(x,y):
  '''black pawn 8'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('p8')
  r = 7
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '7':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) + 1) or var2[1] == str(int(spot[1]) + 2)):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p8'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p8'
            places[spot] = 'none'
            count = 0
            return
          else:
            p8.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p8'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p8'
          places[spot] = 'none'
          count = 0
          return
        p8.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) + 1):
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'p8'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'p8'
            places[spot] = 'none'
            count = 0
            return
          else:
            p8.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'p8'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p8'
          places[spot] = 'none'
          count = 0
          return
        p8.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) - 1)]
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1])-1) == var3[1]:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'p8'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'p8'
          places[var3] = 'none'
          count = 0
          return
        else:
          p8.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'p8'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'p8'
        places[var3] = 'none'
        count = 0
        return
      p8.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) - 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) - 1)]
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def rook1(x,y):
  '''black rook 1'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  global rook1Moved
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('r1')
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[0] == var2[0] or spot[1] == var2[1]:
      var4 = 0
      if int(var2[1]) > int(spot[1]):
        n = int(var2[1]) - int(spot[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[spot] = 'r1'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r1'
              places[spot] = 'none'
              count = 0
              return
            else:
              r1.goto(locations[spot])
              turn = 'white'
              rook1Moved = True
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'r1'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'r1'
            places[spot] = 'none'
            count = 0
            return
          r1.goto(locations[spot])
          turn = 'white'
          rook1Moved = True
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(spot[1]):
        n = columns.index(spot[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == n - m - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[spot] = 'r1'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'r1'
                places[spot] = 'none'
                count = 0
                return
              else:
                r1.goto(locations[spot])
                turn = 'white'
                rook1Moved = True
                count = 0
                return
            places[var2] = 'none'
            places[spot] = 'r1'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r1'
              places[spot] = 'none'
              count = 0
              return
            r1.goto(locations[spot])
            turn = 'white'
            rook1Moved = True
            count = 0
            return
          else:
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == m - n - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[spot] = 'r1'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'r1'
                places[spot] = 'none'
                count = 0
                return
              else:
                r1.goto(locations[spot])
                turn = 'white'
                rook1Moved = True
                count = 0
                return
            places[var2] = 'none'
            places[spot] = 'r1'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r1'
              places[spot] = 'none'
              count = 0
              return
            r1.goto(locations[spot])
            turn = 'white'
            rook1Moved = True
            count = 0
            return
          else:
            count = 0
            return
      else:
        n = int(spot[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[spot[0] + str(int(spot[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[spot] = 'r1'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r1'
              places[spot] = 'none'
              count = 0
              return
            else:
              r1.goto(locations[spot])
              turn = 'white'
              rook1Moved = True
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'r1'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'r1'
            places[spot] = 'none'
            count = 0
            return
          r1.goto(locations[spot])
          turn = 'white'
          rook1Moved = True
          count = 0
          return
        else:
          count = 0
          return
    else:
      count = 0
      return
  elif var == 2:
    var5 = find(spot)
    if var5[0] == var2[0] or var5[1] == var2[1]:
      var4 = 0
      if int(var2[1]) > int(var5[1]):
        n = int(var2[1]) - int(var5[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[var5] = 'r1'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r1'
              places[var5] = 'none'
              count = 0
              return
            else:
              r1.goto(locations[spot])
              turn = 'white'
              rook1Moved = True
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var5] = 'r1'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'r1'
            places[var5] = 'none'
            count = 0
            return
          r1.goto(locations[var5])
          turn = 'white'
          rook1Moved = True
          kill(spot)
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(var5[1]):
        n = columns.index(var5[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + var5[1]] == 'none':
              var4 += 1
          if var4 == n - m - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[var5] = 'r1'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'r1'
                places[var5] = 'none'
                count = 0
                return
              else:
                r1.goto(locations[spot])
                turn = 'white'
                rook1Moved = True
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var5] = 'r1'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r1'
              places[var5] = 'none'
              count = 0
              return
            r1.goto(locations[var5])
            turn = 'white'
            rook1Moved = True
            kill(spot)
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + var5[1]] == 'none':
              var4 += 1
          if var4 == m - n - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[var5] = 'r1'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'r1'
                places[var5] = 'none'
                count = 0
                return
              else:
                r1.goto(locations[spot])
                turn = 'white'
                rook1Moved = True
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var5] = 'r1'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r1'
              places[var5] = 'none'
              count = 0
              return
            r1.goto(locations[var5])
            turn = 'white'
            rook1Moved = True
            kill(spot)
            count = 0
            return
      else:
        n = int(var5[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[var5[0] + str(int(var5[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[var5] = 'r1'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r1'
              places[var5] = 'none'
              count = 0
              return
            else:
              r1.goto(locations[spot])
              turn = 'white'
              rook1Moved = True
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var5] = 'r1'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'r1'
            places[var5] = 'none'
            count = 0
            return
          r1.goto(locations[var5])
          turn = 'white'
          rook1Moved = True
          kill(spot)
          count = 0
          return
    else:
      count = 0
      return




def rook2(x,y):
  '''black rook 2'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  global rook2Moved
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('r2')
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[0] == var2[0] or spot[1] == var2[1]:
      var4 = 0
      if int(var2[1]) > int(spot[1]):
        n = int(var2[1]) - int(spot[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[spot] = 'r2'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r2'
              places[spot] = 'none'
              count = 0
              return
            else:
              r2.goto(locations[spot])
              turn = 'white'
              rook2Moved = True
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'r2'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'r2'
            places[spot] = 'none'
            count = 0
            return
          r2.goto(locations[spot])
          turn = 'white'
          rook2Moved = True
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(spot[1]):
        n = columns.index(spot[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == n - m - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[spot] = 'r2'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'r2'
                places[spot] = 'none'
                count = 0
                return
              else:
                r2.goto(locations[spot])
                turn = 'white'
                rook2Moved = True
                count = 0
                return
            places[var2] = 'none'
            places[spot] = 'r2'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r2'
              places[spot] = 'none'
              count = 0
              return
            r2.goto(locations[spot])
            turn = 'white'
            rook2Moved = True
            count = 0
            return
          else:
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == m - n - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[spot] = 'r2'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'r2'
                places[spot] = 'none'
                count = 0
                return
              else:
                r2.goto(locations[spot])
                turn = 'white'
                rook2Moved = True
                count = 0
                return
            places[var2] = 'none'
            places[spot] = 'r2'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r2'
              places[spot] = 'none'
              count = 0
              return
            r2.goto(locations[spot])
            turn = 'white'
            rook2Moved = True
            count = 0
            return
          else:
            count = 0
            return
      else:
        n = int(spot[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[spot[0] + str(int(spot[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[spot] = 'r2'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r2'
              places[spot] = 'none'
              count = 0
              return
            else:
              r2.goto(locations[spot])
              turn = 'white'
              rook2Moved = True
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'r2'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'r2'
            places[spot] = 'none'
            count = 0
            return
          r2.goto(locations[spot])
          turn = 'white'
          rook2Moved = True
          count = 0
          return
        else:
          count = 0
          return
    else:
      count = 0
      return
  elif var == 2:
    var5 = find(spot)
    if var5[0] == var2[0] or var5[1] == var2[1]:
      var4 = 0
      if int(var2[1]) > int(var5[1]):
        n = int(var2[1]) - int(var5[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[var5] = 'r2'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r2'
              places[var5] = 'none'
              count = 0
              return
            else:
              r2.goto(locations[spot])
              turn = 'white'
              rook2Moved = True
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var5] = 'r2'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'r2'
            places[var5] = 'none'
            count = 0
            return
          r2.goto(locations[var5])
          turn = 'white'
          rook2Moved = True
          kill(spot)
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(var5[1]):
        n = columns.index(var5[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + var5[1]] == 'none':
              var4 += 1
          if var4 == n - m - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[var5] = 'r2'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'r2'
                places[var5] = 'none'
                count = 0
                return
              else:
                r2.goto(locations[spot])
                turn = 'white'
                rook2Moved = True
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var5] = 'r2'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r2'
              places[var5] = 'none'
              count = 0
              return
            r2.goto(locations[var5])
            turn = 'white'
            rook2Moved = True
            kill(spot)
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + var5[1]] == 'none':
              var4 += 1
          if var4 == m - n - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[var5] = 'r2'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'r2'
                places[var5] = 'none'
                count = 0
                return
              else:
                r2.goto(locations[spot])
                turn = 'white'
                rook2Moved = True
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var5] = 'r2'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r2'
              places[var5] = 'none'
              count = 0
              return
            r2.goto(locations[var5])
            turn = 'white'
            rook2Moved = True
            kill(spot)
            count = 0
            return
      else:
        n = int(var5[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[var5[0] + str(int(var5[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[var5] = 'r2'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'r2'
              places[var5] = 'none'
              count = 0
              return
            else:
              r2.goto(locations[spot])
              turn = 'white'
              rook2Moved = True
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var5] = 'r2'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'r2'
            places[var5] = 'none'
            count = 0
            return
          r2.goto(locations[var5])
          turn = 'white'
          rook2Moved = True
          kill(spot)
          count = 0
          return
    else:
      count = 0
      return




def bishop1(x,y):
  '''black bishop 1'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('bi1')
  updates('white')
  var4 = 0
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    var5 = False
    var6 = 0
    for i in range(1,9):
      if spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
        var5 = 'dl'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
        var5 = 'dr'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
        var5 = 'ur'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
        var5 = 'ul'
        var6 = i
    if var6 == 1:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[spot] = 'bi1'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'bi1'
          places[spot] = 'none'
          count = 0
          return
        else:
          bi1.goto(locations[spot])
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'bi1'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'bi1'
        places[spot] = 'none'
        count = 0
        return
      bi1.goto(locations[spot])
      turn = 'white'
      count = 0
      return
    elif var5 == 'ur':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'ul':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'dr':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    elif var5 == 'dl':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    if var4 == var6 - 1:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[spot] = 'bi1'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'bi1'
          places[spot] = 'none'
          count = 0
          return
        else:
          bi1.goto(locations[spot])
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'bi1'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'bi1'
        places[spot] = 'none'
        count = 0
        return
      bi1.goto(locations[spot])
      turn = 'white'
      count = 0
      return
    else:
      count = 0
      return
    
  elif var == 2:
    var3 = find(spot)
    var5 = False
    var6 = 0
    for i in range(1,9):
      if var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
        var5 = 'dl'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
        var5 = 'dr'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
        var5 = 'ur'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
        var5 = 'ul'
        var6 = i
    if var6 == 1:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'bi1'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'bi1'
          places[var3] = 'none'
          count = 0
          return
        else:
          bi1.goto(locations[var3])
          turn = 'white'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'bi1'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'bi1'
        places[var3] = 'none'
        count = 0
        return
      bi1.goto(locations[var3])
      turn = 'white'
      kill(spot)
      count = 0
      return
    elif var5 == 'ur':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'ul':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'dr':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    elif var5 == 'dl':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    if var4 == var6 - 1:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'bi1'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'bi1'
          places[var3] = 'none'
          count = 0
          return
        else:
          bi1.goto(locations[var3])
          turn = 'white'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'bi1'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'bi1'
        places[var3] = 'none'
        count = 0
        return
      bi1.goto(locations[var3])
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
      count = 0
      return




def bishop2(x,y):
  '''black bishop 2'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('bi2')
  updates('white')
  var4 = 0
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    var5 = False
    var6 = 0
    for i in range(1,9):
      if spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
        var5 = 'dl'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
        var5 = 'dr'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
        var5 = 'ur'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
        var5 = 'ul'
        var6 = i
    if var6 == 1:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[spot] = 'bi2'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'bi2'
          places[spot] = 'none'
          count = 0
          return
        else:
          bi2.goto(locations[spot])
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'bi2'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'bi2'
        places[spot] = 'none'
        count = 0
        return
      bi2.goto(locations[spot])
      turn = 'white'
      count = 0
      return
    elif var5 == 'ur':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'ul':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'dr':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    elif var5 == 'dl':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    if var4 == var6 - 1:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[spot] = 'bi2'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'bi2'
          places[spot] = 'none'
          count = 0
          return
        else:
          bi2.goto(locations[spot])
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'bi2'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'bi2'
        places[spot] = 'none'
        count = 0
        return
      bi2.goto(locations[spot])
      turn = 'white'
      count = 0
      return
    else:
      count = 0
      return
    
  elif var == 2:
    var3 = find(spot)
    var5 = False
    var6 = 0
    for i in range(1,9):
      if var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
        var5 = 'dl'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
        var5 = 'dr'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
        var5 = 'ur'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
        var5 = 'ul'
        var6 = i
    if var6 == 1:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'bi2'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'bi2'
          places[var3] = 'none'
          count = 0
          return
        else:
          bi2.goto(locations[var3])
          turn = 'white'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'bi2'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'bi2'
        places[var3] = 'none'
        count = 0
        return
      bi2.goto(locations[var3])
      turn = 'white'
      kill(spot)
      count = 0
      return
    elif var5 == 'ur':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'ul':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'dr':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    elif var5 == 'dl':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    if var4 == var6 - 1:
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'bi2'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'bi2'
          places[var3] = 'none'
          count = 0
          return
        else:
          bi2.goto(locations[var3])
          turn = 'white'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'bi2'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'bi2'
        places[var3] = 'none'
        count = 0
        return
      bi2.goto(locations[var3])
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
      count = 0
      return




def knight1(x,y):
  '''black knight 1'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('n1')
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if (columns.index(var2[0]) == columns.index(spot[0]) + 1 or columns.index(var2[0]) == columns.index(spot[0]) - 1) \
    and (int(spot[1]) == int(var2[1]) + 2 or int(spot[1]) == int(var2[1]) - 2):
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[spot] = 'n1'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'n1'
          places[spot] = 'none'
          count = 0
          return
        else:
          n1.goto(locations[spot])
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'n1'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'n1'
        places[spot] = 'none'
        count = 0
        return
      n1.goto(locations[spot])
      turn = 'white'
      count = 0
      return
    elif (columns.index(var2[0]) == columns.index(spot[0]) + 2 or columns.index(var2[0]) == columns.index(spot[0]) - 2) \
    and (int(spot[1]) == int(var2[1]) + 1 or int(spot[1]) == int(var2[1]) - 1):
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[spot] = 'n1'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'n1'
          places[spot] = 'none'
          count = 0
          return
        else:
          n1.goto(locations[spot])
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'n1'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'n1'
        places[spot] = 'none'
        count = 0
        return
      n1.goto(locations[spot])
      turn = 'white'
      count = 0
      return
    else:
      count = 0
      return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) \
    and (int(var3[1]) == int(var2[1]) + 2 or int(var3[1]) == int(var2[1]) - 2):
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'n1'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'n1'
          places[var3] = 'none'
          count = 0
          return
        else:
          n1.goto(locations[var3])
          turn = 'white'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'n1'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'n1'
        places[var3] = 'none'
        count = 0
        return
      n1.goto(locations[var3])
      turn = 'white'
      kill(spot)
      count = 0
      return
    elif (columns.index(var2[0]) == columns.index(var3[0]) + 2 or columns.index(var2[0]) == columns.index(var3[0]) - 2) \
    and (int(var3[1]) == int(var2[1]) + 1 or int(var3[1]) == int(var2[1]) - 1):
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'n1'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'n1'
          places[var3] = 'none'
          count = 0
          return
        else:
          n1.goto(locations[var3])
          turn = 'white'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'n1'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'n1'
        places[var3] = 'none'
        count = 0
        return
      n1.goto(locations[var3])
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
      count = 0
      return




def knight2(x,y):
  '''black knight 2'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('n2')
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if (columns.index(var2[0]) == columns.index(spot[0]) + 1 or columns.index(var2[0]) == columns.index(spot[0]) - 1) \
    and (int(spot[1]) == int(var2[1]) + 2 or int(spot[1]) == int(var2[1]) - 2):
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[spot] = 'n2'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'n2'
          places[spot] = 'none'
          count = 0
          return
        else:
          n2.goto(locations[spot])
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'n2'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'n2'
        places[spot] = 'none'
        count = 0
        return
      n2.goto(locations[spot])
      turn = 'white'
      count = 0
      return
    elif (columns.index(var2[0]) == columns.index(spot[0]) + 2 or columns.index(var2[0]) == columns.index(spot[0]) - 2) \
    and (int(spot[1]) == int(var2[1]) + 1 or int(spot[1]) == int(var2[1]) - 1):
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[spot] = 'n2'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'n2'
          places[spot] = 'none'
          count = 0
          return
        else:
          n2.goto(locations[spot])
          turn = 'white'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'n2'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'n2'
        places[spot] = 'none'
        count = 0
        return
      n2.goto(locations[spot])
      turn = 'white'
      count = 0
      return
    else:
      count = 0
      return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) \
    and (int(var3[1]) == int(var2[1]) + 2 or int(var3[1]) == int(var2[1]) - 2):
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'n2'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'n2'
          places[var3] = 'none'
          count = 0
          return
        else:
          n2.goto(locations[var3])
          turn = 'white'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'n2'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'n2'
        places[var3] = 'none'
        count = 0
        return
      n2.goto(locations[var3])
      turn = 'white'
      kill(spot)
      count = 0
      return
    elif (columns.index(var2[0]) == columns.index(var3[0]) + 2 or columns.index(var2[0]) == columns.index(var3[0]) - 2) \
    and (int(var3[1]) == int(var2[1]) + 1 or int(var3[1]) == int(var2[1]) - 1):
      if in_check(kPos, 'black'):
        places[var2] = 'none'
        places[var3] = 'n2'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'n2'
          places[var3] = 'none'
          count = 0
          return
        else:
          n2.goto(locations[var3])
          turn = 'white'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'n2'
      updates('white')
      if in_check(kPos, 'black'):
        places[var2] = 'n2'
        places[var3] = 'none'
        count = 0
        return
      n2.goto(locations[var3])
      turn = 'white'
      kill(spot)
      count = 0
      return
    else:
      count = 0
      return




def king(x,y):
  '''black king'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  global kingMoved
  global rook1Moved
  global rook2Moved
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  updates('white')
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('k')
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot == 'c8' and kingMoved == False and rook1Moved == False and places['b8'] == 'none' and places['c8'] == 'none' and places['d8'] == 'none':
      if (not(any('b8' in i for i in wline) and not(any('c8' in i for i in wline))) and not(any('g8' in i for i in wline))):
        if not(in_check(var2, 'black')):
          places[var2] = 'none'
          places[locations1[r1.pos()]] = 'none'
          places[spot] = kPos
          k.goto(locations[spot])
          r1.goto(locations['d8'])
          places[locations1[r1.pos()]] = 'r1'
          turn = 'white'
          count = 0
          kingMoved = True
          rook1Moved = True
        else:
          count = 0
          return
      else:
        count = 0
        return
    elif spot == 'g8' and kingMoved == False and rook2Moved == False and places['e8'] == 'none' and places['f8'] == 'none':
      if (not(any('e8' in i for i in wline) and not(any('f8' in i for i in wline)))):
        if not(in_check(var2, 'black')):
          places[var2] = 'none'
          k.goto(locations[spot])
          places[spot] = kPos
          places[locations1[r2.pos()]] = 'none'
          r2.goto(locations['f8'])
          places[locations1[r2.pos()]] = 'r2'
          turn = 'white'
          count = 0
          kingMoved = True
          rook2Moved = True
        else:
          count = 0
          return
      else:
        count= 0
        return
    else:
      if (int(spot[1]) == int(var2[1]) or int(spot[1]) == int(var2[1]) + 1 or int(spot[1]) == int(var2[1]) - 1) \
      and spot[0] == var2[0] or spot[0] == columns[columns.index(var2[0]) + 1] or spot[0] == columns[columns.index(var2[0]) - 1]:
        if not(in_check(spot, 'black')):
          places[var2] = 'none'
          k.goto(locations[spot])
          places[spot] = kPos
          turn = 'white'
          count = 0
          kingMoved = True
        else:
          count = 0
          return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (int(var3[1]) == int(var2[1]) or int(var3[1]) == int(var2[1]) + 1 or int(var3[1]) == int(var2[1]) - 1) \
    and var3[0] == var2[0] or var3[0] == columns[columns.index(var2[0]) + 1] or var3[0] == columns[columns.index(var2[0]) - 1]:
      if not(in_check(var3, 'black')):
        places[var2] = 'none'
        k.goto(locations[var3])
        places[var3] = kPos
        turn = 'white'
        kill(spot)
        count = 0
        kingMoved = True
      else:
        count = 0
        return
    else:
      count = 0
      return




def queen(x,y):
  '''black queen'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'white':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = bInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('q')
  updates('white')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[0] == var2[0] or spot[1] == var2[1]:
      var4 = 0
      if int(var2[1]) > int(spot[1]):
        n = int(var2[1]) - int(spot[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[spot] = 'q'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'q'
              places[spot] = 'none'
              count = 0
              return
            else:
              q.goto(locations[spot])
              turn = 'white'
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'q'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'q'
            places[spot] = 'none'
            count = 0
            return
          q.goto(locations[spot])
          turn = 'white'
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(spot[1]):
        n = columns.index(spot[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == n - m - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[spot] = 'q'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'q'
                places[spot] = 'none'
                count = 0
                return
              else:
                q.goto(locations[spot])
                turn = 'white'
                count = 0
                return
            places[var2] = 'none'
            places[spot] = 'q'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'q'
              places[spot] = 'none'
              count = 0
              return
            q.goto(locations[spot])
            turn = 'white'
            count = 0
            return
          else:
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == m - n - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[var3] = 'bi2'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'bi2'
                places[var3] = 'none'
                count = 0
                return
              else:
                bi2.goto(locations[var3])
                turn = 'white'
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var3] = 'bi2'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'bi2'
              places[var3] = 'none'
              count = 0
              return
            bi2.goto(locations[var3])
            turn = 'white'
            kill(spot)
            count = 0
            return
          else:
            count = 0
            return
      else:
        n = int(spot[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[spot[0] + str(int(spot[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[spot] = 'q'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'q'
              places[spot] = 'none'
              count = 0
              return
            else:
              q.goto(locations[spot])
              turn = 'white'
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'q'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'q'
            places[spot] = 'none'
            count = 0
            return
          q.goto(locations[spot])
          turn = 'white'
          count = 0
          return
        else:
          count = 0
          return
    else:
      var5 = False
      var6 = 0
      var4 = 0
      for i in range(1,9):
        if spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
          var5 = 'dl'
          var6 = i
        elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
          var5 = 'dr'
          var6 = i
        elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
          var5 = 'ur'
          var6 = i
        elif spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
          var5 = 'ul'
          var6 = i
      if var6 == 1:
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'q'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'q'
            places[spot] = 'none'
            count = 0
            return
          else:
            q.goto(locations[spot])
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'q'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'q'
          places[spot] = 'none'
          count = 0
          return
        q.goto(locations[spot])
        turn = 'white'
        count = 0
        return
        return
      elif var5 == 'ur':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
            var4 += 1
      elif var5 == 'ul':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
            var4 += 1
      elif var5 == 'dr':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
            var4 += 1
      elif var5 == 'dl':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
            var4 += 1
      if var4 == var6 - 1:
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[spot] = 'q'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'q'
            places[spot] = 'none'
            count = 0
            return
          else:
            q.goto(locations[spot])
            turn = 'white'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'q'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'q'
          places[spot] = 'none'
          count = 0
          return
        q.goto(locations[spot])
        turn = 'white'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    var8 = 0
    if var3[0] == var2[0] or var3[1] == var2[1]:
      if int(var2[1]) > int(var3[1]):
        n = int(var2[1]) - int(var3[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var8 += 1
        if var8 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[var3] = 'q'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'q'
              places[var3] = 'none'
              count = 0
              return
            else:
              q.goto(locations[var3])
              turn = 'white'
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var3] = 'q'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'q'
            places[var3] = 'none'
            count = 0
            return
          q.goto(locations[var3])
          turn = 'white'
          kill(spot)
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(var3[1]):
        n = columns.index(var3[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + var3[1]] == 'none':
              var8 += 1
          if var8 == n - m - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[var3] = 'q'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'q'
                places[var3] = 'none'
                count = 0
                return
              else:
                q.goto(locations[var3])
                turn = 'white'
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var3] = 'q'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'q'
              places[var3] = 'none'
              count = 0
              return
            q.goto(locations[var3])
            turn = 'white'
            kill(spot)
            count = 0
            return
          else:
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + var3[1]] == 'none':
              var8 += 1
          if var8 == m - n - 1:
            if in_check(kPos, 'black'):
              places[var2] = 'none'
              places[var3] = 'q'
              updates('white')
              if in_check(kPos, 'black'):
                places[var2] = 'q'
                places[var3] = 'none'
                count = 0
                return
              else:
                q.goto(locations[var3])
                turn = 'white'
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var3] = 'q'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'q'
              places[var3] = 'none'
              count = 0
              return
            q.goto(locations[var3])
            turn = 'white'
            kill(spot)
            count = 0
            return
          else:
            count = 0
            return
      else:
        n = int(var3[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[var3[0] + str(int(var3[1])- i - 1)] == 'none':
            var8 += 1
        if var8 == n:
          if in_check(kPos, 'black'):
            places[var2] = 'none'
            places[var3] = 'q'
            updates('white')
            if in_check(kPos, 'black'):
              places[var2] = 'q'
              places[var3] = 'none'
              count = 0
              return
            else:
              q.goto(locations[var3])
              turn = 'white'
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var3] = 'q'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'q'
            places[var3] = 'none'
            count = 0
            return
          q.goto(locations[var3])
          turn = 'white'
          kill(spot)
          count = 0
          return
        else:
          count = 0
          return
    else:
      var5 = False
      var6 = 0
      for i in range(1,9):
        if var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
          var5 = 'dl'
          var6 = i
        elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
          var5 = 'dr'
          var6 = i
        elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
          var5 = 'ur'
          var6 = i
        elif var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
          var5 = 'ul'
          var6 = i
      if var6 == 1:
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[var3] = 'q'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'q'
            places[var3] = 'none'
            count = 0
            return
          else:
            q.goto(locations[var3])
            turn = 'white'
            kill(spot)
            count = 0
            return
        places[var2] = 'none'
        places[var3] = 'q'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'q'
          places[var3] = 'none'
          count = 0
          return
        q.goto(locations[var3])
        turn = 'white'
        kill(spot)
        count = 0
        return
      elif var5 == 'ur':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
            var8 += 1
      elif var5 == 'ul':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
            var8 += 1
      elif var5 == 'dr':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
            var8 += 1
      elif var5 == 'dl':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
            var8 += 1
      if var8 == var6 - 1:
        if in_check(kPos, 'black'):
          places[var2] = 'none'
          places[var3] = 'q'
          updates('white')
          if in_check(kPos, 'black'):
            places[var2] = 'q'
            places[var3] = 'none'
            count = 0
            return
          else:
            q.goto(locations[var3])
            turn = 'white'
            kill(spot)
            count = 0
            return
        places[var2] = 'none'
        places[var3] = 'q'
        updates('white')
        if in_check(kPos, 'black'):
          places[var2] = 'q'
          places[var3] = 'none'
          count = 0
          return
        q.goto(locations[var3])
        turn = 'white'
        kill(spot)
        count = 0
        return
      else:
        count = 0
        return




def Pawn1(x,y):   
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('P1')
  r = 0
  updates('black')
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '2':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) - 1) or var2[1] == str(int(spot[1]) - 2)):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P1'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P1'
            places[spot] = 'none'
            count = 0
            return
          else:
            P1.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P1'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P1'
          places[spot] = 'none'
          count = 0
          return
        P1.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) - 1):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P1'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P1'
            places[spot] = 'none'
            count = 0
            return
          else:
            P1.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P1'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P1'
          places[spot] = 'none'
          count = 0
          return
        P1.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) \
    and str(int(var2[1]) + 1) == var3[1]:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'P1'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P1'
          places[var3] = 'none'
          count = 0
          return
        else:
          P1.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'P1'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'P1'
        places[var3] = 'none'
        count = 0
        return
      P1.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def Pawn2(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('P2')
  r = 1
  updates('black')
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '2':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) - 1) or var2[1] == str(int(spot[1]) - 2)):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P2'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P2'
            places[spot] = 'none'
            count = 0
            return
          else:
            P2.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P2'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P2'
          places[spot] = 'none'
          count = 0
          return
        P2.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) - 1):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P2'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P2'
            places[spot] = 'none'
            count = 0
            return
          else:
            P2.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P2'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P2'
          places[spot] = 'none'
          count = 0
          return
        P2.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1]) + 1) == var3[1]:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'P2'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P2'
          places[var3] = 'none'
          count = 0
          return
        else:
          P2.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'P2'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'P2'
        places[var3] = 'none'
        count = 0
        return
      P2.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def Pawn3(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('P3')
  r = 2
  updates('black')
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '2':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) - 1) or var2[1] == str(int(spot[1]) - 2)):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P3'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P3'
            places[spot] = 'none'
            count = 0
            return
          else:
            P3.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P3'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P3'
          places[spot] = 'none'
          count = 0
          return
        P3.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) - 1):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P3'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P3'
            places[spot] = 'none'
            count = 0
            return
          else:
            P3.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P3'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P3'
          places[spot] = 'none'
          count = 0
          return
        P3.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) \
    and str(int(var2[1]) + 1) == var3[1]:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'P3'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P3'
          places[var3] = 'none'
          count = 0
          return
        else:
          P3.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'P3'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'P3'
        places[var3] = 'none'
        count = 0
        return
      P3.goto(locations[var3])
      print
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def Pawn4(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('P4')
  r = 3
  updates('black')
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '2':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) - 1) or var2[1] == str(int(spot[1]) - 2)):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P4'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P4'
            places[spot] = 'none'
            count = 0
            return
          else:
            P4.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P4'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P4'
          places[spot] = 'none'
          count = 0
          return
        P4.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) - 1):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P4'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P4'
            places[spot] = 'none'
            count = 0
            return
          else:
            P4.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P4'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P4'
          places[spot] = 'none'
          count = 0
          return
        P4.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) \
    and str(int(var2[1]) + 1) == var3[1]:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'P4'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P4'
          places[var3] = 'none'
          count = 0
          return
        else:
          P4.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'P4'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'P4'
        places[var3] = 'none'
        count = 0
        return
      P4.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def Pawn5(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('P5')
  r = 4
  updates('black')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '2':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) - 1) or var2[1] == str(int(spot[1]) - 2)):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P5'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P5'
            places[spot] = 'none'
            count = 0
            return
          else:
            P5.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P5'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P5'
          places[spot] = 'none'
          count = 0
          return
        P5.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) - 1):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P5'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P5'
            places[spot] = 'none'
            count = 0
            return
          else:
            P5.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P5'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P5'
          places[spot] = 'none'
          count = 0
          return
        P5.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) \
    and str(int(var2[1]) + 1) == var3[1]:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'P5'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P5'
          places[var3] = 'none'
          count = 0
          return
        else:
          P5.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'P5'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'P5'
        places[var3] = 'none'
        count = 0
        return
      P5.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def Pawn6(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('P6')
  r = 5
  updates('black')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '2':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) - 1) or var2[1] == str(int(spot[1]) - 2)):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P6'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P6'
            places[spot] = 'none'
            count = 0
            return
          else:
            P6.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P6'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P6'
          places[spot] = 'none'
          count = 0
          return
        P6.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) - 1):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P6'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P6'
            places[spot] = 'none'
            count = 0
            return
          else:
            P6.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P6'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P6'
          places[spot] = 'none'
          count = 0
          return
        P6.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1]) + 1) == var3[1]:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'P6'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P6'
          places[var3] = 'none'
          count = 0
          return
        else:
          P6.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'P6'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'P6'
        places[var3] = 'none'
        count = 0
        return
      P6.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def Pawn7(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('P7')
  r = 6
  updates('black')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '2':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) - 1) or var2[1] == str(int(spot[1]) - 2)):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P7'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P7'
            places[spot] = 'none'
            count = 0
            return
          else:
            P7.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P7'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P7'
          places[spot] = 'none'
          count = 0
          return
        P7.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) - 1):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P7'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P7'
            places[spot] = 'none'
            count = 0
            return
          else:
            P7.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P7'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P7'
          places[spot] = 'none'
          count = 0
          return
        P7.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1]) + 1) == var3[1]:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'P7'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P7'
          places[var3] = 'none'
          count = 0
          return
        else:
          P7.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'P7'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'P7'
        places[var3] = 'none'
        count = 0
        return
      P7.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def Pawn8(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if black 2 if white 1 if none
  var2 = find('P8')
  r = 7
  updates('black')
  if var == 0 or spot == 'K':
    count = 0
    return
  elif var == 1:
    if spot[1] == '8':
      count = 0
      return
    if var2[1] == '2':
      if spot[0] == var2[0] and (var2[1] == str(int(spot[1]) - 1) or var2[1] == str(int(spot[1]) - 2)):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P8'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P8'
            places[spot] = 'none'
            count = 0
            return
          else:
            P8.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P8'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P8'
          places[spot] = 'none'
          count = 0
          return
        P8.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
    else:
      if spot[0] == var2[0] and var2[1] == str(int(spot[1]) - 1):
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'P8'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'P8'
            places[spot] = 'none'
            count = 0
            return
          else:
            P8.goto(locations[spot])
            bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'P8'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P8'
          places[spot] = 'none'
          count = 0
          return
        P8.goto(locations[spot])
        bline[r] = [columns[columns.index(spot[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(spot[0]) - 1] + str(int(spot[1]) + 1)]
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) and str(int(var2[1]) + 1) == var3[1]:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'P8'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'P8'
          places[var3] = 'none'
          count = 0
          return
        else:
          P8.goto(locations[var3])
          bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'P8'
      updates('black')
      if in_check(kPos, 'black'):
        places[var2] = 'P8'
        places[var3] = 'none'
        count = 0
        return
      P8.goto(locations[var3])
      bline[r] = [columns[columns.index(var3[0]) + 1] + str(int(spot[1]) + 1),columns[columns.index(var3[0]) - 1] + str(int(var3[1]) + 1)]
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
        count = 0
        return




def Rook1(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  global Rook1Moved
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if white 2 if black 1 if none
  var2 = find('R1')
  updates('black')
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    if spot[0] == var2[0] or spot[1] == var2[1]:
      var4 = 0
      if int(var2[1]) > int(spot[1]):
        n = int(var2[1]) - int(spot[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[spot] = 'R1'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R1'
              places[spot] = 'none'
              count = 0
              return
            else:
              R1.goto(locations[spot])
              turn = 'black'
              Rook1Moved = True
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'R1'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'R1'
            places[spot] = 'none'
            count = 0
            return
          R1.goto(locations[spot])
          turn = 'black'
          Rook1Moved = True
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(spot[1]):
        n = columns.index(spot[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == n - m - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[spot] = 'R1'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'R1'
                places[spot] = 'none'
                count = 0
                return
              else:
                R1.goto(locations[spot])
                turn = 'black'
                Rook1Moved = True
                count = 0
                return
            places[var2] = 'none'
            places[spot] = 'R1'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R1'
              places[spot] = 'none'
              count = 0
              return
            R1.goto(locations[spot])
            turn = 'black'
            Rook1Moved = True
            count = 0
            return
          else:
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == m - n - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[spot] = 'R1'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'R1'
                places[spot] = 'none'
                count = 0
                return
              else:
                R1.goto(locations[spot])
                turn = 'black'
                Rook1Moved = True
                count = 0
                return
            places[var2] = 'none'
            places[spot] = 'R1'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R1'
              places[spot] = 'none'
              count = 0
              return
            R1.goto(locations[spot])
            turn = 'black'
            Rook1Moved = True
            count = 0
            return
          else:
            count = 0
            return
      else:
        n = int(spot[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[spot[0] + str(int(spot[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[spot] = 'R1'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R1'
              places[spot] = 'none'
              count = 0
              return
            else:
              R1.goto(locations[spot])
              turn = 'black'
              Rook1Moved = True
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'R1'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'R1'
            places[spot] = 'none'
            count = 0
            return
          R1.goto(locations[spot])
          turn = 'black'
          Rook1Moved = True
          count = 0
          return
        else:
          count = 0
          return
    else:
      count = 0
      return
  elif var == 2:
    var5 = find(spot)
    if var5[0] == var2[0] or var5[1] == var2[1]:
      var4 = 0
      if int(var2[1]) > int(var5[1]):
        n = int(var2[1]) - int(var5[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[var5] = 'R1'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R1'
              places[var5] = 'none'
              count = 0
              return
            else:
              R1.goto(locations[spot])
              turn = 'black'
              Rook1Moved = True
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var5] = 'R1'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'R1'
            places[var5] = 'none'
            count = 0
            return
          R1.goto(locations[var5])
          turn = 'black'
          Rook1Moved = True
          kill(spot)
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(var5[1]):
        n = columns.index(var5[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + var5[1]] == 'none':
              var4 += 1
          if var4 == n - m - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[var5] = 'R1'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'R1'
                places[var5] = 'none'
                count = 0
                return
              else:
                R1.goto(locations[spot])
                turn = 'black'
                Rook1Moved = True
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var5] = 'R1'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R1'
              places[var5] = 'none'
              count = 0
              return
            R1.goto(locations[var5])
            turn = 'black'
            Rook1Moved = True
            kill(spot)
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + var5[1]] == 'none':
              var4 += 1
          if var4 == m - n - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[var5] = 'R1'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'R1'
                places[var5] = 'none'
                count = 0
                return
              else:
                R1.goto(locations[spot])
                turn = 'black'
                Rook1Moved = True
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var5] = 'R1'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R1'
              places[var5] = 'none'
              count = 0
              return
            R1.goto(locations[var5])
            turn = 'black'
            Rook1Moved = True
            kill(spot)
            count = 0
            return
      else:
        n = int(var5[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[var5[0] + str(int(var5[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[var5] = 'R1'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R1'
              places[var5] = 'none'
              count = 0
              return
            else:
              R1.goto(locations[spot])
              turn = 'black'
              Rook1Moved = True
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var5] = 'R1'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'R1'
            places[var5] = 'none'
            count = 0
            return
          R1.goto(locations[var5])
          turn = 'black'
          Rook1Moved = True
          kill(spot)
          count = 0
          return
    else:
      count = 0
      return




def Rook2(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  global Rook2Moved
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if white 2 if black 1 if none
  var2 = find('R2')
  updates('black')
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    if spot[0] == var2[0] or spot[1] == var2[1]:
      var4 = 0
      if int(var2[1]) > int(spot[1]):
        n = int(var2[1]) - int(spot[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[spot] = 'R2'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R2'
              places[spot] = 'none'
              count = 0
              return
            else:
              R2.goto(locations[spot])
              turn = 'black'
              Rook2Moved = True
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'R2'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'R2'
            places[spot] = 'none'
            count = 0
            return
          R2.goto(locations[spot])
          turn = 'black'
          Rook2Moved = True
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(spot[1]):
        n = columns.index(spot[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == n - m - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[spot] = 'R2'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'R2'
                places[spot] = 'none'
                count = 0
                return
              else:
                R2.goto(locations[spot])
                turn = 'black'
                Rook2Moved = True
                count = 0
                return
            places[var2] = 'none'
            places[spot] = 'R2'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R2'
              places[spot] = 'none'
              count = 0
              return
            R2.goto(locations[spot])
            turn = 'black'
            Rook2Moved = True
            count = 0
            return
          else:
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == m - n - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[spot] = 'R2'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'R2'
                places[spot] = 'none'
                count = 0
                return
              else:
                R2.goto(locations[spot])
                turn = 'black'
                Rook2Moved = True
                count = 0
                return
            places[var2] = 'none'
            places[spot] = 'R2'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R2'
              places[spot] = 'none'
              count = 0
              return
            R2.goto(locations[spot])
            turn = 'black'
            Rook2Moved = True
            count = 0
            return
          else:
            count = 0
            return
      else:
        n = int(spot[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[spot[0] + str(int(spot[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[spot] = 'R2'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R2'
              places[spot] = 'none'
              count = 0
              return
            else:
              R2.goto(locations[spot])
              turn = 'black'
              Rook2Moved = True
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'R2'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'R2'
            places[spot] = 'none'
            count = 0
            return
          R2.goto(locations[spot])
          turn = 'black'
          Rook2Moved = True
          count = 0
          return
        else:
          count = 0
          return
    else:
      count = 0
      return
  elif var == 2:
    var5 = find(spot)
    if var5[0] == var2[0] or var5[1] == var2[1]:
      var4 = 0
      if int(var2[1]) > int(var5[1]):
        n = int(var2[1]) - int(var5[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[var5] = 'R2'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R2'
              places[var5] = 'none'
              count = 0
              return
            else:
              R2.goto(locations[spot])
              turn = 'black'
              Rook2Moved = True
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var5] = 'R2'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'R2'
            places[var5] = 'none'
            count = 0
            return
          R2.goto(locations[var5])
          turn = 'black'
          Rook2Moved = True
          kill(spot)
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(var5[1]):
        n = columns.index(var5[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + var5[1]] == 'none':
              var4 += 1
          if var4 == n - m - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[var5] = 'R2'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'R2'
                places[var5] = 'none'
                count = 0
                return
              else:
                R2.goto(locations[spot])
                turn = 'black'
                Rook2Moved = True
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var5] = 'R2'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R2'
              places[var5] = 'none'
              count = 0
              return
            R2.goto(locations[var5])
            turn = 'black'
            Rook2Moved = True
            kill(spot)
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + var5[1]] == 'none':
              var4 += 1
          if var4 == m - n - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[var5] = 'R2'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'R2'
                places[var5] = 'none'
                count = 0
                return
              else:
                R2.goto(locations[spot])
                turn = 'black'
                Rook2Moved = True
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var5] = 'R2'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R2'
              places[var5] = 'none'
              count = 0
              return
            R2.goto(locations[var5])
            turn = 'black'
            Rook2Moved = True
            kill(spot)
            count = 0
            return
      else:
        n = int(var5[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[var5[0] + str(int(var5[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[var5] = 'R2'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'R2'
              places[var5] = 'none'
              count = 0
              return
            else:
              R2.goto(locations[spot])
              turn = 'black'
              Rook2Moved = True
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var5] = 'R2'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'R2'
            places[var5] = 'none'
            count = 0
            return
          R2.goto(locations[var5])
          turn = 'black'
          Rook2Moved = True
          kill(spot)
          count = 0
          return
    else:
      count = 0
      return




def Bishop1(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if white 2 if black 1 if none
  var2 = find('Bi1')
  updates('black')
  var4 = 0
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    var5 = False
    var6 = 0
    for i in range(1,9):
      if spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
        var5 = 'dl'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
        var5 = 'dr'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
        var5 = 'ur'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
        var5 = 'ul'
        var6 = i
    if var6 == 1:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[spot] = 'Bi1'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Bi1'
          places[spot] = 'none'
          count = 0
          return
        else:
          Bi1.goto(locations[spot])
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'Bi1'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'Bi1'
        places[spot] = 'none'
        count = 0
        return
      Bi1.goto(locations[spot])
      turn = 'black'
      count = 0
      return
    elif var5 == 'ur':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'ul':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'dr':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    elif var5 == 'dl':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    if var4 == var6 - 1:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[spot] = 'Bi1'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Bi1'
          places[spot] = 'none'
          count = 0
          return
        else:
          Bi1.goto(locations[spot])
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'Bi1'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'Bi1'
        places[spot] = 'none'
        count = 0
        return
      Bi1.goto(locations[spot])
      turn = 'black'
      count = 0
      return
    else:
      count = 0
      return
    
  elif var == 2:
    var3 = find(spot)
    var5 = False
    var6 = 0
    for i in range(1,9):
      if var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
        var5 = 'dl'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
        var5 = 'dr'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
        var5 = 'ur'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
        var5 = 'ul'
        var6 = i
    if var6 == 1:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'Bi1'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Bi1'
          places[var3] = 'none'
          count = 0
          return
        else:
          Bi1.goto(locations[var3])
          turn = 'black'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'Bi1'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'Bi1'
        places[var3] = 'none'
        count = 0
        return
      Bi1.goto(locations[var3])
      turn = 'black'
      kill(spot)
      count = 0
      return
    elif var5 == 'ur':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'ul':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'dr':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    elif var5 == 'dl':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    if var4 == var6 - 1:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'Bi1'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Bi1'
          places[var3] = 'none'
          count = 0
          return
        else:
          Bi1.goto(locations[var3])
          turn = 'black'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'Bi1'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'Bi1'
        places[var3] = 'none'
        count = 0
        return
      Bi1.goto(locations[var3])
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
      count = 0
      return




def Bishop2(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if white 2 if black 1 if none
  var2 = find('Bi2')
  updates('black')
  var4 = 0
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    var5 = False
    var6 = 0
    for i in range(1,9):
      if spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
        var5 = 'dl'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
        var5 = 'dr'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
        var5 = 'ur'
        var6 = i
      elif spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
        var5 = 'ul'
        var6 = i
    if var6 == 1:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[spot] = 'Bi2'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Bi2'
          places[spot] = 'none'
          count = 0
          return
        else:
          Bi2.goto(locations[spot])
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'Bi2'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'Bi2'
        places[spot] = 'none'
        count = 0
        return
      Bi2.goto(locations[spot])
      turn = 'black'
      count = 0
      return
    elif var5 == 'ur':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'ul':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'dr':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    elif var5 == 'dl':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    if var4 == var6 - 1:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[spot] = 'Bi2'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Bi2'
          places[spot] = 'none'
          count = 0
          return
        else:
          Bi2.goto(locations[spot])
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'Bi2'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'Bi2'
        places[spot] = 'none'
        count = 0
        return
      Bi2.goto(locations[spot])
      turn = 'black'
      count = 0
      return
    else:
      count = 0
      return
    
  elif var == 2:
    var3 = find(spot)
    var5 = False
    var6 = 0
    for i in range(1,9):
      if var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
        var5 = 'dl'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
        var5 = 'dr'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
        var5 = 'ur'
        var6 = i
      elif var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
        var5 = 'ul'
        var6 = i
    if var6 == 1:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'Bi2'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Bi2'
          places[var3] = 'none'
          count = 0
          return
        else:
          Bi2.goto(locations[var3])
          turn = 'black'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'Bi2'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'Bi2'
        places[var3] = 'none'
        count = 0
        return
      Bi2.goto(locations[var3])
      turn = 'black'
      kill(spot)
      count = 0
      return
    elif var5 == 'ur':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'ul':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
          var4 += 1
    elif var5 == 'dr':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    elif var5 == 'dl':
      for i in range(1, var6):
        if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
          var4 += 1
    if var4 == var6 - 1:
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'Bi2'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Bi2'
          places[var3] = 'none'
          count = 0
          return
        else:
          Bi2.goto(locations[var3])
          turn = 'black'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'Bi2'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'Bi2'
        places[var3] = 'none'
        count = 0
        return
      Bi2.goto(locations[var3])
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
      count = 0
      return




def Knight1(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if white 2 if black 1 if none
  var2 = find('N1')
  updates('black')
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    if (columns.index(var2[0]) == columns.index(spot[0]) + 1 or columns.index(var2[0]) == columns.index(spot[0]) - 1) \
    and (int(spot[1]) == int(var2[1]) + 2 or int(spot[1]) == int(var2[1]) - 2):
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[spot] = 'N1'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'N1'
          places[spot] = 'none'
          count = 0
          return
        else:
          N1.goto(locations[spot])
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'N1'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'N1'
        places[spot] = 'none'
        count = 0
        return
      N1.goto(locations[spot])
      turn = 'black'
      count = 0
      return
    elif (columns.index(var2[0]) == columns.index(spot[0]) + 2 or columns.index(var2[0]) == columns.index(spot[0]) - 2) \
    and (int(spot[1]) == int(var2[1]) + 1 or int(spot[1]) == int(var2[1]) - 1):
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[spot] = 'N1'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'N1'
          places[spot] = 'none'
          count = 0
          return
        else:
          N1.goto(locations[spot])
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'N1'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'N1'
        places[spot] = 'none'
        count = 0
        return
      N1.goto(locations[spot])
      turn = 'black'
      count = 0
      return
    else:
      count = 0
      return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) \
    and (int(var3[1]) == int(var2[1]) + 2 or int(var3[1]) == int(var2[1]) - 2):
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'N1'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'N1'
          places[var3] = 'none'
          count = 0
          return
        else:
          N1.goto(locations[var3])
          turn = 'black'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'N1'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'N1'
        places[var3] = 'none'
        count = 0
        return
      N1.goto(locations[var3])
      turn = 'black'
      kill(spot)
      count = 0
      return
    elif (columns.index(var2[0]) == columns.index(var3[0]) + 2 or columns.index(var2[0]) == columns.index(var3[0]) - 2) \
    and (int(var3[1]) == int(var2[1]) + 1 or int(var3[1]) == int(var2[1]) - 1):
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'N1'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'N1'
          places[var3] = 'none'
          count = 0
          return
        else:
          N1.goto(locations[var3])
          turn = 'black'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'N1'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'N1'
        places[var3] = 'none'
        count = 0
        return
      N1.goto(locations[var3])
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
      count = 0
      return




def Knight2(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if white 2 if black 1 if none
  var2 = find('N2')
  updates('black')
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    if (columns.index(var2[0]) == columns.index(spot[0]) + 1 or columns.index(var2[0]) == columns.index(spot[0]) - 1) \
    and (int(spot[1]) == int(var2[1]) + 2 or int(spot[1]) == int(var2[1]) - 2):
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[spot] = 'N2'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'N2'
          places[spot] = 'none'
          count = 0
          return
        else:
          N2.goto(locations[spot])
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'N2'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'N2'
        places[spot] = 'none'
        count = 0
        return
      N2.goto(locations[spot])
      turn = 'black'
      count = 0
      return
    elif (columns.index(var2[0]) == columns.index(spot[0]) + 2 or columns.index(var2[0]) == columns.index(spot[0]) - 2) \
    and (int(spot[1]) == int(var2[1]) + 1 or int(spot[1]) == int(var2[1]) - 1):
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[spot] = 'N2'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'N2'
          places[spot] = 'none'
          count = 0
          return
        else:
          N2.goto(locations[spot])
          turn = 'black'
          count = 0
          return
      places[var2] = 'none'
      places[spot] = 'N2'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'N2'
        places[spot] = 'none'
        count = 0
        return
      N2.goto(locations[spot])
      turn = 'black'
      count = 0
      return
    else:
      count = 0
      return
  elif var == 2:
    var3 = find(spot)
    if (columns.index(var2[0]) == columns.index(var3[0]) + 1 or columns.index(var2[0]) == columns.index(var3[0]) - 1) \
    and (int(var3[1]) == int(var2[1]) + 2 or int(var3[1]) == int(var2[1]) - 2):
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'N2'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'N2'
          places[var3] = 'none'
          count = 0
          return
        else:
          N2.goto(locations[var3])
          turn = 'black'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'N2'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'N2'
        places[var3] = 'none'
        count = 0
        return
      N2.goto(locations[var3])
      turn = 'black'
      kill(spot)
      count = 0
      return
    elif (columns.index(var2[0]) == columns.index(var3[0]) + 2 or columns.index(var2[0]) == columns.index(var3[0]) - 2)\
    and (int(var3[1]) == int(var2[1]) + 1 or int(var3[1]) == int(var2[1]) - 1):
      if in_check(KPos, 'white'):
        places[var2] = 'none'
        places[var3] = 'N2'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'N2'
          places[var3] = 'none'
          count = 0
          return
        else:
          N2.goto(locations[var3])
          turn = 'black'
          kill(spot)
          count = 0
          return
      places[var2] = 'none'
      places[var3] = 'N2'
      updates('black')
      if in_check(KPos, 'white'):
        places[var2] = 'N2'
        places[var3] = 'none'
        count = 0
        return
      N2.goto(locations[var3])
      turn = 'black'
      kill(spot)
      count = 0
      return
    else:
      count = 0
      return




def King(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  global KingMoved
  global Rook1Moved
  global Rook2Moved
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if white 2 if black 1 if none
  var2 = find('K')
  updates('black')
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    if spot == 'c1' and KingMoved == False and Rook1Moved == False and places['b1'] == 'none' and places['c1'] == 'none' and places['d1'] == 'none':
      if (not(any('b1' in i for i in bline) and not(any('c1' in i for i in bline))) and not(any('e1' in i for i in bline))):
        if not(in_check(var2, 'white')):
          places[var2] = 'none'
          K.goto(locations[spot])
          places[spot] = KPos
          places[locations1[R1.pos()]] = 'none'
          R1.goto(locations['d1'])
          places[locations1[R1.pos()]] = 'R1'
          turn = 'black'
          count = 0
          KingMoved = True
          Rook1Moved = True
        else: 
          count = 0
          return
      else:
        count = 0
        return
    elif spot == 'g1' and KingMoved == False and Rook2Moved == False and places['g1'] == 'none' and places['f1'] == 'none':
      if (not(any('g1' in i for i in bline) and not(any('f1' in i for i in bline)))):
        if not(in_check(var2, 'white')):
          places[var2] = 'none'
          K.goto(locations[spot])
          places[spot] = KPos
          places[locations1[R2.pos()]] = 'none'
          R2.goto(locations['f1'])
          places[locations1[R2.pos()]] = 'R2'
          turn = 'black'
          count = 0
          KingMoved = True
          Rook2Moved = True
        else: 
          count = 0
          return
      else:
        count = 0
        return
    else:
      if (int(spot[1]) == int(var2[1]) or int(spot[1]) == int(var2[1]) + 1 or int(spot[1]) == int(var2[1]) - 1)\
      and spot[0] == var2[0] or spot[0] == columns[columns.index(var2[0]) + 1] or spot[0] == columns[columns.index(var2[0]) - 1]:
        if not(in_check(spot, 'white')):
          places[var2] = 'none'
          K.goto(locations[spot])
          places[spot] = KPos
          turn = 'black'
          count = 0
          KingMoved = True
        else:
          count = 0
          return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    if (int(var3[1]) == int(var2[1]) or int(var3[1]) == int(var2[1]) + 1 or int(var3[1]) == int(var2[1]) - 1)\
    and var3[0] == var2[0] or var3[0] == columns[columns.index(var2[0]) + 1] or var3[0] == columns[columns.index(var2[0]) - 1]:
      if not(in_check(var3, 'white')):
        wline[14] = []
        places[var2] = 'none'
        K.goto(locations[var3])
        places[var3] = KPos
        turn = 'black'
        kill(spot)
        count = 0
        KingMoved = True
      else:
        count = 0
        return
    else:
      count = 0
      return




def Queen(x,y):
  '''white'''
  global places
  global locations
  global locations1
  global count
  global spot
  global turn
  global kPos
  global KPos
  if count == 1 or turn == 'black':
    return
  time.sleep(0)
  spot = 'none'
  while spot == 'none':
    count = 1
    time.sleep(0)
    scr.onscreenclick(check)
  var = wInList(spot)  # 0 if white 2 if black 1 if none
  var2 = find('Q')
  updates('black')
  if var == 0 or spot == 'k':
    count = 0
    return
  elif var == 1:
    if spot[0] == var2[0] or spot[1] == var2[1]:
      var4 = 0
      if int(var2[1]) > int(spot[1]):
        n = int(var2[1]) - int(spot[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[spot] = 'Q'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'Q'
              places[spot] = 'none'
              count = 0
              return
            else:
              Q.goto(locations[spot])
              turn = 'black'
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'Q'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'Q'
            places[spot] = 'none'
            count = 0
            return
          Q.goto(locations[spot])
          turn = 'black'
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(spot[1]):
        n = columns.index(spot[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == n - m - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[spot] = 'Q'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'Q'
                places[spot] = 'none'
                count = 0
                return
              else:
                Q.goto(locations[spot])
                turn = 'black'
                count = 0
                return
            places[var2] = 'none'
            places[spot] = 'Q'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'Q'
              places[spot] = 'none'
              count = 0
              return
            Q.goto(locations[spot])
            turn = 'black'
            count = 0
            return
          else:
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + spot[1]] == 'none':
              var4 += 1
          if var4 == m - n - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[var3] = 'bi2'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'bi2'
                places[var3] = 'none'
                count = 0
                return
              else:
                bi2.goto(locations[var3])
                turn = 'black'
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var3] = 'bi2'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'bi2'
              places[var3] = 'none'
              count = 0
              return
            bi2.goto(locations[var3])
            turn = 'black'
            kill(spot)
            count = 0
            return
          else:
            count = 0
            return
      else:
        n = int(spot[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[spot[0] + str(int(spot[1])- i - 1)] == 'none':
            var4 += 1
        if var4 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[spot] = 'Q'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'Q'
              places[spot] = 'none'
              count = 0
              return
            else:
              Q.goto(locations[spot])
              turn = 'black'
              count = 0
              return
          places[var2] = 'none'
          places[spot] = 'Q'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'Q'
            places[spot] = 'none'
            count = 0
            return
          Q.goto(locations[spot])
          turn = 'black'
          count = 0
          return
        else:
          count = 0
          return
    else:
      var5 = False
      var6 = 0
      var4 = 0
      for i in range(1,9):
        if spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
          var5 = 'dl'
          var6 = i
        elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
          var5 = 'dr'
          var6 = i
        elif spot == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
          var5 = 'ur'
          var6 = i
        elif spot == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
          var5 = 'ul'
          var6 = i
      if var6 == 1:
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'Q'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'Q'
            places[spot] = 'none'
            count = 0
            return
          else:
            Q.goto(locations[spot])
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'Q'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Q'
          places[spot] = 'none'
          count = 0
          return
        Q.goto(locations[spot])
        turn = 'black'
        count = 0
        return
        return
      elif var5 == 'ur':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
            var4 += 1
      elif var5 == 'ul':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
            var4 += 1
      elif var5 == 'dr':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
            var4 += 1
      elif var5 == 'dl':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
            var4 += 1
      if var4 == var6 - 1:
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[spot] = 'Q'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'Q'
            places[spot] = 'none'
            count = 0
            return
          else:
            Q.goto(locations[spot])
            turn = 'black'
            count = 0
            return
        places[var2] = 'none'
        places[spot] = 'Q'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Q'
          places[spot] = 'none'
          count = 0
          return
        Q.goto(locations[spot])
        turn = 'black'
        count = 0
        return
      else:
        count = 0
        return
  elif var == 2:
    var3 = find(spot)
    var8 = 0
    if var3[0] == var2[0] or var3[1] == var2[1]:
      if int(var2[1]) > int(var3[1]):
        n = int(var2[1]) - int(var3[1]) - 1
        for i in range(n):
          if places[var2[0] + str(int(var2[1])- i - 1)] == 'none':
            var8 += 1
        if var8 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[var3] = 'Q'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'Q'
              places[var3] = 'none'
              count = 0
              return
            else:
              Q.goto(locations[var3])
              turn = 'black'
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var3] = 'Q'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'Q'
            places[var3] = 'none'
            count = 0
            return
          Q.goto(locations[var3])
          turn = 'black'
          kill(spot)
          count = 0
          return
        else:
          count = 0
          return
          
      elif int(var2[1]) == int(var3[1]):
        n = columns.index(var3[0])
        m = columns.index(var2[0])
        if n > m:
          for i in range(n - m - 1):
            if places[columns[n - i - 1] + var3[1]] == 'none':
              var8 += 1
          if var8 == n - m - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[var3] = 'Q'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'Q'
                places[var3] = 'none'
                count = 0
                return
              else:
                Q.goto(locations[var3])
                turn = 'black'
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var3] = 'Q'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'Q'
              places[var3] = 'none'
              count = 0
              return
            Q.goto(locations[var3])
            turn = 'black'
            kill(spot)
            count = 0
            return
          else:
            count = 0
            return
        elif m > n:
          for i in range(m - n - 1):
            if places[columns[m - i - 1] + var3[1]] == 'none':
              var8 += 1
          if var8 == m - n - 1:
            if in_check(KPos, 'white'):
              places[var2] = 'none'
              places[var3] = 'Q'
              updates('black')
              if in_check(KPos, 'white'):
                places[var2] = 'Q'
                places[var3] = 'none'
                count = 0
                return
              else:
                Q.goto(locations[var3])
                turn = 'black'
                kill(spot)
                count = 0
                return
            places[var2] = 'none'
            places[var3] = 'Q'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'Q'
              places[var3] = 'none'
              count = 0
              return
            Q.goto(locations[var3])
            turn = 'black'
            kill(spot)
            count = 0
            return
          else:
            count = 0
            return
      else:
        n = int(var3[1]) - int(var2[1]) - 1
        for i in range(n):
          if places[var3[0] + str(int(var3[1])- i - 1)] == 'none':
            var8 += 1
        if var8 == n:
          if in_check(KPos, 'white'):
            places[var2] = 'none'
            places[var3] = 'Q'
            updates('black')
            if in_check(KPos, 'white'):
              places[var2] = 'Q'
              places[var3] = 'none'
              count = 0
              return
            else:
              Q.goto(locations[var3])
              turn = 'black'
              kill(spot)
              count = 0
              return
          places[var2] = 'none'
          places[var3] = 'Q'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'Q'
            places[var3] = 'none'
            count = 0
            return
          Q.goto(locations[var3])
          turn = 'black'
          kill(spot)
          count = 0
          return
        else:
          count = 0
          return
    else:
      var5 = False
      var6 = 0
      for i in range(1,9):
        if var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) - i)):
          var5 = 'dl'
          var6 = i
        elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) - i)):
          var5 = 'dr'
          var6 = i
        elif var3 == (columns[columns.index(var2[0]) + i]) + (str(int(var2[1]) + i)):
          var5 = 'ur'
          var6 = i
        elif var3 == (columns[columns.index(var2[0]) - i]) + (str(int(var2[1]) + i)):
          var5 = 'ul'
          var6 = i
      if var6 == 1:
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[var3] = 'Q'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'Q'
            places[var3] = 'none'
            count = 0
            return
          else:
            Q.goto(locations[var3])
            turn = 'black'
            kill(spot)
            count = 0
            return
        places[var2] = 'none'
        places[var3] = 'Q'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Q'
          places[var3] = 'none'
          count = 0
          return
        Q.goto(locations[var3])
        turn = 'black'
        kill(spot)
        count = 0
        return
      elif var5 == 'ur':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) + i))]) == 'none':
            var8 += 1
      elif var5 == 'ul':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) + i))]) == 'none':
            var8 += 1
      elif var5 == 'dr':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) + i] + (str(int(var2[1]) - i))]) == 'none':
            var8 += 1
      elif var5 == 'dl':
        for i in range(1, var6):
          if (places[columns[columns.index(var2[0]) - i] + (str(int(var2[1]) - i))]) == 'none':
            var8 += 1
      if var8 == var6 - 1:
        if in_check(KPos, 'white'):
          places[var2] = 'none'
          places[var3] = 'Q'
          updates('black')
          if in_check(KPos, 'white'):
            places[var2] = 'Q'
            places[var3] = 'none'
            count = 0
            return
          else:
            Q.goto(locations[var3])
            turn = 'black'
            kill(spot)
            count = 0
            return
        places[var2] = 'none'
        places[var3] = 'Q'
        updates('black')
        if in_check(KPos, 'white'):
          places[var2] = 'Q'
          places[var3] = 'none'
          count = 0
          return
        Q.goto(locations[var3])
        turn = 'black'
        kill(spot)
        count = 0
        return
      else:
        count = 0
        return




def updates(color):
  '''finds what each color attacks'''
  var = 'none'
  count = 1
  if color == 'white': # white covers
    if not(R1.pos() == (1000,1000)): #rook
      wline[8] = []
      temp = find('R1')
      if temp[1] != '8':
        temp1 = temp[0] + str(int(temp[1]) + 1)
        wline[8].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) + 1)
          if temp1[1] == '9':
            break
          wline[8].append(temp1)
      if temp[1] != '1':
        temp1 = temp[0] + str(int(temp[1]) - 1)
        wline[8].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) - 1)
          if temp1[1] == '0':
            break
          wline[8].append(temp1)
      if temp[0] != 'h':
        temp1 = columns[columns.index(temp[0]) + 1] + temp[1]
        wline[8].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + temp1[1]
          if temp1[0] == 'z':
            break
          wline[8].append(temp1)
      if temp[0] != 'a':
        temp1 = columns[columns.index(temp[0]) - 1] + temp[1]
        wline[8].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + temp1[1]
          if temp1[0] == 'z':
            break
          wline[8].append(temp1)

    if not(R2.pos() == (1000,1000)): #rook
      wline[9] = []
      temp = find('R2')
      if temp[1] != '8':
        temp1 = temp[0] + str(int(temp[1]) + 1)
        wline[9].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) + 1)
          if temp1[1] == '0':
            break
          wline[9].append(temp1)
      if temp[1] != '1':
        temp1 = temp[0] + str(int(temp[1]) - 1)
        wline[9].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) - 1)
          if temp1[1] == '0':
            break
          wline[9].append(temp1)
      if temp[0] != 'h':
        temp1 = columns[columns.index(temp[0]) + 1] + temp[1]
        wline[9].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + temp1[1]
          if temp1[0] == 'z':
            break
          wline[9].append(temp1)
      if temp[0] != 'a':
        temp1 = columns[columns.index(temp[0]) - 1] + temp[1]
        wline[9].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + temp1[1]
          if temp1[0] == 'z':
            break
          wline[9].append(temp1)
    if not(Bi1.pos() == (1000,1000)):
      wline[12] = []
      temp = find('Bi1')
      if temp == 'a1':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
      elif temp == 'h8':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
      elif temp[1] == '1':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
      elif temp[1] == '8':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
      elif temp[0] == 'a':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
      elif temp[0] == 'h':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
      else:
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        wline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[12].append(temp1)
    if not(Bi2.pos() == (1000,1000)):
      wline[13] = []
      temp = find('Bi2')
      if temp == 'h1':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
      elif temp == 'a8':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
      elif temp[1] == '1':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
      elif temp[1] == '8':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
      elif temp[0] == 'a':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
      elif temp[0] == 'h':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
      else:
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        wline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[13].append(temp1)
    if not(N1.pos() == (1000,1000)):
      wline[10] = []
      temp = find('N1')
      ind = columns.index(temp[0])
      templist = [columns[ind + 1] + str(int(temp[1]) + 2), columns[ind + 1] + str(int(temp[1]) - 2),
      columns[ind + 2] + str(int(temp[1]) + 1),columns[ind + 2] + str(int(temp[1]) + 1), 
      columns[ind - 1] + str(int(temp[1]) + 2), columns[ind - 1] + str(int(temp[1]) - 2),
      columns[ind - 2] + str(int(temp[1]) + 1),columns[ind - 2] + str(int(temp[1]) + 1)]
      for i in templist:
        if i in squares:
          wline[10].append(i)
    if not(N2.pos() == (1000,1000)):
      wline[11] = []
      temp = find('N2')
      ind = columns.index(temp[0])
      templist = [columns[ind + 1] + str(int(temp[1]) + 2), columns[ind + 1] + str(int(temp[1]) - 2),
      columns[ind + 2] + str(int(temp[1]) + 1),columns[ind + 2] + str(int(temp[1]) + 1), 
      columns[ind - 1] + str(int(temp[1]) + 2), columns[ind - 1] + str(int(temp[1]) - 2),
      columns[ind - 2] + str(int(temp[1]) + 1),columns[ind - 2] + str(int(temp[1]) + 1)]
      for i in templist:
        if i in squares:
          wline[11].append(i)
    if not(Q.pos() == (1000,1000)):       #QUEEN
      wline[15] = []
      temp = find('Q')
      if temp[1] != '8':
        temp1 = temp[0] + str(int(temp[1]) + 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) + 1)
          if temp1[1] == '9':
            break
          wline[15].append(temp1)
      if temp[1] != '1':
        temp1 = temp[0] + str(int(temp[1]) - 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) - 1)
          if temp1[1] == '0':
            break
          wline[15].append(temp1)
      if temp[0] != 'h':
        temp1 = columns[columns.index(temp[0]) + 1] + temp[1]
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + temp1[1]
          if temp1[0] == 'z':
            break
          wline[15].append(temp1)
      if temp[0] != 'a':
        temp1 = columns[columns.index(temp[0]) - 1] + temp[1]
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + temp1[1]
          if temp1[0] == 'z':
            break
          wline[15].append(temp1)
      if temp == 'h1':                                              #DIAGONALs
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
      elif temp == 'a8':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
      elif temp[1] == '1':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
      elif temp[1] == '8':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
      elif temp[0] == 'a':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
      elif temp[0] == 'h':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
      else:
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        wline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          wline[15].append(temp1)
    if not(K.pos() == (1000,1000)): #King
      wline[14] = []
      temp = find('K')
      ind = columns.index(temp[0])
      num = int(temp[1])
      templist = [temp[0] + str(num + 1),temp[0] + str(num - 1),columns[ind + 1] + str(num),
      columns[ind - 1] + str(num),columns[ind + 1] + str(num + 1),columns[ind + 1] + str(num - 1),
      columns[ind - 1] + str(num - 1),columns[ind - 1] + str(num + 1)]
      for i in templist:
        if i in squares:
          wline[14].append(i)

  elif color == 'black':
    if not(r1.pos() == (1000,1000)): #rook
      bline[8] = []
      temp = find('r1')
      if temp[1] != '8':
        temp1 = temp[0] + str(int(temp[1]) + 1)
        bline[8].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) + 1)
          if temp1[1] == '0':
            break
          bline[8].append(temp1)
      if temp[1] != '1':
        temp1 = temp[0] + str(int(temp[1]) - 1)
        bline[8].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) - 1)
          if temp1[1] == '0':
            break
          bline[8].append(temp1)
      if temp[0] != 'h':
        temp1 = columns[columns.index(temp[0]) + 1] + temp[1]
        bline[8].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + temp1[1]
          if temp1[0] == 'z':
            break
          bline[8].append(temp1)
      if temp[0] != 'a':
        temp1 = columns[columns.index(temp[0]) - 1] + temp[1]
        bline[8].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + temp1[1]
          if temp1[0] == 'z':
            break
          bline[8].append(temp1)
    if not(r2.pos() == (1000,1000)): #rook2
      temp = find('r2')
      if temp[1] != '8':
        temp1 = temp[0] + str(int(temp[1]) + 1)
        bline[9].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) + 1)
          if temp1[1] == '0':
            break
          bline[9].append(temp1)
      if temp[1] != '1':
        temp1 = temp[0] + str(int(temp[1]) - 1)
        bline[9].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) - 1)
          if temp1[1] == '0':
            break
          bline[9].append(temp1)
      if temp[0] != 'h':
        temp1 = columns[columns.index(temp[0]) + 1] + temp[1]
        bline[9].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + temp1[1]
          if temp1[0] == 'z':
            break
          bline[9].append(temp1)
      if temp[0] != 'a':
        temp1 = columns[columns.index(temp[0]) - 1] + temp[1]
        bline[9].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + temp1[1]
          if temp1[0] == 'z':
            break
          bline[9].append(temp1)
    if not(bi1.pos() == (1000,1000)):
      bline[12] = []
      temp = find('bi1')
      if temp == 'h1':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
      elif temp == 'a8':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
      elif temp[1] == '1':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
      elif temp[1] == '8':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
      elif temp[0] == 'a':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
      elif temp[0] == 'h':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
      else:
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        bline[12].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[12].append(temp1)
    if not(bi2.pos() == (1000,1000)):
      bline[13] = []
      temp = find('bi2')
      if temp == 'a1':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
      elif temp == 'h8':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
      elif temp[1] == '1':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
      elif temp[1] == '8':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
      elif temp[0] == 'a':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
      elif temp[0] == 'h':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
      else:
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        bline[13].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[13].append(temp1)
    if not(n1.pos() == (1000,1000)):
      bline[10] = []
      temp = find('n1')
      ind = columns.index(temp[0])
      templist = [columns[ind + 1] + str(int(temp[1]) + 2), columns[ind + 1] + str(int(temp[1]) - 2),
      columns[ind + 2] + str(int(temp[1]) + 1),columns[ind + 2] + str(int(temp[1]) + 1), 
      columns[ind - 1] + str(int(temp[1]) + 2), columns[ind - 1] + str(int(temp[1]) - 2),
      columns[ind - 2] + str(int(temp[1]) + 1),columns[ind - 2] + str(int(temp[1]) + 1)]
      for i in templist:
        if i in squares:
          bline[10].append(i)
    if not(n2.pos() == (1000,1000)):
      bline[11] = []
      temp = find('n2')
      ind = columns.index(temp[0])
      templist = [columns[ind + 1] + str(int(temp[1]) + 2), columns[ind + 1] + str(int(temp[1]) - 2),
      columns[ind + 2] + str(int(temp[1]) + 1),columns[ind + 2] + str(int(temp[1]) + 1), 
      columns[ind - 1] + str(int(temp[1]) + 2), columns[ind - 1] + str(int(temp[1]) - 2),columns[ind - 2] + str(int(temp[1]) + 1),
      columns[ind - 2] + str(int(temp[1]) + 1)]
      for i in templist:
        if i in squares:
          bline[11].append(i)
    if not(q.pos() == (1000,1000)):       #QUEEN
      bline[15] = []
      temp = find('q')
      if temp[1] != '8':
        temp1 = temp[0] + str(int(temp[1]) + 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) + 1)
          if temp1[1] == '9':
            break
          bline[15].append(temp1)
      if temp[1] != '1':
        temp1 = temp[0] + str(int(temp[1]) - 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = temp1[0] + str(int(temp1[1]) - 1)
          if temp1[1] == '0':
            break
          bline[15].append(temp1)
      if temp[0] != 'h':
        temp1 = columns[columns.index(temp[0]) + 1] + temp[1]
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + temp1[1]
          if temp1[0] == 'z':
            break
          bline[15].append(temp1)
      if temp[0] != 'a':
        temp1 = columns[columns.index(temp[0]) - 1] + temp[1]
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + temp1[1]
          if temp1[0] == 'z':
            break
          bline[15].append(temp1)
      if temp == 'h1':                                              #DIAGONALs
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
      elif temp == 'a8':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
      elif temp[1] == '1':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
      elif temp[1] == '8':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
      elif temp[0] == 'a':
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
      elif temp[0] == 'h':
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
      else:
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) - 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) + 1] + str(int(temp[1]) + 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) + 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) - 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) - 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
        temp1 = columns[columns.index(temp[0]) - 1] + str(int(temp[1]) + 1)
        bline[15].append(temp1)
        while places[temp1] == 'none':
          temp1 = columns[columns.index(temp1[0]) - 1] + str(int(temp1[1]) + 1)
          if temp1[1] == '0' or temp1[1] == '9' or temp1[0] == 'z':
            break
          bline[15].append(temp1)
    if not(k.pos() == (1000,1000)): #king
      bline[14] = []
      temp = find('k')
      ind = columns.index(temp[0])
      num = int(temp[1])
      templist = [temp[0] + str(num + 1),temp[0] + str(num - 1),
      columns[ind + 1] + str(num),columns[ind - 1] + str(num),
      columns[ind + 1] + str(num + 1),columns[ind + 1] + str(num - 1),
      columns[ind - 1] + str(num - 1),columns[ind - 1] + str(num + 1)]
      for i in templist:
        if i in squares:
          bline[14].append(i)



def in_check(pos, color):
  '''checks if the king is in check'''
  if color == 'white':
    for i in bline:
      for l in i:
        if pos == l:
          return True
  elif color == 'black':
    for p in wline:
      for k in p:
        if pos == k:
          return True
  else:
    return
  return False






  

def kill(turtle):
  '''when piece is killed'''
  if turtle == 'P1':
    wline[0] = []
    P1.goto(1000,1000)
  elif turtle == 'P2':
    wline[1] = []
    P2.goto(1000,1000)
  elif turtle == 'P3':
    wline[2] = []
    P3.goto(1000,1000)
  elif turtle == 'P4':
    wline[3] = []
    P4.goto(1000,1000)
  elif turtle == 'P5':
    wline[4] = []
    P5.goto(1000,1000)
  elif turtle == 'P6':
    wline[5] = []
    P6.goto(1000,1000)
  elif turtle == 'P7':
    wline[6] = []
    P7.goto(1000,1000)
  elif turtle == 'P8':
    wline[7] = []
    P8.goto(1000,1000)
  elif turtle == 'R1':
    wline[8] = []
    R1.goto(1000,1000)
  elif turtle == 'R2':
    wline[9] = []
    R2.goto(1000,1000)
  elif turtle == 'Bi1':
    wline[12] = []
    Bi1.goto(1000,1000)
  elif turtle == 'Bi2':
    wline[13] = []
    Bi2.goto(1000,1000)
  elif turtle == 'N1':
    wline[10] = []
    N1.goto(1000,1000)
  elif turtle == 'N2':
    wline[11] = []
    N2.goto(1000,1000)
  elif turtle == 'Q':
    wline[15] = []
    Q.goto(1000,1000)
  elif turtle == 'p1':
    bline[0] = []
    p1.goto(1000,1000)
  elif turtle == 'p2':
    bline[1] = []
    p2.goto(1000,1000)
  elif turtle == 'p3':
    bline[2] = []
    p3.goto(1000,1000)
  elif turtle == 'p4':
    bline[3] = []
    p4.goto(1000,1000)
  elif turtle == 'p5':
    bline[4] = []
    p5.goto(1000,1000)
  elif turtle == 'p6':
    bline[5] = []
    p6.goto(1000,1000)
  elif turtle == 'p7':
    bline[6] = []
    p7.goto(1000,1000)
  elif turtle == 'p8':
    bline[7] = []
    p8.goto(1000,1000)
  elif turtle == 'r1':
    bline[8] = []
    r1.goto(1000,1000)
  elif turtle == 'r2':
    bline[9] = []
    r2.goto(1000,1000)
  elif turtle == 'n1':
    bline[10] = []
    n1.goto(1000,1000)
  elif turtle == 'n2':
    bline[11] = []
    n2.goto(1000,1000)
  elif turtle == 'bi1':
    bline[12] = []
    bi1.goto(1000,1000)
  elif turtle == 'bi2':
    bline[13] = []
    bi2.goto(1000,1000)
  elif turtle == 'q':
    bline[15] = []
    q.goto(1000,1000)


#lists

rows = [0,0,0,0,1,2,3,4,5,6,7,8,0,0,0,0,0,0]

columns = [ 'z', 'z', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']

FONT = ('Times New Roman', 15, 'Normal')

wPieces = ['P1','P2','P3','P4','P5','P6','P7','P8','R1','R2','Bi1','Bi2','Q','K', 'N1', 'N2']

bPieces = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'r1', 'r2', 'bi1', 'bi2', 'q', 'k', 'n1', 'n2']

squares = ['a1','a2','a3','a4','a5','a6','a7','a8','b1','b2','b3','b4','b5','b6','b7','b8','c1','c2','c3','c4','c5','c6','c7','c8','d1',
'd2','d3','d4','d5','d6','d7','d8','e1','e2','e3','e4','e5','e6','e7','e8','f1','f2','f3','f4','f5','f6','f7','f8','g1','g2',
'g3','g4','g5','g6','g7','g8','h1','h2','h3','h4','h5','h6','h7','h8']

count = 0

turn = 'white'

pinned = []

#for castling
kingMoved = False
KingMoved = False
Rook1Moved = False
Rook2Moved = False
rook1Moved = False
rook2Moved = False

#2d list for each piece attacking
bline = [   # piece       #Index
 ['b6'],  #p1         0
 ['a6', 'c6'],  #p2         1
 ['b6', 'd6'],  #p3         2
 ['c6', 'e6'],  #p4         3
 ['d6', 'f6'],  #p5         4
 ['e6', 'g6'],  #p6         5
 ['f6', 'h6'],  #p7         6
 ['g6'],  #p8         7
 ['a7', 'b8'],  #r1         8
 ['h7', 'g8'],  #r2         9
 ['a6', 'c6'],  #n1         10
 ['f6', 'h6'],  #n2         11
 ['b7', 'd7'],  #b1         12
 ['e7', 'g7'],  #b2         13
 ['c7', 'd7', 'e7', 'c8', 'e8'],  #k          14
 ['d7', 'e7', 'f7', 'd8', 'f8'],  #q          15
]


wline = [
['b3'], #P1           0
['a3', 'c3'], #P2           1
['b3','d3'], #P3           2
['c3','e3'], #P4           3
['d3','f3'], #P5           4
['e3','g3'], #P6           5
['f3','h3'], #P7           6
['g3'], #P8           7
['a2', 'b1'], #R1           8
['g1', 'h2'], #R2           9
['a3','c3'], #N1           10
['f3','h3'], #N2           11
['b2', 'd2'], #B1           12
['e2', 'g2'], #B2           13
['c2', 'd2', 'e2', 'c1', 'e1'], #K           14
['d2', 'e2', 'f2', 'd1', 'f1'], #Q           15
]








#where each square
locations = {
'a1' : (-350,-350),
'a2' : (-350,-250),
'a3' : (-350,-150),
'a4' : (-350,-50),
'a5' : (-350,50),
'a6' : (-350,150),
'a7' : (-350,250),
'a8' : (-350,350),
'b1' : (-250,-350),
'b2' : (-250,-250),
'b3' : (-250,-150),
'b4' : (-250,-50),
'b5' : (-250,50),
'b6' : (-250,150),
'b7' : (-250,250),
'b8' : (-250,350),
'c1' : (-150,-350),
'c2' : (-150,-250),
'c3' : (-150,-150),
'c4' : (-150,-50),
'c5' : (-150,50),
'c6' : (-150,150),
'c7' : (-150,250),
'c8' : (-150,350),
'd1' : (-50,-350),
'd2' : (-50,-250),
'd3' : (-50,-150),
'd4' : (-50,-50),
'd5' : (-50,50),
'd6' : (-50,150),
'd7' : (-50,250),
'd8' : (-50,350),
'e1' : (50,-350),
'e2' : (50,-250),
'e3' : (50,-150),
'e4' : (50,-50),
'e5' : (50,50),
'e6' : (50,150),
'e7' : (50,250),
'e8' : (50,350),
'f1' : (150,-350),
'f2' : (150,-250),
'f3' : (150,-150),
'f4' : (150,-50),
'f5' : (150,50),
'f6' : (150,150),
'f7' : (150,250),
'f8' : (150,350),
'g1' : (250,-350),
'g2' : (250,-250),
'g3' : (250,-150),
'g4' : (250,-50),
'g5' : (250,50),
'g6' : (250,150),
'g7' : (250,250),
'g8' : (250,350),
'h1' : (350,-350),
'h2' : (350,-250),
'h3' : (350,-150),
'h4' : (350,-50),
'h5' : (350,50),
'h6' : (350,150),
'h7' : (350,250),
'h8' : (350,350)
}

locations1 = {
(-350,-350) : 'a1',  
(-350,-250) : 'a2',  
(-350,-150) : 'a3',  
(-350,-50) : 'a4',  
(-350,50) : 'a5',  
(-350,150) : 'a6',  
(-350,250) : 'a7',  
(-350,350) : 'a8',  
(-250,-350) : 'b1',  
(-250,-250) : 'b2',  
(-250,-150) : 'b3',  
(-250,-50) : 'b4',  
(-250,50) : 'b5',  
(-250,150) : 'b6',  
(-250,250) : 'b7',  
(-250,350) : 'b8',  
(-150,-350) : 'c1',  
(-150,-250) : 'c2',  
(-150,-150) : 'c3',  
(-150,-50) : 'c4',  
(-150,50) : 'c5',  
(-150,150) : 'c6',  
(-150,250) : 'c7',  
(-150,350) : 'c8',  
(-50,-350) : 'd1',  
(-50,-250) : 'd2',  
(-50,-150) : 'd3',  
(-50,-50) : 'd4',  
(-50,50) : 'd5',  
(-50,150) : 'd6',  
(-50,250) : 'd7',  
(-50,350) : 'd8',  
(50,-350) : 'e1',  
(50,-250) : 'e2',  
(50,-150) : 'e3',  
(50,-50) : 'e4',  
(50,50) : 'e5',  
(50,150) : 'e6',  
(50,250) : 'e7',  
(50,350) : 'e8',  
(150,-350) : 'f1',  
(150,-250) : 'f2',  
(150,-150) : 'f3',  
(150,-50) : 'f4',  
(150,50) : 'f5',  
(150,150) : 'f6',  
(150,250) : 'f7',  
(150,350) : 'f8',  
(250,-350) : 'g1',  
(250,-250) : 'g2',  
(250,-150) : 'g3',  
(250,-50) : 'g4',  
(250,50) : 'g5',  
(250,150) : 'g6',  
(250,250) : 'g7',  
(250,350) : 'g8',  
(350,-350) : 'h1',  
(350,-250) : 'h2',  
(350,-150) : 'h3',  
(350,-50) : 'h4',  
(350,50) : 'h5',  
(350,150) : 'h6',  
(350,250) : 'h7',  
(350,350) : 'h8'
}


'''what piece is where'''
places = {
'a1' : 'R1',
'a2' : 'P1',
'a3' : 'none',
'a4' : 'none',
'a5' : 'none',
'a6' : 'none',
'a7' : 'p1',
'a8' : 'r1',
'b1' : 'N1',
'b2' : 'P2',
'b3' : 'none',
'b4' : 'none',
'b5' : 'none',
'b6' : 'none',
'b7' : 'p2',
'b8' : 'n1',
'c1' : 'Bi1',
'c2' : 'P3',
'c3' : 'none',
'c4' : 'none',
'c5' : 'none',
'c6' : 'none',
'c7' : 'p3',
'c8' : 'bi1',
'd1' : 'Q',
'd2' : 'P4',
'd3' : 'none',
'd4' : 'none',
'd5' : 'none',
'd6' : 'none',
'd7' : 'p4',
'd8' : 'q',
'e1' : 'K',
'e2' : 'P5',
'e3' : 'none',
'e4' : 'none',
'e5' : 'none',
'e6' : 'none',
'e7' : 'p5',
'e8' : 'k',
'f1' : 'Bi2',
'f2' : 'P6',
'f3' : 'none',
'f4' : 'none',
'f5' : 'none',
'f6' : 'none',
'f7' : 'p6',
'f8' : 'bi2',
'g1' : 'N2',
'g2' : 'P7',
'g3' : 'none',
'g4' : 'none',
'g5' : 'none',
'g6' : 'none',
'g7' : 'p7',
'g8' : 'n2',
'h1' : 'R2',
'h2' : 'P8',
'h3' : 'none',
'h4' : 'none',
'h5' : 'none',
'h6' : 'none',
'h7' : 'p8',
'h8' : 'r2'

}








  



#setting up each onclick
P1.onclick(Pawn1)
P2.onclick(Pawn2)
P3.onclick(Pawn3)
P4.onclick(Pawn4)
P5.onclick(Pawn5)
P6.onclick(Pawn6)
P7.onclick(Pawn7)
P8.onclick(Pawn8)
R1.onclick(Rook1)
R2.onclick(Rook2)
N1.onclick(Knight1)
N2.onclick(Knight2)
Bi1.onclick(Bishop1)
Bi2.onclick(Bishop2)
K.onclick(King)
Q.onclick(Queen)
p1.onclick(pawn1)
p2.onclick(pawn2)
p3.onclick(pawn3)
p4.onclick(pawn4)
p5.onclick(pawn5)
p6.onclick(pawn6)
p7.onclick(pawn7)
p8.onclick(pawn8)
r1.onclick(rook1)
r2.onclick(rook2)
n1.onclick(knight1)
n2.onclick(knight2)
bi1.onclick(bishop1)
bi2.onclick(bishop2)
k.onclick(king)
q.onclick(queen)


#board colors
while True:
  custom = input('Would you like custom colors? type y or n').lower()
  if custom == 'y':
    background = input('Please enter the background color')
    scr.bgcolor(background)
    dark = input('Please enter the dark color')
    light = input('Please enter the light color')
    makeBoard(light, dark)
    system('cls')
    break
  elif custom == 'n':
    background = 64, 121, 140
    dark = 139, 184, 167
    light = 207, 224, 195
    scr.bgcolor(background)
    makeBoard(light, dark)
    system('cls')
    break

setPiecesWhite()
setShapes()

spot = 'none'



#finishes board/slows turtles
scr.tracer(1)
scr.update()

time.sleep(1)


updates('white')
updates('black')

#keeps looping to find king positions, sleeps 2 secs because of lag
while True:
  kPos = find('k')
  KPos = find('K')
  time.sleep(2)
  
  