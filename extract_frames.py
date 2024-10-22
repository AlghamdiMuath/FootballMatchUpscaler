import cv2
import os

def extract_frames(video_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_dir, f'frame_{frame_count:04d}.png')
        cv2.imwrite(frame_path, frame)
        frame_count += 1
    cap.release()
    print(f"Extracted {frame_count} frames.")

if __name__ == "__main__":
    video_path = 'path_to_your_video.mp4'
    output_dir = 'frames'
    extract_frames(video_path, output_dir)
