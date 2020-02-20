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
ev3.speaker.set_volume(60)
motor1 = Motor(Port.A)

frequency = [440, 294, 15000, 294,587,523,440,440,392,440,440,294,15000,294,587,523, 440,440,392,440, 294, 15000, 294,587,523, 440, 440, 440, 440, 440, 440, 440, 392, 392, 392, 349,349,349, 329,294,15000 ]
durations = [500,500, 200,500,500,1000,250,250,250,250,500,1500,200, 500,500,1000, 250,250,250,250, 250, 1000, 500,500,1000, 250, 250,  250, 250, 250,  250, 250, 250, 250, 500, 250,250, 250,500,250,250] 


# frequency = [440,440,392,440]
# durations = [500,500,250,250]
s=serial.Serial("/dev/ttyACM0",9600)
while True:

     for i in range(len(frequency)):
          
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
          for t in range(len(imu)):
               imu[t] = float(imu[t])
          magnitudeA = math.sqrt((imu[0])**2 + (imu[1])**2 + (imu[2])**2 )
          magnitudeB = math.sqrt((imu[3])**2 + (imu[4])**2 + (imu[5])**2 )-9
          print(magnitudeB)
          
          #print(i)
          #print(frequency[i])
          scaler = 1.5 - magnitudeB/750
          mscale = 1 + ((magnitudeB)**2)/300
          slow=50
          fast=240
          ev3.speaker.beep(frequency[i],scaler*durations[i])
          motor1.run(220*mscale)
          #ev3.speaker.beep(frequency[i],(durations[i]))
          



#notes = ['G3/8','G3/8', 'G3/8', 'Eb3/2','R/8','F3/8','F3/8', 'F3/8', 'D3/2']
#ev3.speaker.play_notes(notes, tempo=120)


#Receive input from arduino through serial


#returns position vector given an acceleration vector and initial conditions
#def position(AccVector,timeVector,initx,initv):
  # for i in range(AccVector):







