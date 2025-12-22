import cv2
import os
import time
import numpy as np


class DWVideoLogger:
    def __init__(self, config):
        self.save_dir = config.get('save_dir', 'Data')
        self.timestamp_str = config.get('timestamp_str')
        self.fps = config.get('fps', 30)
        self.fourcc = config.get('fourcc', None)
        # Get video extension from config, default to 'avi'
        self.video_extension = config.get('video_extension', 'avi')
        # Determine extension based on system type if not provided
        if 'video_extension' not in config:
            import platform
            sys_platform = platform.system().lower()
            if 'darwin' in sys_platform or 'mac' in sys_platform:
                self.video_extension = 'mov'
            else:
                self.video_extension = 'avi'
        self.video_path = os.path.join(self.save_dir, f'camera_feed_{self.timestamp_str}.{self.video_extension}')
        self.log_file_path = os.path.join(self.save_dir, f'log_{self.timestamp_str}.csv')
        self.video_writer = None
        self.log_file = None
        self.frame_counter = 0

    def start(self, frame_size):
        self.video_writer = cv2.VideoWriter(self.video_path, self.fourcc, self.fps, frame_size)
        if not self.video_writer.isOpened():
            raise RuntimeError(f"Failed to open video writer with filename {self.video_path}")
        self.log_file = open(self.log_file_path, 'w')
        self.log_file.write(f'# VideoFile: {os.path.basename(self.video_path)}\n')
        self.log_file.write('FrameNumber,Timestamp,TargetX,TargetY\n')

    def write_frame(self, frame, target_x, target_y):
        if self.video_writer is not None:
            self.video_writer.write(frame)
        if self.log_file is not None:
            timestamp = int(time.time() * 1e6)  # microseconds
            self.log_file.write(f'{self.frame_counter},{timestamp},{target_x},{target_y}\n')
            self.frame_counter += 1

    def release(self):
        if self.video_writer is not None:
            self.video_writer.release()
        if self.log_file is not None:
            self.log_file.close()

    def get_paths(self):
        return self.video_path, self.log_file_path

class DWCalibrationGUI:
    CROSS_SIZE = 5

    def __init__(self, config):
        self.use_camera_background = False
        self.background_color = tuple(config.get('background_color', (255, 255, 255)))
        self.target_radius = config.get('target_radius', 30)
        self.target_color = tuple(config.get('target_color', (0, 0, 255)))

    def setup_window(self):
        cv2.namedWindow('Calibration', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('Calibration', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    def prepare_frame(self, camera_frame, target_point):
        screen_width = camera_frame.shape[1]
        screen_height = camera_frame.shape[0]
        camera_frame = cv2.resize(camera_frame, (screen_width, screen_height))
        if self.use_camera_background:
            frame = camera_frame.copy()
        else:
            frame = np.full((screen_height, screen_width, 3), self.background_color, dtype=np.uint8)

        abs_x = int(target_point[0] * screen_width)
        abs_y = int(target_point[1] * screen_height)

        self.draw_target(frame, abs_x, abs_y)
        return frame

    def draw_target(self, frame, x, y):
        cv2.circle(frame, (x, y), self.target_radius, self.target_color, -1)
        cross_color = (0, 0, 0)
        thickness = 2
        cv2.line(frame, (x - self.CROSS_SIZE, y), (x + self.CROSS_SIZE, y), cross_color, thickness)
        cv2.line(frame, (x, y - self.CROSS_SIZE), (x, y + self.CROSS_SIZE), cross_color, thickness)

    def toggle_background(self):
        self.use_camera_background = not self.use_camera_background

    def destroy(self):
        cv2.destroyAllWindows()
