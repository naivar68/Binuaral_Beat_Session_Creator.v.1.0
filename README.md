# Binaural Beat Generator and Mixer

## Overview

This project provides a tool to generate binaural beats and mix them with a video file. It offers both a Command-Line Interface (CLI) and a web-based interface using Streamlit.

## Requirements

Ensure you have the following installed:
- Python 3.x
- FFMPEG
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Pre-Run Instructions

Before running the program, you need to prepare your video file as follows:

1. **Create or download a video** that you intend to use with the binaural beats.
2. **Edit the video** using a video editing tool such as `kdenlive` on Linux or a Windows equivalent to achieve the desired length and content.
3. **Take note of the EXACT time** of the video's duration after editing.
4. **Convert this duration to milliseconds** (e.g., a video of 2 minutes and 30 seconds has a duration of 150,000 milliseconds).
5. To calculate the number of milliseconds in 30 minutes:

    Convert minutes to seconds:
    30 minutes×60 seconds/minute=1800 seconds
    30minutes×60seconds/minute=1800seconds
    When inputting the value into the program **omit** the commas

5. When running the program, you must **input this value as the project duration**. Failure to follow these steps will result in errors during execution.
6. ** Ensure the video file is in MP4 format**.
## Usage

### Command-Line Interface (CLI)

1. Open a terminal and navigate to the project directory.
2. Run the program:
    ```sh
    python main.py
    ```
3. Select the CLI mode by entering `1`.
4. Follow the prompts to generate binaural beats and mix them with the video file.

### Web-Based Interface (Streamlit)

1. Open a terminal and navigate to the project directory.
2. Run the program:
    ```sh
    python main.py
    ```
3. Select the Streamlit mode by entering `2`.
4. A web browser will open with the Streamlit interface.
5. Configure the parameters in the sidebar:
    - Sample Rate (Hz)
    - Duration (milliseconds) (Ensure this matches the video duration)
    - Number of Frequency Transitions
    - Frequencies for each transition
    - Binaural Volume
    - Upload an MP4 video file
    - Output File Name
6. Click "Generate Binaural Beats" to create the binaural beats audio file.
7. Click "Mix with Video" to mix the generated binaural beats with the uploaded video file.

## Files

- `main.py`: Entry point for the application. Allows the user to choose between CLI and Streamlit interfaces.
- `streamlit_app.py`: Contains the Streamlit web interface logic.
- `BinauralBeatGenerator.py`: Functions to generate binaural beats.
- `BinauralBeatMixer.py`: Class to mix binaural beats with a video file.
- `variables.py`: Contains the `Variables` class to manage configuration and user inputs.
- `requirements.txt`: Lists the required Python packages.

## Troubleshooting

- If you encounter issues with FFMPEG, ensure it is correctly installed and accessible from the command line.
- Ensure all required Python packages are installed by running `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
