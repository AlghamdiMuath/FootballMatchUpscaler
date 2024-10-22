# Football Match Video Upscaler

This project uses Real-ESRGAN to upscale low-quality Saudi football match videos, improving resolution and visual clarity using AI-based upscaling techniques.

## Features

- Extracts frames from video using OpenCV.
- Upscales frames using Real-ESRGAN.
- Reassembles frames back into a video (not implemented yet).
- Focused on producing high-quality output.

## Getting Started

### Prerequisites

Make sure you have Python 3.9 installed.

### Step-by-Step Setup Instructions (Terminal)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AlghamdiMuath/FootballMatchUpscaler.git
   cd FootballMatchUpscaler
2. Set up a virtual environment: Create a virtual environment to keep your dependencies organized.

   ```bash
    python -m venv env
3. Activate the virtual environment:
   ```bash
    .\env\Scripts\activate
4. Installing Real-ESRGAN
    1. Clone the Real-ESRGAN repository:
       ```bash
        git clone https://github.com/xinntao/Real-ESRGAN.git
    2. Install Real-ESRGAN dependencies
       ```bash
       cd Real-ESRGAN
       pip install -r requirements.txt
    3. Download the RealESRGAN_x4plus.pth model from the Real-ESRGAN GitHub.
    4. Save the model file inside the Real-ESRGAN/experiments/pretrained_models directory.
       
