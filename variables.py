import os
import sys
import subprocess as sp
from os import path
import ffmpeg

class Variables:
    def __init__(self):
        self.sample_rate = None
        self.duration = 1805
        self.frequency_transitions = []
        self.video_name = "video.mp4"
        self.output_file = "" + ".mp4"
        self.binaural_volume = None   # Default volume level for binaural beats

    def is_ffmpeg_installed(self):
        ffmpeg_installation = sp.run("ffmpeg")
        if ffmpeg_installation == 1:
            print("Error: FFMPEG is not installed. Please install FFMPEG and add it to your PATH.")
            sys.exit()
        else:
            print("FFMPEG is installed.")
            return True

    def interface(self):
        try:
            self.sample_rate = 48000  # Fixed sample rate to 48000 Hz
            self.duration = 30 * 60  # Fixed duration to 30 minutes
            num_transitions = int(input("Enter the number of frequency transitions: "))

            for i in range(num_transitions):
                left_start_freq = int(input(f"Enter the start frequency for transition {i+1} (left ear, in Hz): "))
                right_start_freq = int(input(f"Enter the start frequency for transition {i+1} (right ear, in Hz): "))
                left_end_freq = int(input(f"Enter the end frequency for transition {i+1} (left ear, in Hz): "))
                right_end_freq = int(input(f"Enter the end frequency for transition {i+1} (right ear, in Hz): "))
                self.frequency_transitions.append((left_start_freq, right_start_freq, left_end_freq, right_end_freq))

            self.output_file = input("Enter the desired name for the output file (including the .mp4 extension): ")
            if not self.output_file.endswith(".mp4"):
                raise SystemExit("The output file must have a .mp4 extension.")

            self.binaural_volume = float(input("Enter the volume level for the binaural beats (0.0 to 1.0): "))
            if not (0.0 <= self.binaural_volume <= 1.0):
                raise ValueError("Volume level must be between 0.0 and 1.0")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit()

    def validate(self):
        if not all([self.sample_rate, self.duration, self.frequency_transitions, self.output_file]):
            print("Error: All values must be set and non-zero.")
            sys.exit()
        else:
            return self.sample_rate, self.duration, self.frequency_transitions, self.output_file