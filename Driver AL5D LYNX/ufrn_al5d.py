#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:24:07 2018

@author: jean
"""
import time
import serial

 
SERIAL_PORT='/dev/ttyS0' #Serial
BAUD_RATE='115200'       #Set Baud rates to 115200
TIMEOUT='1'              #Timeout after opening
PARITY='N'               # No parity
STOPBITS='1'             
BYTESIZE='8'        

def abre():
    print ('\nObtendo informacoes sobre a comunicacao serial\n')
    # Iniciando conexao serial
    #comport = serial.Serial(DEVICE, 115200, timeout=1)
    serial_port = serial.Serial(SERIAL_PORT,
        int(BAUD_RATE),
        timeout=int(TIMEOUT),
        bytesize=int(BYTESIZE),
        stopbits=int(STOPBITS),
        parity=PARITY)
 # Alem das opcoes rtscts=BOOL, xonxoff=BOOL, e dsrdtr=BOOL
    time.sleep(1.8) # Entre 1.5s a 2s
    print ('\nStatus Porta: %s ' % (serial_port.isOpen()))
    print ('Device conectado: %s ' % (serial_port.name))
    print ('Dump da configuracao:\n %s ' % (serial_port))
    print('\n###############################################\n')
    serial_port.close()

""" main """
if __name__ == '__main__':
    abre()