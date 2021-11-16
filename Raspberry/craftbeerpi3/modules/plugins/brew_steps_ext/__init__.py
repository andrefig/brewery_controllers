# -*- coding: utf-8 -*-
import time


from modules.core.props import Property, StepProperty
from modules.core.step import StepBase
from modules import cbpi


@cbpi.step
class TransfStep_Max(StepBase):
    '''
    Just put the decorator @cbpi.step on top of a method
    '''
    # Properties
    vol = Property.Number("Volume (Lim. Sup.)", configurable=True)
    pump = StepProperty.Actor("Pump")
    sensor = StepProperty.Sensor("Sensor de Volume")
    #@cbpi.action("Start Transfer")
    def init(self):
        self.actor_on(int(self.pump))
    #	pass
    # 	if self.is_timer_finished() is None:
    #   #self.start_timer(int(self.timer) * 60)
    def reset(self):
        pass
    def finish(self):     
        self.actor_off(int(self.pump))
    #def init(self):
    #   self.actor_on(int(self.pump))

    def execute(self):
        #self.actor_power(int(self.pump),self.get_sensor_value(self.sensor))
	if (int(self.get_sensor_value(self.sensor)) >= int(self.vol)):
            #self.actor_off(int(self.pump))
            self.next()
        #else:
        #    self.actor_power(int(self.pump),self.get_sensor_value(self.sensor))  

	#if self.is_timer_finished() == True:
        #    self.next()



@cbpi.step
class TransfStep_Min(StepBase):
    '''
    Just put the decorator @cbpi.step on top of a method
    '''
    # Properties
    vol = Property.Number("Volume (Lim. Inf.)", configurable=True)
    pump = StepProperty.Actor("Pump")
    sensor = StepProperty.Sensor("Sensor de Volume")
    #@cbpi.action("Start Transfer")
    def init(self):
        self.actor_on(int(self.pump))
    #	pass
    # 	if self.is_timer_finished() is None:
    #   #self.start_timer(int(self.timer) * 60)
    def reset(self):
        pass
    def finish(self):     
        self.actor_off(int(self.pump))
    #def init(self):
    #   self.actor_on(int(self.pump))

    def execute(self):
        #self.actor_power(int(self.pump),self.get_sensor_value(self.sensor))
	if (int(self.get_sensor_value(self.sensor)) < int(self.vol)):
            #self.actor_off(int(self.pump))
            self.next()
        #else:
        #    self.actor_power(int(self.pump),self.get_sensor_value(self.sensor))  


@cbpi.step
class DoubleHeatStep(StepBase):
    '''
    Just put the decorator @cbpi.step on top of a method
    '''
    # Properties
    temp1 = Property.Number("Temperature Kettle A", configurable=True, default_value=90, description="Target temperature")
    temp2 = Property.Number("Temperature Keetle B", configurable=True, default_value=90, description="Target temperature")

    kettle1 = StepProperty.Kettle("Kettle A")
    kettle2 = StepProperty.Kettle("Kettle B")

    timer = Property.Number("Timer in Minutes - Kettle A", configurable=True, default_value=90, description="Timer is started when target temperature is reached")

    def init(self):
        '''
        Initialize Step. This method is called once at the beginning of the step
        :return: 
        '''
        # set target tep
        self.set_target_temp(self.temp1, self.kettle1)
        self.set_target_temp(self.temp2, self.kettle2)



    @cbpi.action("Start Timer Now")
    def start(self):
        '''
        Custom Action which can be execute form the brewing dashboard.
        All method with decorator @cbpi.action("YOUR CUSTOM NAME") will be available in the user interface
        :return: 
        '''
        if self.is_timer_finished() is None:
            self.start_timer(int(self.timer) * 60)

    def reset(self):
        self.stop_timer()
        self.set_target_temp(self.temp1, self.kettle1)
        self.set_target_temp(self.temp2, self.kettle2)

    def finish(self):
        self.set_target_temp(0, self.kettle1)
        self.set_target_temp(0, self.kettle2)

    #def check_hop_timer(self, number, value):
    #
    #    if self.__getattribute__("hop_%s_added" % number) is not True and time.time() > (
    #        self.timer_end - (int(self.timer) * 60 - int(value) * 60)):
    #        self.__setattr__("hop_%s_added" % number, True)
    #        self.notify("Hop Alert", "Please add Hop %s" % number, timeout=None)

    def execute(self):
        '''
        This method is execute in an interval
        :return: 
        '''
        # Check if Target Temp is reached
        if self.get_kettle_temp(self.kettle1) >= int(self.temp1):
            # Check if Timer is Running
            if self.is_timer_finished() is None:
                self.start_timer(int(self.timer) * 60)
            #else:
            #    self.check_hop_timer(1, self.hop_1)
            #    self.check_hop_timer(2, self.hop_2)
            #    self.check_hop_timer(3, self.hop_3)
        # Check if timer finished and go to next step
        if self.is_timer_finished() == True:
            self.next()



