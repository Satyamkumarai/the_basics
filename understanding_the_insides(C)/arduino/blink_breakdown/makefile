CFLAGS ?= -Os -DF_APU=16000000UL -mmcu=atmega328p
LDFLAGS ?= -mmcu=atmega328p
# Path where your Arduino Uno is connected to
ARDUINO_USB ?= /dev/ttyUSB0
# if using old bootloader of  atmega328p use baud rate=57600 
# https://arduino.stackexchange.com/questions/51866/arduino-nano-atmega328p-bootloader-difference
BAUDRATE ?= 57600

all: led.hex

led.hex: led
	avr-objcopy -O ihex -R .eeprom led led.hex

led: led.o
	avr-gcc $(LDFLAGS) -o $@ $^

led.o: blink.c
	avr-gcc $(CFLAGS) -c -o $@ $<

deploy: led.hex
	avrdude  -c arduino -p ATmega328P -P ${ARDUINO_USB} -b $(BAUDRATE) -U flash:w:led.hex  

clean: FRC
	rm -f led.elf led.hex led.o led
disasm:
	avr-objdump -d -j .sec1 -m avr5 led.hex
FRC: