import os
import ffmpeg
from variables import Variables
from pathlib import Path






class BinauralBeatMixer:
    def __init__(self, variables):
        self.duration = variables.duration
        self.sample_rate = variables.sample_rate
        self.video_name = "video.mp4"
        self.output_file = variables.output_file
        self.ffmpeg_path = 'ffmpeg'
        self.binaural_volume = variables.binaural_volume

    def binaural_mixer(self):
        try:
            if Path('binaural_beats.wav').exists():
                input_video = ffmpeg.input(self.video_name)
                input_audio = ffmpeg.input('binaural_beats.wav')
                original_audio = input_video.audio
                adjusted_binaural_audio = input_audio.filter('volume', self.binaural_volume)
                mixed_audio = ffmpeg.filter([original_audio, adjusted_binaural_audio], 'amix', inputs=2)
                output = ffmpeg.output(input_video.video, mixed_audio, self.output_file)
                output.run()
                print(f"Binaural beats mixed with video successfully. The output file is named {self.output_file}.")
            else:
                print("File 'binaural_beats.wav' does not exist. Please generate the binaural beat file first.")
                raise SystemExit()
        except ffmpeg.Error as e:
            print(f"An error occurred while mixing binaural beats with the video file: {e}")
            return None

