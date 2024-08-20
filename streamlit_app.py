import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from BinauralBeatGenerator import generate_binaural_beats_production
from BinauralBeatMixer import BinauralBeatMixer
from variables import Variables

def load_and_plot_csv(file_path):
    # Load the CSV file
    file_path = "binaural_beats_chart.csv"
    df = pd.read_csv(file_path)

    # Plotting with matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(ax=ax)

    ax.set_title("Binaural Beats Chart")
    ax.set_xlabel("X-axis Label")
    ax.set_ylabel("Y-axis Label")

    return fig

def run_streamlit_app():
    # Load and display the chart
    chart_fig = load_and_plot_csv('binaural_beats_chart.csv')
    st.pyplot(chart_fig)

    st.title("Binaural Beat Generator and Mixer")
    st.write("This tool allows you to generate binaural beats and mix them with a video file.")

    # Sidebar for input parameters
    st.sidebar.header("Configuration")

    # Initialize variables
    variables = Variables()

    # Sample rate and duration are pre-set in your Variables class, adjust if necessary
    variables.sample_rate = st.sidebar.number_input("Sample Rate (Hz)", value=variables.sample_rate)
    variables.duration = st.sidebar.number_input("Duration (seconds)", value=variables.duration)

    # Number of frequency transitions
    num_transitions = st.sidebar.number_input("Number of Frequency Transitions", min_value=1, max_value=10, value=len(variables.frequency_transitions) or 1)
    variables.frequency_transitions = []
    for i in range(num_transitions):
        st.sidebar.subheader(f"Transition {i + 1}")
        left_start_freq = st.sidebar.number_input(f"Left Start Frequency (Hz) - Transition {i + 1}", value=100)
        right_start_freq = st.sidebar.number_input(f"Right Start Frequency (Hz) - Transition {i + 1}", value=100)
        left_end_freq = st.sidebar.number_input(f"Left End Frequency (Hz) - Transition {i + 1}", value=200)
        right_end_freq = st.sidebar.number_input(f"Right End Frequency (Hz) - Transition {i + 1}", value=200)
        variables.frequency_transitions.append((left_start_freq, right_start_freq, left_end_freq, right_end_freq))

    # Binaural volume (adjust according to your project defaults)
    variables.binaural_volume = st.sidebar.slider("Binaural Volume", min_value=0.0, max_value=1.0, value=variables.binaural_volume or 0.5)

    # Video file upload
    uploaded_video = st.sidebar.file_uploader("Upload MP4 Video", type=["mp4"])

    # Output file name
    variables.output_file = st.sidebar.text_input("Output File Name", value=variables.output_file or "output.mp4")

    # Generate Binaural Beats
    if st.sidebar.button("Generate Binaural Beats"):
        st.write("Generating binaural beats...")
        generate_binaural_beats_production(variables.duration, variables.frequency_transitions, variables.sample_rate, "binaural_beats.wav")
        st.success("Binaural beats generated successfully.")

    # Mix Binaural Beats with Video
    if st.sidebar.button("Mix with Video"):
        if uploaded_video is None:
            st.error("Please upload a video file.")
        else:
            with open("video.mp4", "wb") as f:
                f.write(uploaded_video.getbuffer())

            st.write("Mixing audio with video...")
            mixer = BinauralBeatMixer(variables)
            mixer.binaural_mixer()
            st.success(f"Video and binaural beats mixed successfully. The output file is named {variables.output_file}.")

if __name__ == "__main__":
    run_streamlit_app()
