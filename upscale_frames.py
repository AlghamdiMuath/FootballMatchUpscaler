import os
import subprocess

def upscale_frames(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    frames = sorted([f for f in os.listdir(input_dir) if f.endswith('.png')])

    for frame in frames:
        input_frame = os.path.join(input_dir, frame)
        output_frame = os.path.join(output_dir, frame)
        
        # Run Real-ESRGAN model (assuming it's set up as a Python script)
        command = f"python inference_realesrgan.py -i {input_frame} -o {output_frame} -n RealESRGAN_x4plus"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    input_dir = 'frames'
    output_dir = 'upscaled_frames'
    upscale_frames(input_dir, output_dir)
