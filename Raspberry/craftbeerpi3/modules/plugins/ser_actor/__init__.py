# -*- coding: utf-8 -*-
import time
import serial

from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
from modules.core.props import Property

from modules.core.step import StepBase

@cbpi.actor
class SerActor(ActorBase):
    
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
	
	ser = open ('/dev/ttyUSB0', 'w')
        ser.write(self.t1)
	ser.write(';100 \n')
        print "ON"
	ser.close()
    	#self.state=1
    def off(self):
	'''
	ser = serial.Serial(

               port='/dev/ttyUSB0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )
	'''
	ser = open ('/dev/ttyUSB0', 'w')
	ser.write(self.t1)
	ser.write(';0 \n')
        print "OFF"
	ser.close()
    	#self.state=0

@cbpi.actor
class SerActorPWM(ActorBase):

    t1=Property.Text("Texto Serial", configurable=True)   
    #state= Property.Number("", configurable=False)

    power = 100
    def stateV(self):
	return self.state

    def on(self, power=None):
        if power is not None:
            self.power = int(power)
	ser = open ('/dev/ttyUSB0', 'w')
        ser.write('%s;%s \n' % (self.t1, self.power))
        #ser.write(str(self.power))
        #ser.write('\n')
	ser.close()
    	#self.state=1
    def set_power(self, power):
        '''
        Optional: Set the power of your actor
        :param power: int value between 0 - 100
        :return:
        '''
        if power is not None:
            self.power = int(power)
        ser = open ('/dev/ttyUSB0', 'w')
        #ser.write(self.t1)
        #ser.write(str(self.power))
	#ser.write('\n')
	#ser.write('%s;%s \n' % (self.t1, self.power))
	ser.close()
    def off(self):
        print "GPIO OFF"
        ser = open ('/dev/ttyUSB0', 'w')
        #ser.write(self.t1)
        #ser.write('0')
	#ser.write('\n')
	ser.write('%s;0 \n' % (self.t1))
	ser.close()
    	#self.state=0
