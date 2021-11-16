#!/usr/bin/env python

#fonte = open ('/dev/ttyDUMMY', 'r')

import time
import subprocess
import select
import os


#os.system('sudo interceptty /dev/ttyUSB0 /dev/ttyDUMMY')
#time.sleep(5)

while 1==1:
 time.sleep(0.1)
 try:
  f = subprocess.Popen(['head','-n2','/dev/ttyDUMMY'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  p = select.poll()
  p.register(f.stdout)
  content =  f.stdout.readline()
  #s0=open('/home/pi/teste111.txt','r+w')
  #s0.write(content.split()[0])
  #s0.write(';')
  #s0.write(content)
  #s0.write(';')
  #s0.write(content.split()[0])
  #s0.write(';')
  #s0.write(content.split()[1])
  #s0.write(';')
  #s0.write(content.split()[2])
  #s0.write(';')
  #s0.write(content.split()[3])
  #s0.write(';')

  if (content.split()[0] == 'DAT'):
		i=1
		for dirname in os.listdir('/home/pi/entrada'):  #range(1,1
		   #try:
	            	t1 = ( (content.split()[i]))
			#s0.write(str(i))
			#s0.write('---')
			#s0.write(t1)
			#s0.write('!')
			saida=open('/home/pi/entrada/%s/entrada' % str(i-1),'w') #??
			saida.write(str(i-1))
			saida.write(' ')
			saida.write(t1)
			saida.close()            	
			i=i+1	
  if (content.split()[0] == 'DAT2'):
    i=1
    for dirname in os.listdir('/home/pi/entrada2'):  #range(1,1
       #try:
      t1 = ( (content.split()[i]))
      #s0.write(str(i))
      #s0.write('---')
      #s0.write(t1)
      #s0.write('!')
      saida=open('/home/pi/entrada2/%s/entrada' % str(i-1),'w') #??
      saida.write(str(i-1))
      saida.write(' ')
      saida.write(t1)
      saida.close()             
      i=i+1 
 except:
   pass
 time.sleep(0.1)
 try:
  f = subprocess.Popen(['head','-n2','/dev/ttyDUMMY1'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  p = select.poll()
  p.register(f.stdout)
  content =  f.stdout.readline()
  #s0=open('/home/pi/teste111.txt','r+w')
  #s0.write(content.split()[0])
  #s0.write(';')
  #s0.write(content)
  #s0.write(';')
  #s0.write(content.split()[0])
  #s0.write(';')
  #s0.write(content.split()[1])
  #s0.write(';')
  #s0.write(content.split()[2])
  #s0.write(';')
  #s0.write(content.split()[3])
  #s0.write(';')
  if (content.split()[0] == 'DAT'):
    i=1
    for dirname in os.listdir('/home/pi/entrada'):  #range(1,1
       #try:
      t1 = ( (content.split()[i]))
      #s0.write(str(i))
      #s0.write('---')
      #s0.write(t1)
      #s0.write('!')
      saida=open('/home/pi/entrada/%s/entrada' % str(i-1),'w')
      saida.write(str(i-1))
      saida.write(' ')
      saida.write(t1)
      saida.close()             
      i=i+1 
  if (content.split()[0] == 'DAT2'):
		i=1
		for dirname in os.listdir('/home/pi/entrada2'):  #range(1,1
		   #try:
			t1 = ( (content.split()[i]))
			#s0.write(str(i))
			#s0.write('---')
			#s0.write(t1)
			#s0.write('!')
			saida=open('/home/pi/entrada2/%s/entrada' % str(i-1),'w') #??
			saida.write(str(i-1))
			saida.write(' ')
			saida.write(t1)
			saida.close()            	
			i=i+1	
 except:
   pass
 time.sleep(0.1)
