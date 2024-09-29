# Music Generation via State Machine

Learning Goals 
==============

This assignment asks you to create a finite state machine and print its current state.

Background
=====

The goal of this assignment is to procedurally generate music using a state machine. It is very easy to convert random number generation into music. Each musical note can be described as a whole number of half-steps higher or lower than the middle C key, where a half-step is a transition from two keys on a piano directly next to each other. Each half-step represents a 5.946% increase in pitch, with an octave (12 half-steps) doubling pitch. As a result, we can play any note `n` half-steps above middle C by playing at the frequency `f`, where `f=f0*2^(n/12)`. If we were to generate a random number between -42 and 41 and plug it into the formula above, it would match the pitch of one of the keys on an 84-key piano.

However, random notes do not normally sound very good. To improve the quality of our music, we will use a very simple model which restricts which notes can follow the note last played. To do this, we will use a finite state machine.

A finite state machine is a method of programming in which the program keeps track of its current state. This can be useful when you have multiple asynchronous systems working with each other. FSMs are very common in embedded systems, and are particularly useful in hardware description languages such as VHDL. However, they can be useful anywhere.

In the previous assignment, you were only using 5 notes, all of which were natural, and you were only playing one note at a time. For this assignment, you will be keeping track of not only 12 notes, but also their.

A chord is a series of notes played at the same time. There are two types of chords: major and minor chords. A major chord typically sounds "happy" to the ear, while a minor chord typically sounds "sad."

[Major audio]
[Minor audio]

You can make a major or minor chord out of any note on the scale. For example: C major is composed of the notes C, E, and G, and C munor is composed of the notes C, Eb, and G.

If you assign a number to every note, you can see how these relate to each other:

|C|C#|D|D#|E|F|F#|G|G#|A|A#|B |C |
|-|--|-|--|-|-|--|-|--|-|--|--|--|
|0|1 |2|3 |4|5|6 |7|8 |9|10|11|12|
|↑|  | |  |↑| |  |↑|  | |  |  |  |


|C|C#|D|D#|E|F|F#|G|G#|A|A#|B |C |
|-|--|-|--|-|-|--|-|--|-|--|--|--|
|0|1 |2|3 |4|5|6 |7|8 |9|10|11|12|
|↑|  | |↑ | | |  |↑|  | |  |  |  |

This can be extrapolated onto every other note. To play a major chord, you need to play the root, the root + 4, and the root + 7. To play a minor chord, you need to play the root, the root + 3, and the root + 7. Then, since we are limiting ourselves to one octave, you will need to loop back around whenever the result is higher than 11 (i.e., take modulo 12).

We are also going to restrict note transitions in a similar fashion. Rather than having each note have a chance to transition to each note, we will only be transferring to one of the notes in the common chords - the root (+0), third (+4), fourth (+5), or fifth (+7). After a C major/minor, our next chord will either be C, E, F, or G.

What You Need to Do
======================

1. Write the `init_state` function. This should seed the random number generator and
2. Write the `process_state` function. This should take the current state (note), generate a random number as described below, and then transition to the next note based on the rules described.
3. Finally, write the `print_state` function, which prints the properly formatted note.


The FSM rules are:

1. Each root note (C,C#,D...A#,B) should have its own unique state.
2. The "majorness" of the current chord should be stored independently, with a 40% chance to change each state transition.
3. The initial chord should be C major.
4. The transition from one chord to another is random. The next root note must be one of the notes in the current chord.
5. Implement random number generation as described below; doing it differently may cause your otherwise working code to not work with the autograder.
6. Every 8th note should be empty.


When printing a note, you must include whether it is sharp, natural or flat, by appending s, n or b respectively. In order to play a chord, you should put all notes for that chord on the same line. To print a C major chord, you might print something like this:

```
printf("Cn");
printf("En");
printf("Gn");
printf("\n");
```

When printing an empty note, you must still print a newline on its own. Additionally, you should still call the `rand()` function when skipping a note, but you shouldn't change the chord.

```
print("\n");
```

If you want to listen to the music your program produces, there is a Python script that will play the song. You can use it by running `make listen` in the assignment directory.

You may have to install pydub for this to work. Run `pip install pydub --user` if it fails.

FSM Transitions
==========

The transitions for this are much easier described compared to 13, since there are only 3 possible transitions.

* 10% chance to maintain the root note (+0)
* 30% chance to switch to the third (+4)
* 20% chance to switch to the fourth (+5)
* 40% chance to switch to the fifth (+7)

For instance, if your current chord is C major (C, E, G), your next chord will either be C (10%), E(30%), F(20%) or G(40%).

Random Number Generation
==========

Since this assignment uses pseudorandom number generation, in order to ensure consistency between tests, you will need to use a constant seed. This can be found in the file `fsm_macros.h`. When testing against the expected output, you should set `HW13_RAND_SEED` to `264`, which is its default value. You can change this to produce different music.

Random numbers should be generated using the standard `rand` function. This will generate a very large random number. Generate a random number, modulate by 100, and use that to evaluate the state transition, moving from left to right in the table.

For example: C transitions as follows.
|Note|C  |E  |F  |G  |
|-|-|-|-|-|
|C|10%|30%|20% |40%|

* If rand()%100 is between 0 and 9, the next root note is C.
* If rand()%100 is between 20 and 49, the next root note is E.
* If rand()%100 is between 50 and 69, the next root note is F.
* If rand()%100 is between 70 and 99, the next root note is G.

Additionally, whether a chord is major should be based on the same number. Do not call rand() a second time, or your RNG will not match the expected/autograder.

If rand()%100 is between 0 and 39, the chord should flip from major to minor or minor to major. Otherwise, it should remain what it is.

**Only generate the random number one time per `process_state`.** Generating it more than once per function call will make it generate different numbers. **You should still generate the random number when you are skipping a note.** Don't do anything with the number you generated.

You can test your random number generation by running `make test_rand`. With the default seed, print out your random number every time you call it, and don't print anything else. If you see nothing in the diff, then you are producing the correct random numbers.

Submission
==========

```
zip hw14.zip state_machine.c
```

Upload hw14.zip to Gradescope

Additional Reading
==================
