import cv2
import numpy as np
import time
import os
import platform
from datetime import datetime
from DWVideoLogger import DWVideoLogger
from DWCamera import DWCamera
from DWCalibrationGUI import DWCalibrationGUI
import json

# Targets class for loading and storing calibration points
class DWTargets:
    def __init__(self, config):
        self.points = self.load(config)

    def load(self, config):
        # Load default points from config
        default_points = config.get('default_targets', None)
        if default_points is None:
            raise ValueError("No default targets found in config.json under 'default_targets'.")
        # Convert list of [x, y] to list of (x, y) tuples
        return [tuple(pair) for pair in default_points]

def main():
    config_path = 'config.json'
    with open(config_path, 'r') as f:
        config = json.load(f)

    targets = DWTargets(config)

    os.makedirs(config.get('save_dir', 'Data'), exist_ok=True)

    timestamp_str = datetime.now().strftime("%m%d_%H%M")
    system_name = platform.system()
    if system_name == 'Darwin':
        fourcc = cv2.VideoWriter_fourcc(*'avc1')
        video_extension = 'mov'
    else:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video_extension = 'avi'

    config['fourcc'] = fourcc
    config['video_extension'] = video_extension
    config['timestamp_str'] = timestamp_str
    config['fps'] = 30

    camera = DWCamera(config)
    gui = DWCalibrationGUI(config)
    logger = DWVideoLogger(config)

    available_cameras = camera.list_cameras()
    if not available_cameras:
        print("Error: No available cameras found.")
        exit()
    default_camera = available_cameras[0]
    if not camera.connect(default_camera):
        print(f"Error: Could not open default camera {default_camera}.")
        exit()

    gui.setup_window()

    print("Press 's' to start calibration and recording, 'ESC' to exit. Press 'l' to list cameras and switch.")

    while True:
        ret, frame = camera.read()
        if not ret:
            print("Error: Failed to capture frame from camera.")
            break
        cv2.imshow('Calibration', frame)

        key = cv2.waitKey(1)
        if key == ord('l'):
            cameras = camera.list_cameras()
            if not cameras:
                print("No cameras found.")
            else:
                print("Available cameras:")
                for cam in cameras:
                    print(f"Camera Index: {cam}")
        elif ord('0') <= key <= ord('9'):
            new_index = key - ord('0')
            print(f"Switching to camera {new_index}")
            camera.connect(new_index)
        elif key == ord('s'):
            frame_size = (frame.shape[1], frame.shape[0])
            logger.start(frame_size)
            break
        elif key == 27:
            camera.release()
            logger.release()
            gui.destroy()
            exit()

    print("Press 'b' during calibration to toggle background (camera/blank).")

    current_point_idx = 0
    num_points = len(targets.points)
    target_start_time = time.time()

    while current_point_idx < num_points:
        ret, camera_frame = camera.read()
        if not ret:
            print("Error: Failed to capture frame from camera.")
            break

        frame = gui.prepare_frame(camera_frame, targets.points[current_point_idx])

        cv2.imshow('Calibration', frame)

        # Save the real camera frame, not the calibration screen
        logger.write_frame(camera_frame, targets.points[current_point_idx][0], targets.points[current_point_idx][1])

        key = cv2.waitKey(1)
        if key == 27:
            break
        elif key == ord('b'):
            gui.toggle_background()

        if time.time() - target_start_time >= config.get('target_display_time', 3.0):
            current_point_idx += 1
            target_start_time = time.time()

    logger.release()
    camera.release()
    gui.destroy()

    video_path, log_file_path = logger.get_paths()

    print(f"Calibration finished. Video saved to: {video_path}")
    print(f"Frame log saved to: {log_file_path}")

if __name__ == "__main__":
    print("Starting")
    main()
