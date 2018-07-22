import sys


def playWAV( fname ):
  import pymedia.audio.sound as sound
  import time, wave
  f= wave.open( fname, 'rb' )
  sampleRate= f.getframerate()
  channels= f.getnchannels()
  format= sound.AFMT_S16_LE
  snd1= sound.Output( sampleRate, channels, format )
  s= ' '
  while len( s ):
    s= f.readframes( 1000 )
    snd1.play( s )
  
  # Since sound module is not synchronous we want everything to be played before we exit
  while snd1.isPlaying(): time.sleep( 0.05 )

# ----------------------------------------------------------------------------------

# Play a wav file through the sound object

# http://pymedia.org/

if __name__== '__main__':
  print("Usage: play_wav <file>")
  playWAV("demp.wav")
