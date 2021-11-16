from modules import cbpi
from modules.core.controller import KettleController
from modules.core.props import Property


@cbpi.controller
class Hysteresis_mod(KettleController):

    # Custom Properties

    on = Property.Number("Offset On", True, 0, description="Offset below target temp when heater should switched on. Should be bigger then Offset Off")
    off = Property.Number("Offset Off", True, 0, description="Offset below target temp when heater should switched off. Should be smaller then Offset Off")
    
    act = []
    state = []

    act.append(Property.Actor("Actor 1"))
    act.append(Property.Actor("Actor 2"))
    act.append(Property.Actor("Actor 3"))
    act.append(Property.Actor("Actor 4"))
    act.append(Property.Actor("Actor 5"))
    act.append(Property.Actor("Actor 6"))
    act.append(Property.Actor("Actor 7"))
    act.append(Property.Actor("Actor 8"))

    state.append(Property.Select("State Actor 1", (0,1,4),description="0 = LOW, 1 = HIGH, 4 = on with heater"))
    state.append(Property.Select("State Actor 2", (0,1,4),description="0 = LOW, 1 = HIGH, 4 = on with heater"))
    state.append(Property.Select("State Actor 3", (0,1,4),description="0 = LOW, 1 = HIGH, 4 = on with heater"))
    state.append(Property.Select("State Actor 4", (0,1,4),description="0 = LOW, 1 = HIGH, 4 = on with heater"))
    state.append(Property.Select("State Actor 5", (0,1,4),description="0 = LOW, 1 = HIGH, 4 = on with heater"))
    state.append(Property.Select("State Actor 6", (0,1,4),description="0 = LOW, 1 = HIGH, 4 = on with heater"))
    state.append(Property.Select("State Actor 7", (0,1,4),description="0 = LOW, 1 = HIGH, 4 = on with heater"))
    state.append(Property.Select("State Actor 8", (0,1,4),description="0 = LOW, 1 = HIGH, 4 = on with heater"))



    def stop(self):
        '''
        Invoked when the automatic is stopped.
        Normally you switch off the actors and clean up everything
        :return: None
        '''
        super(KettleController, self).stop()
        self.heater_off()

        for i in range(8):
                if state[i]== 0:
                    act[i].off()
                elif state[i]==1:
                    act[i].off()
                elif state[i]==4:
                    act[i].off()

    def run(self):
        '''
        Each controller is exectuted in its own thread. The run method is the entry point
        :return: 
        '''
        while self.is_running():
            for i in range(8):
                if state[i]== 0:
                    act[i].off()
                elif state[i]==1:
                    act[i].on()
                elif state[i]==4:
                    if self.get_temp() < self.get_target_temp() - float(self.on):
                        act[i].on()
                    else:
                        act[i].off()


            if self.get_temp() < self.get_target_temp() - float(self.on):
                self.heater_on(100)

            elif self.get_temp() >= self.get_target_temp() - float(self.off):
                self.heater_off()
            else:
                self.heater_off()
            self.sleep(1)

