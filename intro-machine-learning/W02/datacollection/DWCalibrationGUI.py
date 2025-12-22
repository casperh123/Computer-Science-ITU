CROSS_SIZE = 5
import cv2
import numpy as np

class DWCalibrationGUI:
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
        cv2.line(frame, (x - CROSS_SIZE, y), (x + CROSS_SIZE, y), cross_color, thickness)
        cv2.line(frame, (x, y - CROSS_SIZE), (x, y + CROSS_SIZE), cross_color, thickness)

    def toggle_background(self):
        self.use_camera_background = not self.use_camera_background

    def destroy(self):
        cv2.destroyAllWindows()
