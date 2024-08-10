# BINAURALBEATGENERATOR.PY
import numpy as np
from scipy.io.wavfile import write
from variables import Variables


def generate_tone(frequency, duration, sample_rate=48000):
	t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
	return np.sin(2 * np.pi * frequency * t)

def generate_binaural_beat(left_freq, right_freq, duration, sample_rate=48000):
	left_tone = generate_tone(left_freq, duration, sample_rate)
	right_tone = generate_tone(right_freq, duration, sample_rate)
	return np.vstack((left_tone, right_tone)).T

def generate_binaural_beats_production(duration, frequency_transitions, sample_rate, output_file):
	total_duration = duration
	transition_duration = total_duration // len(frequency_transitions)

	full_beat = np.array([]).reshape(0, 2)

	for left_start_freq, right_start_freq, left_end_freq, right_end_freq in frequency_transitions:
		start_beats = generate_binaural_beat(left_start_freq, right_start_freq, transition_duration, sample_rate)
		transition = create_binaural_transition(left_start_freq, right_start_freq, left_end_freq, right_end_freq, transition_duration, sample_rate)
		full_beat = np.concatenate((full_beat, start_beats, transition))

	write(output_file, sample_rate, (full_beat * 32767).astype(np.int16))

		# Combine all parts

def create_binaural_transition(left_start_freq, right_start_freq, left_end_freq, right_end_freq, duration, sample_rate=48000):
	transition_duration = duration // 2
	left_frequencies = np.linspace(left_start_freq, left_end_freq, transition_duration * sample_rate)
	right_frequencies = np.linspace(right_start_freq, right_end_freq, transition_duration * sample_rate)

	left_channel = np.sin(2 * np.pi * left_frequencies * np.arange(transition_duration * sample_rate) / sample_rate)
	right_channel = np.sin(2 * np.pi * right_frequencies * np.arange(transition_duration * sample_rate) / sample_rate)

	return np.vstack((left_channel, right_channel)).T





if __name__ == "__main__":
	variables = Variables()
	variables.interface()
	generate_binaural_beats_production(duration, frequency_transitions, sample_rate, output_file)
	print("Binaural beats generated successfully.")
 

 
 