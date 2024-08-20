import subprocess as sp
import sys
import os
import streamlit.cli_util as stcli
from BinauralBeatGenerator import *
from BinauralBeatMixer import *
from variables import Variables

def run_cli_version():
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

def run_streamlit_version():
    # Ensure this function runs the Streamlit version of the app
        sys.exit(stcli.main())

def main():
    print("Select the mode to run the application:")
    print("1. Command-Line Interface (CLI)")
    print("2. Web-Based Interface (Streamlit)")

    choice = input("Enter the number of your choice (1 or 2): ")

    if choice == '1':
        run_cli_version()
    elif choice == '2':
        # Activate streamlit virtual environment
        os.system("streamlit run streamlit_app.py")

    else:
        print("Invalid choice. Please enter 1 or 2.")
        sys.exit()

if __name__ == "__main__":
    main()

