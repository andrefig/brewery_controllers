# -*- coding: utf-8 -*-
import time
#import serial

#from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
from modules.core.props import Property

from modules.core.step import StepBase


#import time
from flask_classy import route
from modules import DBModel, cbpi
from modules.core.baseview import BaseView



@cbpi.actor
class CombActor(ActorBase,StepBase):

    act0=Property.Actor("Actor 0")
    act1=Property.Actor("Actor 1")
    act2=Property.Actor("Actor 2")
    act3=Property.Actor("Actor 3")
    act4=Property.Actor("Actor 4")
    act5=Property.Actor("Actor 5")
    act6=Property.Actor("Actor 6")
    act7=Property.Actor("Actor 7")
    act8=Property.Actor("Actor 8")

    #gpio = Property.Select("GPIO", options=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27], description="GPIO to which the actor is connected")

    state1= Property.Number("State Actor 1 - ON", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state2= Property.Number("State Actor 2 - ON", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state3= Property.Number("State Actor 3 - ON", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state4= Property.Number("State Actor 4 - ON", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state5= Property.Number("State Actor 5 - ON", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state6= Property.Number("State Actor 6 - ON", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state7= Property.Number("State Actor 7 - ON", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state8= Property.Number("State Actor 8 - ON", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)

    Ostate1= Property.Number("State Actor 1 - OFF", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    Ostate2= Property.Number("State Actor 2 - OFF", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    Ostate3= Property.Number("State Actor 3 - OFF", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    Ostate4= Property.Number("State Actor 4 - OFF", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    Ostate5= Property.Number("State Actor 5 - OFF", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    Ostate6= Property.Number("State Actor 6 - OFF", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    Ostate7= Property.Number("State Actor 7 - OFF", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    Ostate8= Property.Number("State Actor 8 - OFF", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)

    Pstate1 = Property.Number("M0", configurable=False)
    Pstate2 = Property.Number("M1", configurable=False)
    Pstate3 = Property.Number("M2", configurable=False)
    Pstate4 = Property.Number("M3", configurable=False)
    Pstate5 = Property.Number("M4", configurable=False)
    Pstate6 = Property.Number("M5", configurable=False)
    Pstate7 = Property.Number("M6", configurable=False)
    Pstate8 = Property.Number("M7", configurable=False)

    power = 100
    #def exib_on(self,power=None):
    #    return None
    def on(self, power=None, so_exibe=False):
       try:
    #    self.Pstate1=self.act1.stateV()
    #    self.Pstate2=self.act2.stateV()
	#self.Pstate3=self.act3.stateV()
	#self.Pstate4=self.act4.stateV()
	#self.Pstate5=self.act5.stateV()
	#self.Pstate6=self.act6.stateV()
	#self.Pstate7=self.act7.stateV()
	#self.Pstate8=self.act8.stateV()
        if so_exibe == True:
            return
        if power is not None:
            self.power = int(power)
        #print(self.act0)
        #print(int(self.act0))
        if self.act0 !='':
            self.actor_on(int(self.act0),int(self.power))

        if float(self.state1)==0:            
            self.Pstate1 = self.actor_off(int(self.act1))
        elif float(self.state1)==1:
            self.Pstate1 = self.actor_on(int(self.act1))

        #print(float(self.Pstate1))

        if float(self.state2)==0:            
            self.Pstate2 = self.actor_off(int(self.act2))
        elif float(self.state2)==1:
            self.Pstate2 = self.actor_on(int(self.act2))

        if float(self.state3)==0:            
            self.Pstate3 = self.actor_off(int(self.act3))
        elif float(self.state3)==1:
            self.Pstate3 = self.actor_on(int(self.act3))

        if float(self.state4)==0:            
            self.Pstate4 = self.actor_off(int(self.act4))
        elif float(self.state4)==1:
            self.Pstate4 = self.actor_on(int(self.act4))

        if float(self.state5)==0:            
            self.Pstate5 = self.actor_off(int(self.act5))
        elif float(self.state5)==1:
            self.Pstate5 = self.actor_on(int(self.act5))

        if float(self.state6)==0:            
            self.Pstate6 = self.actor_off(int(self.act6))
        elif float(self.state6)==1:
            self.Pstate6 = self.actor_on(int(self.act6))

        if float(self.state7)==0:            
            self.Pstate7 = self.actor_off(int(self.act7))
        elif float(self.state7)==1:
            self.Pstate7 = self.actor_on(int(self.act7))

        if float(self.state8)==0:            
            self.Pstate8 = self.actor_off(int(self.act8))
        elif float(self.state8)==1:
            self.Pstate8 = self.actor_on(int(self.act8))
       except Exception as e:
            return



    def set_power(self, power):
        '''
        Optional: Set the power of your actor
        :param power: int value between 0 - 100
        :return:
        '''

        if self.act0  !='':
            if power is not None:
                self.power = int(power)
            self.actor_power(int(self.act0), self.power)


    def off(self,so_exibe=False):
       try:
        if so_exibe == True:
            return

        if self.act0  !='':
            self.actor_off(int(self.act0))
        
        if float(self.Ostate1)==0:            
            self.actor_off(int(self.act1))
        elif float(self.Ostate1)==1:
            self.actor_on(int(self.act1))
        elif float(self.Ostate1)==2:
	       if float(self.Pstate1)==1:
                 self.actor_on(int(self.act1))
                 #print("!")
	       else:
                self.actor_off(int(self.act1))
                #print("@")


        if float(self.Ostate2)==0:            
            self.actor_off(int(self.act2))
        elif float(self.Ostate2)==1:
            self.actor_on(int(self.act2))
        elif float(self.Ostate2)==2:
          if float(self.Pstate2)==1:
            self.actor_on(int(self.act2))
          else:
            self.actor_off(int(self.act2))


        if float(self.Ostate3)==0:            
            self.actor_off(int(self.act3))
        elif float(self.Ostate3)==1:
            self.actor_on(int(self.act3))
        elif float(self.Ostate3)==2:
          if float(self.Pstate3)==1:
            self.actor_on(int(self.act3))
          else:
            self.actor_off(int(self.act3))


        if float(self.Ostate4)==0:            
            self.actor_off(int(self.act4))
        elif float(self.Ostate4)==1:
            self.actor_on(int(self.act4))
        elif float(self.Ostate1)==2:
          if float(self.Pstate4)==1:
            self.actor_on(int(self.act4))
          else:
            self.actor_off(int(self.act4))


        if float(self.Ostate5)==0:            
            self.actor_off(int(self.act5))
        elif float(self.Ostate5)==1:
            self.actor_on(int(self.act5))
        elif float(self.Ostate1)==2:
          if float(self.Pstate5)==1:
            self.actor_on(int(self.act5))
          else:
            self.actor_off(int(self.act5))


        if float(self.Ostate6)==0:            
            self.actor_off(int(self.act6))
        elif float(self.Ostate6)==1:
            self.actor_on(int(self.act6))
        elif float(self.Ostate1)==2:
          if float(self.Pstate6)==1:
            self.actor_on(int(self.act6))
          else:
            self.actor_off(int(self.act6))


        if float(self.Ostate7)==0:            
            self.actor_off(int(self.act7))
        elif float(self.Ostate7)==1:
            self.actor_on(int(self.act7))
        elif float(self.Ostate7)==2:
          if float(self.Pstate7)==1:
            self.actor_on(int(self.act7))
          else:
            self.actor_off(int(self.act7))

        if float(self.Ostate8)==0:            
            self.actor_off(int(self.act8))
        elif float(self.Ostate8)==1:
            self.actor_on(int(self.act8))
        elif float(self.Ostate1)==2:
          if float(self.Pstate8)==1:
            self.actor_on(int(self.act8))
          else:
            self.actor_off(int(self.act8))
       except Exception as e:
           return


    def verif_status(self):
        status=1
        try:

            
            if self.act0  !='':
                #print("@")
                #print((self.state1))
                #print((self.actor_read_status(int(self.act1))))
                if 1!=int(self.actor_read_status(int(self.act0))):    
                     #print("#")        
                     status=0#self.Pstate1 = self.actor_off(int(self.act1))


            if self.act1  !='':
                #print("@")
                #print((self.state1))
                #print((self.actor_read_status(int(self.act1))))
                if int(self.state1)!=int(self.actor_read_status(int(self.act1))):    
                     #print("#")        
                     status=0#self.Pstate1 = self.actor_off(int(self.act1))
            if self.act2  !='':
                if int(self.state2)!=int(self.actor_read_status(int(self.act2))):            
                     status=0#self.Pstate1 = self.actor_off(int(self.act1))
            if self.act3  !='':
                if int(self.state3)!=int(self.actor_read_status(int(self.act3))):            
                     status=0#self.Pstate1 = self.actor_off(int(self.act1))                   
            if self.act4  !='':
                if int(self.state4)!=int(self.actor_read_status(int(self.act4))):            
                     status=0#self.Pstate1 = self.actor_off(int(self.act1))
            if self.act5  !='':
                if int(self.state5)!=int(self.actor_read_status(int(self.act5))):            
                     status=0#self.Pstate1 = self.actor_off(int(self.act1))
            if self.act6  !='':
                if int(self.state6)!=int(self.actor_read_status(int(self.act6))):            
                     status=0#self.Pstate1 = self.actor_off(int(self.act1))
            if self.act7  !='':
                if int(self.state7)!=int(self.actor_read_status(int(self.act7))):            
                     status=0#self.Pstate1 = self.actor_off(int(self.act1))
            if self.act8  !='':
                if int(self.state8)!=int(self.actor_read_status(int(self.act8))):            
                     status=0#self.Pstate1 = self.actor_off(int(self.act1))
            #print ("STATUS=")
            #print(status)
            return status
        except Exception as e:
            #print ("STATUS*=")
            #print(status)
            return status      




@cbpi.actor
class IndirectActor(ActorBase,StepBase):

    act0=Property.Actor("Actor 0")


    #gpio = Property.Select("GPIO", options=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27], description="GPIO to which the actor is connected")

    state0= Property.Number("State Actor 0 - ON", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)

    Ostate0= Property.Number("State Actor 0 - OFF", configurable=True, default_value=3,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)

    Pstate0 = Property.Number("M0", configurable=False)


    power = 100
    #def exib_on(self,power=None):
    #    return None
    def on(self, power=None, so_exibe=False):
       try:
        if so_exibe == True:
            return
        if power is not None:
            self.power = int(power)

        if float(self.state0)==0:            
            self.Pstate0 = self.actor_off(int(self.act0))
        elif float(self.state0)==1:
            self.Pstate0 = self.actor_on(int(self.act0))
       except Exception as e:
           return

    def set_power(self, power):
        '''
        Optional: Set the power of your actor
        :param power: int value between 0 - 100
        :return:
        '''

        if self.act0  !='':
            if power is not None:
                self.power = int(power)
            self.actor_power(int(self.act0), self.power)


    def off(self,so_exibe=False):
       try:
        if so_exibe == True:
            return

        if float(self.Ostate0)==0:            
            self.actor_off(int(self.act0))
        elif float(self.Ostate0)==1:
            self.actor_on(int(self.act0))
        elif float(self.Ostate0)==2:
           if float(self.Pstate0)==1:
                 self.actor_on(int(self.act0))
                 #print("!")
           else:
                self.actor_off(int(self.act0))
                #print("@")

       except Exception as e:
           return


    def verif_status(self):
        status=1
        try:
            if int(self.state0)!=int(self.actor_read_status(int(self.act0))):          
                     status=0#self.Pstate1 = self.actor_off(int(self.act1))
    
            return status
        except Exception as e:
            #print ("STATUS*=")
            #print(status)
            return status      



@cbpi.sensor
class SuperDummySensor(SensorActive):

    temp = Property.Number("Temperature", configurable=True, default_value=5, description="Dummy Temperature as decimal value")

    @cbpi.action("+")
    def my_action(self):
        self.temp=float(self.temp)+10

    @cbpi.action("-")
    def my_action(self):
        self.temp=float(self.temp)-10


    def get_unit(self):
        '''
        :return: Unit of the sensor as string. Should not be longer than 3 characters
        '''
        return "°C" if self.get_config_parameter("unit", "C") == "C" else "°F"

    def stop(self):
        SensorActive.stop(self)

    def execute(self):
        '''
        Active sensor has to handle his own loop
        :return: 
        '''
        while self.is_running() is True:
            self.data_received(self.temp)
            self.sleep(5)

    @classmethod
    def init_global(cls):
        '''
        Called one at the startup for all sensors
        :return: 
        '''


'''
@cbpi.actor
class ExibActor(ActorBase,StepBase):

    act0=Property.Actor("Actor 0")
    act1=Property.Actor("Actor 1")
    act2=Property.Actor("Actor 2")
    act3=Property.Actor("Actor 3")
    act4=Property.Actor("Actor 4")
    act5=Property.Actor("Actor 5")
    act6=Property.Actor("Actor 6")
    act7=Property.Actor("Actor 7")
    act8=Property.Actor("Actor 8")
    #def exib_on(self,power=None):
    #    return None
    def on(self, power=None, so_exibe=False):
        #self.actor_off(int(self.id))
        #print(int(self.act0))
        #print(int(self.act1))
        #print(int(self.id))
        try:
            if self.act0  !='':
                self.actor_exib(int(self.act0))
            if self.act1  !='':
                self.actor_exib(int(self.act1))
            if self.act2  !='':
                self.actor_exib(int(self.act2))
            if self.act3  !='':
                self.actor_exib(int(self.act3))
            if self.act4  !='':
                self.actor_exib(int(self.act4))
            if self.act5  !='':
                self.actor_exib(int(self.act5))
            if self.act6  !='':
                self.actor_exib(int(self.act6))
            if self.act7  !='':
                self.actor_exib(int(self.act7))
            if self.act8  !='':
                self.actor_exib(int(self.act8))
        except Exception as e:
            return

    def set_power(self, power):
            return

    def off(self,so_exibe=False):
        return
        #self.actor_exib_off(int(self.act0))
'''



@cbpi.actor
class ExibActorAuto(ActorBase,StepBase):

    #    return None
    def on(self, power=None, so_exibe=False):
            '''
            for key, value in cbpi.cache.get("actors").iteritems():
                estado =2
                try:
                    #print(value.instance.verif_status())
                    estado = value.instance.verif_status()
                    value.instance.on(so_exibe=True)
                    #value.state = 1
                    self.emit("SWITCH_ACTOR", value)
                    #self.actor_exib(int(value.instance))

                except Exception as e:
                    pass

                if estado == 0:
                        self.actor_exib(int(value.instance.id))
                        #print("!")
                elif estado==1:    
                        self.actor_exib(int(value.instance.id))
                        #print("@")
            '''
            self.atualiza()
            
    def set_power(self, power):
        '''
        Optional: Set the power of your actor
        :param power: int value between 0 - 100
        :return:
        '''

    def off(self,so_exibe=False):
        return

    def atualiza(self):
            for key, value in cbpi.cache.get("actors").iteritems():
                try:
                    estado = value.instance.verif_status()
                    self.actor_exib(int(value.instance.id))
                except Exception as e:
                    pass


@cbpi.backgroundtask(key="atualliza_exib", interval=1)

def atualliza_exib(api):
    """
    Processo em background para atualizar exibições - UTILIZA ExibActorAuto
    :return: None

    """
    for key, value in cbpi.cache.get("actors").iteritems():
        try:
            value.instance.atualiza() #so entra no atuadorque tem essa funcao...
        except Exception as e:
            pass