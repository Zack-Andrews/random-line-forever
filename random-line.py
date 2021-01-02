#the most random script i could come up with 

 

#imports 

import random

import turtle 

 

#script 

 

wn = turtle.Screen() 

alexa = turtle.Turtle() 

turtle.bgcolor('black') 

alexa.color('green') 

alexa.hideturtle() 

alexa.speed(1) 

random = random.randint(50,500) 

alexa.forward(random) 

alexa.right(random) 

alexa.forward(random) 

alexa.right(random) 

alexa.forward(random) 

alexa.right(random) 

alexa.forward(random) 

 

#qeustion 

 

awnser = input('are u now randomizedY/N') 
 

if awnser=='y': 

  print('coolbeans') 

else: 

  alexa.forward(random) 

  alexa.right(random) 

  alexa.forward(random) 

  alexa.right(random) 

  alexa.forward(random) 

  alexa.right(random) 

  alexa.forward(random) 

 

awnser = input('are u now randomizedY/N') 

 

if awnser=='y': 

  print('coolbeans') 

else: 

  print('you are not randomizeble') 

 

 

#end 