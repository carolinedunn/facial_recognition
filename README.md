# Facial Recognition on Raspberry Pi (2023+ Bookworm OS)


<img src="https://github.com/carolinedunn/facial_recognition/blob/main/photo/screenshot.png?raw=true" width="500"/>


Materials: Raspberry Pi 4 or 5 and Webcam

<img src="https://github.com/carolinedunn/facial_recognition/blob/main/photo/webcamandRPi4.JPG?raw=true" width="500"/>

This project walks you through setting up facial recognition on a Raspberry Pi using a virtual environment, OpenCV, and the `face-recognition` library. With the release of Bookworm OS, virtual environments are now required to avoid conflicts with system packages — but don’t worry, it’s quick and easy!

### 📦 Set Up Virtual Environment and Install Libraries

Open a terminal window and follow these steps:

```bash
# Create a virtual environment
python3 -m venv --system-site-packages face_rec

# Activate the virtual environment
source face_rec/bin/activate
```

Update your Raspberry Pi:

```bash
sudo apt update && sudo apt full-upgrade -y
```

Install required Python libraries:

```bash
pip install opencv-python
pip install imutils
pip install face-recognition
```

Install CMake (for compiling dependencies):

```bash
sudo apt install cmake -y
```

> 💡 If you ever exit the terminal, simply re-run `source face_rec/bin/activate` to reactivate your environment.

### 🧪 Configure Thonny to Use Virtual Environment

Open Thonny and set the interpreter to point to the `face_rec/bin/python3` inside your virtual environment so your code runs with the correct libraries.

### 📥 Download the Code

Clone this repository:

```bash
git clone https://github.com/carolinedunn/facial_recognition.git
```

Original Tutorial - https://www.tomshardware.com/how-to/raspberry-pi-facial-recognition


2025 Updated Tutorial from Core Electronics (this code has been expanded to include webcams) - https://core-electronics.com.au/guides/face-recognition-with-raspberry-pi-and-opencv/
