#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import math
import serial

# Write your program here
ev3 = EV3Brick()
ev3.speaker.beep()


s=serial.Serial("/dev/ttyACM0",9600)
while True:
     # data=s.read(s.inWaiting()).decode("utf-8")
     try:
          data=s.read(1024).decode("utf-8")
     except:
          print("Broken read")
          continue
     #print('size = %d, buffer = %d' % (len(data),s.inWaiting()))
     #print(data)
     data = data.splitlines()
     imu = data[-2].split(',')
     #print(imu)
     for i in range(len(imu)):
          imu[i] = float(imu[i])
     magnitudeA = math.sqrt((imu[0])**2 + (imu[1])**2 + (imu[2])**2 )
     magnitudeB = math.sqrt((imu[3])**2 + (imu[4])**2 + (imu[5])**2 )
     print(magnitudeB)

     slow=50
     fast=240
     notes = ['G3/8','G3/8', 'G3/8', 'Eb3/2','R/8','F3/8','F3/8', 'F3/8', 'D3/2']
     for i in range(len(notes)):
          wait(1000)
          print(notes[i])
          # if magnitudeB <200:
          #      ev3.speaker.play_notes(notes[i], tempo=slow)
          # else:
          #      ev3.speaker.play_notes(notes[i], tempo=fast)



#notes = ['G3/8','G3/8', 'G3/8', 'Eb3/2','R/8','F3/8','F3/8', 'F3/8', 'D3/2']
#ev3.speaker.play_notes(notes, tempo=120)


#Receive input from arduino through serial


#returns position vector given an acceleration vector and initial conditions
#def position(AccVector,timeVector,initx,initv):
  # for i in range(AccVector):







