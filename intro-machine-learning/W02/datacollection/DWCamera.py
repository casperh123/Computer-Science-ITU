import cv2

class DWCamera:
    def __init__(self, config):
        self.cap = None
        self.width = config.get('screen_width', 1280)
        self.height = config.get('screen_height', 720)
        self.max_tested = config.get('max_tested', 10)

    def list_cameras(self):
        available = []
        for i in range(self.max_tested):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                available.append(i)
                cap.release()
            else:
                cap.release()
        return available

    def connect(self, index):
        available_cameras = self.list_cameras()
        if index not in available_cameras:
            print(f"Error: Camera index {index} is not available.")
            return False
        self.release()
        self.cap = cv2.VideoCapture(index)
        if not self.cap.isOpened():
            print(f"Error: Cannot open camera with index {index}")
            self.cap = None
            return False
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        return True

    def select_camera_from_list(self):
        cameras = self.list_cameras()
        if not cameras:
            print("No cameras found.")
            return False
        print("Available cameras:")
        for cam in cameras:
            print(f"Camera Index: {cam}")
        selected = input("Enter camera index: ")
        if selected.isdigit():
            return self.connect(int(selected))
        else:
            print("Invalid input.")
            return False

    def read(self):
        if self.cap is not None:
            return self.cap.read()
        return False, None

    def release(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def __del__(self):
        self.release()
