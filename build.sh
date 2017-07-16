#!/bin/bash

/opt/arduino-1.8.3/arduino --verify --board arduino:avr:mega:cpu=atmega2560 --pref build.path=${HOME}/Code/printers/build/ Marlin/Marlin.ino
