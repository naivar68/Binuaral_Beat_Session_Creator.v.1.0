# MAIN.PY
import os
import sys
import subprocess as sp
from BinauralBeatGenerator import *
from BinauralBeatMixer import *
from variables import Variables



def main():
	sp.run("cls" if os.name == "nt" else "clear", shell=True)
	print('''
          Binaural Beat Generator and Mixer
          ---------------------------------
          Ensure you have installed the requirements in requirements.txt and FFMPEG.
          The video file must be in the same directory as this program and must be an MP4 file.
          ''')

	print("checking for ffmpeg...")
	variables = Variables()
	variables.is_ffmpeg_installed()

	print("Are you ready to create the beats .wav file?")
	answer = input("Enter 'yes' or 'no': ")
	if answer.lower() == "yes":
		variables.interface()
		generate_binaural_beats_production(variables.duration, variables.frequency_transitions, variables.sample_rate, "binaural_beats.wav")
	else:
		print("Exiting program...")
		sys.exit()

	print("Are you ready to mix the audio with the video?")
	answer = input("Enter 'yes' or 'no': ")
	if answer.lower() == "yes":
		mixer = BinauralBeatMixer(variables)
		mixer.binaural_mixer()
	else:
		print("Exiting program...")
		sys.exit()



if __name__ == "__main__":
	main()