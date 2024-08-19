# Binaural Beat Generator and Mixer

## Overview
This project is a Python-based application that generates binaural beats and mixes them with a video file. The application uses `ffmpeg` for video and audio processing and requires user input to configure the frequency transitions and volume levels for the binaural beats.

## Prerequisites
- Python 3.x
- `ffmpeg` installed and added to your system's PATH
- Required Python packages listed in `requirements.txt`

## Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure `ffmpeg` is installed and added to your system's PATH. You can check the installation by running:
    ```sh
    ffmpeg -version
    ```

## Usage
1. Place the video file (`.mp4` format) in the same directory as the program.

2. Run the main script:
    ```sh
    python main.py
    ```

3. Follow the on-screen prompts to:
    - Enter the number of frequency transitions.
    - Enter the start and end frequencies for each transition.
    - Enter the desired name for the output file (including the `.mp4` extension).
    - Enter the volume level for the binaural beats (0.0 to 1.0).

4. The program will generate a `.wav` file with the binaural beats and then mix it with the video file.

## Project Structure
- `main.py`: The main script that orchestrates the generation and mixing of binaural beats.
- `variables.py`: Contains the `Variables` class for handling user input and validation.
- `BinauralBeatGenerator.py`: Contains functions for generating binaural beats and transitions.
- `BinauralBeatMixer.py`: Contains the `BinauralBeatMixer` class for mixing the generated binaural beats with the video file.

## Example
```sh
python main.py