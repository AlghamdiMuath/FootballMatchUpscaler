import cv2
import os
def reassemble_video(input_dir, output_video_path, fps=30):
    frames = sorted([f for f in os.listdir(input_dir) if f.endswith('.png')])
    frame = cv2.imread(os.path.join(input_dir, frames[0]))
    height, width, _ = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for frame_file in frames:
        frame_path = os.path.join(input_dir, frame_file)
        frame = cv2.imread(frame_path)
        out.write(frame)

    out.release()
    print(f"Video saved to {output_video_path}")

if __name__ == "__main__":
    input_dir = 'upscaled_frames'
    output_video_path = 'upscaled_video.mp4'
    reassemble_video(input_dir, output_video_path)
