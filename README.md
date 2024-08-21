# Queue Counting System Using YOLOv8

## Overview

This project is a Queue Counting System that utilizes the YOLOv8 object detection model to identify and track vehicles in a video feed. The system focuses on counting the number of vehicles—specifically cars, buses, and trucks—present in a designated queue region. This application is particularly useful for traffic management and monitoring vehicle congestion in real-time.

## Features

- **YOLOv8 Object Detection:** 
  - Implements YOLOv8 (You Only Look Once) for fast and accurate detection of vehicles such as cars, buses, and trucks.
  
- **Queue Region Monitoring:** 
  - Monitors a specific region of interest (ROI) within the video frame, counting vehicles that enter this area.
  
- **Real-Time Tracking:** 
  - Assigns unique IDs to vehicles for consistent tracking as they move within and out of the queue region.
  
- **Custom Visualization:** 
  - Visualizes detected vehicles with bounding boxes, center point markers, and descriptive labels showing vehicle type and ID.
  - Displays real-time queue counts on the video feed.

- **Performance Optimization:** 
  - Optimized for real-time processing, ensuring smooth and accurate detection even with a low confidence threshold.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MohammedHamza0/QueueCountingSystem.git
   cd QueueCountingSystem
   ```

2. **Install Dependencies:**
   Ensure you have Python installed, then install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLOv8 Model:**
   - You can download the YOLOv8 model (`yolov8m.pt`) from the [Ultralytics YOLOv8 repository](https://github.com/ultralytics/ultralytics).

4. **Place Your Video File:**
   - Add your video file to the project directory or specify the path to your video file in the code.

## Usage

1. **Modify the Queue Region:**
   - Define the region of interest (ROI) in the code by modifying the `queue_region` variable to fit your video frame.

2. **Run the Queue Counting System:**
   ```bash
   python queue_counting.py
   ```

3. **View the Output:**
   - The system will display the video feed with detected vehicles, showing bounding boxes, vehicle type, IDs, and the real-time queue count.

## Code Structure

- `queue_counting.py`: The main script that runs the queue counting system.
- `requirements.txt`: List of Python dependencies required to run the project.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request if you have any improvements or new features to add.
