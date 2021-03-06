//Tell which board we are using 
// #define __AVR_ATmega328P__

#include <avr/io.h>


#define BLINK_DELAY_MS 1000

#include <util/delay.h>

int main (void)
{
  // Arduino digital pin 13 (pin 5 of PORTB) for output
  DDRB |= 0B100000; // PORTB5

  while(1) {
    // turn LED on
    PORTB |= 0B100000; // PORTB5
    _delay_ms(BLINK_DELAY_MS);

    // turn LED off
    PORTB &= ~ 0B100000; // PORTB5
    _delay_ms(BLINK_DELAY_MS);
  }
}