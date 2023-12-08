# Ball Tracking Project

<img src="https://raw.githubusercontent.com/Rajivjha003/Color-Balls-Tracker/main/ball%20tracked%20img.png?token=GHSAT0AAAAAACK3E6ZSNVZW5ZJCN243SRCOZLTG5FQ" alt="Screenshot">

## Overview

This project is aimed at tracking colored balls in a video, recording entry and exit events in various quadrants, and producing a processed video with color overlays.
## Features

- **Color Tracking:** Utilizes computer vision techniques to track balls of different colors (white, yellow, green, pink) in a given video.

- **Quadrant Detection:** Divides the video frame into four quadrants and detects entry and exit events of colored balls in each quadrant.

- **Processed Video Output:** Generates a processed video with color overlays indicating ball positions and timestamps for entry/exit events.

## Project Structure

- **ball_tracking.py:** The main Python script for ball tracking.

- **output_video.avi:** The processed video with color overlays.

- **output.txt:** Text file containing event data.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## How to Use

1. Clone the repository.

```bash
git clone https://github.com/your-username/ball-tracking.git

