// ***
// *** DO NOT modify this file
// ***
#include <stdlib.h> 
#include <string.h> 
#include <stdio.h>
#include "fsm_macros.h"

// only 3 functions, no need to create .h file
void init_state();
void process_state(); 
void print_state();

int main()
{
  printf("%i\n",HW14_SONG_SPEED); //Record BPM
  init_state(); //Initialize
  print_state(0); //Print initialized without transition
  for(int i = 1;i < HW14_SONG_LENGTH; i++) {
    process_state(i);
    print_state(i);
  }
  return EXIT_SUCCESS;
}

