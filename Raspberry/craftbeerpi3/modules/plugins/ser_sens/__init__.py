# -*- coding: utf-8 -*-
import os
from subprocess import Popen, PIPE, call

from modules import cbpi, app
from modules.core.hardware import SensorPassive
import json
import os, re, threading, time
from flask import Blueprint, render_template, request
from modules.core.props import Property

temp = 22

blueprint = Blueprint('teste', __name__)

def getSensorsS():
    try:
        arr = []
        for dirname in os.listdir('/home/pi/entrada'):
           # if (dirname.startswith("28") or dirname.startswith("10")):
            arr.append(dirname)
        return arr
    except:
        return []




class myThreadS (threading.Thread):

    value = 0


    def __init__(self, sensor_name):
        threading.Thread.__init__(self)
        self.value = 0
        self.sensor_name = sensor_name
        self.runnig = True

    def shutdown(self):
        pass

    def stop(self):
        self.runnig = False

    def run(self):

        while self.runnig:
            try:
                app.logger.info("READ TEMP")
                ## Test Mode
                if self.sensor_name is None:
                    return
                with open('/home/pi/entrada/%s/entrada' % self.sensor_name, 'r') as content_file:
                    content = content_file.read()
                    #if (content.split('\n')[0].split(' ')[0] == self.sensor_name):
                    temp = float(content.split(' ')[1]) # temp in Celcius
                    self.value = temp
            except:
                pass

            time.sleep(4)



@cbpi.sensor
class SERIAL_SENSOR(SensorPassive):

    sensor_name = Property.Select("Sensor", getSensorsS())
    unidade=Property.Text("Unidade", configurable=True)    	

    def get_unit(self):
        '''
        :return: Unit of the sensor as string. Should not be longer than 3 characters
        '''
        return (self.unidade)
    def init(self):

        self.t = myThreadS(self.sensor_name)

        def shudown():
            shudown.cb.shutdown()
        shudown.cb = self.t
        self.t.start()

    def stop(self):
        try:
            self.t.stop()
        except:
            pass

    def read(self):
            self.data_received(round(self.t.value, 2))
    
@blueprint.route('/<int:t>', methods=['GET'])
def set_temp(t):
    global temp
    temp = t
    return ('', 204)


@cbpi.initalizer()
def init(cbpi):

    cbpi.app.register_blueprint(blueprint, url_prefix='/api/teste')
