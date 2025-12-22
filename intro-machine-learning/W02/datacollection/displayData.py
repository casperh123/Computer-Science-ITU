import cv2
import os
import numpy as np
import json

def load_calibration_data(log_file_path):
    with open(log_file_path, 'r') as f:
        lines = f.readlines()

    video_file = None
    frames = []

    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            if "VideoFile" in line:
                video_file = line.split(': ')[-1]
            continue
        if not line or line.startswith("FrameNumber"):
            continue

        parts = line.split(',')
        if len(parts) < 4:
            continue

        try:
            frame_number = int(parts[0])
            timestamp = int(parts[1])
            target_x = float(parts[2])
            target_y = float(parts[3])
            frames.append((frame_number, timestamp, target_x, target_y))
        except ValueError:
            continue

    if video_file is None:
        raise ValueError("No video file name found in the log file.")

    return video_file, frames

def draw_target(frame, norm_x, norm_y, config):
    width = frame.shape[1]
    height = frame.shape[0]
    abs_x = int(norm_x * width)
    abs_y = int(norm_y * height)
    radius = config.get('target_radius', 30)
    target_color = tuple(config.get('target_color', (0, 0, 255)))
    cross_size = 10
    cross_color = (0, 0, 0)
    thickness = 2

    cv2.circle(frame, (abs_x, abs_y), radius, target_color, -1)
    cv2.line(frame, (abs_x - cross_size, abs_y), (abs_x + cross_size, abs_y), cross_color, thickness)
    cv2.line(frame, (abs_x, abs_y - cross_size), (abs_x, abs_y + cross_size), cross_color, thickness)

def draw_overlay(frame, frame_idx, total_frames, play_mode):
    text = f"Frame {frame_idx + 1} / {total_frames} — {'PLAY' if play_mode else 'PAUSE'}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    font_color = (0, 255, 0) if play_mode else (0, 0, 255)
    thickness = 2
    position = (30, 30)

    cv2.putText(frame, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)

def draw_instructions(frame):
    instructions = [
        "Controls:",
        "A: Back    D: Forward",
        "Space: Play/Pause",
        "ESC: Exit"
    ]
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.6
    font_color = (255, 255, 255)
    thickness = 1
    line_height = 30
    x, y_start = 30, 60

    for i, line in enumerate(instructions):
        y = y_start + i * line_height
        cv2.putText(frame, line, (x, y), font, font_scale, font_color, thickness, cv2.LINE_AA)

def load_video_to_memory(video_path):
    cap = cv2.VideoCapture(video_path)
    frames_memory = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames_memory.append(frame.copy())
    cap.release()
    print(f"Loaded {len(frames_memory)} frames into memory.")
    return frames_memory

def replay_step_by_step(log_filename, config_path='config.json'):
    with open(config_path, 'r') as f:
        config = json.load(f)

    save_dir = config.get('save_dir', 'Data')
    background_color = tuple(config.get('background_color', (255, 255, 255)))
    fps = config.get('fps', 30)

    log_path = os.path.join(save_dir, log_filename)

    if not os.path.isfile(log_path):
        print(f"Log file {log_path} does not exist.")
        return

    print(f"Using log file: {log_path}")

    video_file_from_log, frame_targets = load_calibration_data(log_path)
    video_path = os.path.join(save_dir, video_file_from_log)

    if not os.path.isfile(video_path):
        print(f"Video file {video_path} does not exist.")
        return

    frames_memory = load_video_to_memory(video_path)
    total_frames = len(frames_memory)

    if total_frames != len(frame_targets):
        print(f"Warning: Number of video frames ({total_frames}) and target frames ({len(frame_targets)}) do not match.")

    # Print Navigation Instructions
    print("\nNavigation Instructions:")
    print("A: Back    D: Forward")
    print("Space: Play/Pause")
    print("ESC: Exit\n")

    cv2.namedWindow('Video Replay', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Target Replay', cv2.WINDOW_NORMAL)

    frame_idx = 0
    play_mode = False  # Start paused

    while True:
        frame_idx = max(0, min(frame_idx, total_frames - 1))

        frame = frames_memory[frame_idx].copy()
        screen_height, screen_width = frame.shape[:2]

        target_frame = np.full((screen_height, screen_width, 3), background_color, dtype=np.uint8)
        _, _, norm_x, norm_y = frame_targets[frame_idx]
        draw_target(target_frame, norm_x, norm_y, config)

        draw_overlay(frame, frame_idx, total_frames, play_mode)
        draw_instructions(target_frame)

        cv2.imshow('Video Replay', frame)
        cv2.imshow('Target Replay', target_frame)

        # 🛠️ Key handling
        if play_mode:
            key = cv2.waitKey(int(1000 / fps)) & 0xFF  # 33ms for ~30fps
            frame_idx += 1  # auto-advance
        else:
            key = cv2.waitKey(0) & 0xFF  # wait for key

        if key == 27:  # ESC
            break
        elif key == ord(' '):  # Spacebar
            play_mode = not play_mode
            print("Play mode" if play_mode else "Paused")
        elif key == ord('a'):  # 'a' key for back
            frame_idx -= 1
        elif key == ord('d'):  # 'd' key for forward
            frame_idx += 1

    cv2.destroyAllWindows()

if __name__ == "__main__":
    log_filename = 'log_0604_2110.csv'
    replay_step_by_step(log_filename)