@cbpi.step
class TControlStep(StepBase):
    '''
    Just put the decorator @cbpi.step on top of a method
    '''
    # Properties
    #temp = Property.Number("Set Point", configurable=True)
    #pump = StepProperty.Actor("Actor")
    #sensor = StepProperty.Sensor("Sensor")

    #act[2]=StepProperty.Actor("Actor 1")
    temp = Property.Number("Set Point", configurable=True,  description="Target Temperature")
    kettle = StepProperty.Kettle("Kettle", description="Kettle in which the mashing takes place")
    timer = Property.Number("Timer in Minutes", configurable=True, default_value=90, description="Timer is started when target temperature is reached")

    act1=StepProperty.Actor("Actor 1")
    act2=StepProperty.Actor("Actor 2")
    act3=StepProperty.Actor("Actor 3")
    act4=StepProperty.Actor("Actor 4")
    act5=StepProperty.Actor("Actor 5")
    act6=StepProperty.Actor("Actor 6")
    act7=StepProperty.Actor("Actor 7")
    act8=StepProperty.Actor("Actor 8")

    state1= Property.Number("State Actor 1", True, 0,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state2= Property.Number("State Actor 2", True, 0,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state3= Property.Number("State Actor 3", True, 0,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state4= Property.Number("State Actor 4", True, 0,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state5= Property.Number("State Actor 5", True, 0,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state6= Property.Number("State Actor 6", True, 0,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state7= Property.Number("State Actor 7", True, 0,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)
    state8= Property.Number("State Actor 8", True, 0,description="0 = LOW, 1 = HIGH")#, (0,1),description="0 = LOW, 1 = HIGH", configurable=True)


    #act = [act1,act2,act3,act4,act5,act6,act7,act8]
    #state = [state1,state2,state3,state4,state5,state6,state7,state8]
    #s = False



    def init(self):
        #print("INIT--")
        if float(self.state1)==0:            
            self.actor_off(int(self.act1))
        elif float(self.state1)==1:
            self.actor_on(int(self.act1))

        if float(self.state2)==0:            
            self.actor_off(int(self.act2))
        elif float(self.state2)==1:
            self.actor_on(int(self.act2))

        if float(self.state3)==0:            
            self.actor_off(int(self.act3))
        elif float(self.state3)==1:
            self.actor_on(int(self.act3))

        if float(self.state4)==0:            
            self.actor_off(int(self.act4))
        elif float(self.state4)==1:
            self.actor_on(int(self.act4))

        if float(self.state5)==0:            
            self.actor_off(int(self.act5))
        elif float(self.state5)==1:
            self.actor_on(int(self.act5))

        if float(self.state6)==0:            
            self.actor_off(int(self.act6))
        elif float(self.state6)==1:
            self.actor_on(int(self.act6))

        if float(self.state7)==0:            
            self.actor_off(int(self.act7))
        elif float(self.state7)==1:
            self.actor_on(int(self.act7))

        if float(self.state8)==0:            
            self.actor_off(int(self.act8))
        elif float(self.state8)==1:
            self.actor_on(int(self.act8))







            #    print(1)
        #print("!")
        #i = 0
        #for int i in range(8):
        #while i<8:
        #        state1=self.state[i]
        #        if ((float(state1))== 0):
        #            self.act[i].off()
        #            print(0)
        #        elif (float(state1)==1):
        #            self.act[i].on()
        #            print(1)    
        #        i=i+1
        #        print(self.state[i])
        #        if (((self.state[i]))== 0):
        #            self.act[i].off()
        #            print(0)
        #        elif ((float(self.state[i]))==1):
        #            self.act[i].on()
        #            print(1)
                ##elif state[i]==4:
                ##    if self.get_temp() < self.get_target_temp() - float(self.on):
                ##        act[i].on()
                ##    else:
                ##        act[i].off()
        #self.s = False
        self.set_target_temp(self.temp, self.kettle)
    #   pass

    #   if self.is_timer_finished() is None:
    #   #self.start_timer(int(self.timer) * 60)
    @cbpi.action("Start Timer Now")
    def start(self):
        '''
        Custom Action which can be execute form the brewing dashboard.
        All method with decorator @cbpi.action("YOUR CUSTOM NAME") will be available in the user interface
        :return: 
        '''
        #for i in range(8):
        #        if self.state[i]== 0:
        #            self.act[i].off()
        #        elif self.state[i]==1:
        #            self.act[i].on()
                #elif state[i]==4:
                #    if self.kettle.heater:
                #        act[i].on()
                #    else:
                #        act[i].off()

        if self.is_timer_finished() is None:
            self.start_timer(int(self.timer) * 60)


    def reset(self):
        self.stop_timer()
        self.set_target_temp(self.temp, self.kettle)

    def finish(self):

        self.set_target_temp(0, self.kettle)

        if float(self.state1)==0:            
            self.actor_off(int(self.act1))
        elif float(self.state1)==1:
            self.actor_off(int(self.act1))

        if float(self.state2)==0:            
            self.actor_off(int(self.act2))
        elif float(self.state2)==1:
            self.actor_off(int(self.act2))

        if float(self.state3)==0:            
            self.actor_off(int(self.act3))
        elif float(self.state3)==1:
            self.actor_off(int(self.act3))

        if float(self.state4)==0:            
            self.actor_off(int(self.act4))
        elif float(self.state4)==1:
            self.actor_off(int(self.act4))

        if float(self.state5)==0:            
            self.actor_off(int(self.act5))
        elif float(self.state5)==1:
            self.actor_off(int(self.act5))

        if float(self.state6)==0:            
            self.actor_off(int(self.act6))
        elif float(self.state6)==1:
            self.actor_off(int(self.act6))

        if float(self.state7)==0:            
            self.actor_off(int(self.act7))
        elif float(self.state7)==1:
            self.actor_off(int(self.act7))

        if float(self.state8)==0:            
            self.actor_off(int(self.act8))
        elif float(self.state8)==1:
            self.actor_off(int(self.act8))


        #for i in range(8):
        #        if self.state[i]== 0:
        #            self.act[i].off()
        #        elif self.state[i]==1:
        #            self.act[i].off()
                #elif state[i]==4:
                #    act[i].off()

    def execute(self):
        '''
        This method is execute in an interval
        :return: 
        '''

        # Check if Target Temp is reached
        if self.get_kettle_temp(self.kettle) >= float(self.temp):
            # Check if Timer is Running
            if self.is_timer_finished() is None:
                self.start_timer(int(self.timer) * 60)

        # Check if timer finished and go to next step
        if self.is_timer_finished() == True:
            self.next()
