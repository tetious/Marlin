avrdude -p atmega2560 -P /dev/ttyACM0 -b 115200 -c wiring -D -U "flash:w:marlin.hex:i"
