# -*- coding: utf-8 -*-
import time
import serial

from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
from modules.core.props import Property

from modules.core.step import StepBase

@cbpi.actor
class SerActor2(ActorBase):
    t0=Property.Text("Serial", configurable=True)    
    t1=Property.Text("Texto Serial", configurable=True)    
    #state= Property.Number("Memoria", configurable=False)

    def stateV(self):
      return self.state
    def on(self, power=100):
      '''
      Code to switch on the actor
      :param power: int value between 0 - 100
      :return: 
      '''
      ser = open (self.t0, 'w')
      ser.write(self.t1)
      ser.write(';100 \n')
      print "ON"
      ser.close()
    def off(self):
     '''
     '''
     ser = open (self.t0, 'w')
     ser.write(self.t1)
     ser.write(';0 \n')
     print "OFF"
     ser.close()
@cbpi.actor
class SerActorPWM2(ActorBase):
    t0=Property.Text("Serial", configurable=True)    
    t1=Property.Text("Texto Serial", configurable=True)   
    #state= Property.Number("", configurable=False)

    power = 100
    def stateV(self):
        return self.state

    def on(self, power=None):
        if power is not None:
            self.power = int(power)
        ser = open (self.t0, 'w')
        ser.write('%s;%s \n' % (self.t1, self.power))
        #ser.write(str(self.power))
        #ser.write('\n')
        ser.close()
    def set_power(self, power):
        '''
        Optional: Set the power of your actor
        :param power: int value between 0 - 100
        :return:
        '''
        if power is not None:
            self.power = int(power)
        if (self.state>0):
           ser = open (self.t0, 'w')
           ser.write('%s;%s \n' % (self.t1, self.power))
           self.on()
           ser.close()
    def off(self):
        print "GPIO OFF"
        ser = open (self.t0, 'w')
        #ser.write(self.t1)
        #ser.write('0')
        ser.write('%s;0 \n' % (self.t1))
        ser.close()
