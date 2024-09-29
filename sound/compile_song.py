from pydub import AudioSegment
from pydub.playback import play
import math

song_file="output"
sound_file="piano_"
sound_ext=".wav"

def note_from_file(note):
    return AudioSegment.from_file("sound/sounds/piano_" + note + ".wav")

notes={
    "Cn": note_from_file("c"),
    "Cs": note_from_file("cs"),
    "Db": note_from_file("cs"),
    "Dn": note_from_file("d"),
    "Ds": note_from_file("ds"),
    "Eb": note_from_file("ds"),
    "En": note_from_file("e"),
    "Fb": note_from_file("e"),
    "Es": note_from_file("f"),
    "Fn": note_from_file("f"),
    "Fs": note_from_file("fs"),
    "Gb": note_from_file("fs"),
    "Gn": note_from_file("g"),
    "Gs": note_from_file("gs"),
    "Ab": note_from_file("gs"),
    "An": note_from_file("a"),
    "As": note_from_file("as"),
    "Bb": note_from_file("as"),
    "Bn": note_from_file("b"),
    "Cb": note_from_file("b"),
    "C2": note_from_file("c2")
}


f=open(song_file)
song_lines=f.readlines()
f.close()


bpm=int(song_lines[0])

sample_rate = 24000.0 #Hz
note_duration = 3360 #ms - length of the note file in ms
note_separation = math.floor(1000*60/bpm) #ms - time between two notes\
note_silence = 438 #ms - silence at beginning of piano note


song=0 #song variable
bonus_separation=0 #extra separation due to silent note(s)


for song_line in song_lines[1:]:
    note="" #note string
    line_notes=[] #list of notes on this line
    for c in song_line: #iterate through characters. don't need to trim newline as notes are even # of chars
        if note=="": #if this is the first character in a note, store it and then read the next character
            note=c
        else: 
            note=note+c #append modifier (n,b,s) to note
            line_notes = line_notes + [notes[note]] #lookup the note file for this note and append it to the note list
            note="" #reset the note string
    if len(line_notes) == 0: #do not want to try to iterate nothing
        bonus_separation = bonus_separation + note_separation #extra separation due to silent note(s)
    else:
        mixed=line_notes[0][note_silence:] #establish AudioSegment to mix
        for line_note in line_notes[1:]:
            mixed=mixed.overlay(line_note[note_silence:]) #overlay each note in this line
        if song == 0: #if this is the first note, song variable needs to be set, not modified
            song = mixed
        else:
            #Cuts the current song 500ms after the most recent note then appends this note
            song = song[:-note_duration+note_separation+note_silence+bonus_separation] + mixed
            bonus_separation=0 #this note wasn't empty, so don't delay the next note more
song.export("song.wav",format="wav") #export as wav to share
play(song) #play immediately