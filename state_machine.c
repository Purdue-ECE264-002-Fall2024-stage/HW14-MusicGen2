// ***
// *** You MUST modify this file
// ***

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h> 
#include <string.h>
#include "fsm_macros.h"

void init_state() {
  //In this function you should seed the random number generator and initialize your FSM to its default state.

}

void process_state(int note_count) {
  //In this function you should process the specified state transitions by generating a random number.
  //Every 8th note should be silent, and the state transition logic should be skipped. However, you should still call rand() when skipping a note.

}

void print_state(int note_count) {
  //In this process you should simply print the current state. An example for the 'C' state is already present.
  //Every 8th note should be skipped/silent. You still have to print a newline when skipping a note!
  
}