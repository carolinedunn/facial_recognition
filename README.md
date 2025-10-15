# Facial Recognition on Raspberry Pi 2025

<img src="https://github.com/carolinedunn/facial_recognition/blob/main/photo/CandP.png?raw=true" width="500"/>


Materials: Raspberry Pi 4 or 5 and Webcam

<img src="https://github.com/carolinedunn/facial_recognition/blob/main/photo/RPi5+webcam.jpg?raw=true" width="500"/>

This project walks you through setting up facial recognition on a Raspberry Pi using a virtual environment, OpenCV, and the `face-recognition` library. With the release of Bookworm OS, virtual environments are now required to avoid conflicts with system packages — but don’t worry, it’s quick and easy!

## [Watch the Tutorial on YouTube - Face Rec on RPi](https://youtu.be/XNSSbSJ4lB4)

### Set Up Virtual Environment and Install Libraries

Open a terminal window and follow these steps:

Create a virtual environment
```bash
python3 -m venv --system-site-packages face_rec
```

Activate the virtual environment
```bash
source face_rec/bin/activate
```

Update your Raspberry Pi:

```bash
sudo apt update && sudo apt full-upgrade -y
```

### Add Swap Memory (Recommended First Step)

The Raspberry Pi doesn’t have enough memory to compile dlib. Add swap space to avoid memory crashes during compilation:

Open the dphys-swapfile config
```bash
sudo nano /etc/dphys-swapfile
```

Find the line:

```ini
CONF_SWAPSIZE=512
```

Change it to:

```ini
CONF_SWAPSIZE=2048
```

Save and exit (`CTRL+X`, then `Y`, then `Enter`), then restart the swap service:

```bash
sudo systemctl restart dphys-swapfile
```

### Install Required Python Libraries

```bash
pip install opencv-python
```

```bash
pip install imutils
```
Install CMake (for compiling dependencies):

```bash
sudo apt install cmake -y
```

Installing face recognition will take anywhere from 10 minutes to an hour.

```bash
pip install face-recognition
```

> Once you're done with installation, it's a good idea to **change the swap size back to reduce SD card wear**:

```bash
sudo nano /etc/dphys-swapfile
```

Change:

```ini
CONF_SWAPSIZE=2048
```
Back to:

```ini
CONF_SWAPSIZE=512
```

Then restart the service:

```bash
sudo systemctl restart dphys-swapfile
```

> If you ever exit the terminal, simply re-run `source face_rec/bin/activate` to reactivate your environment.



### Download the Code

Clone this repository:

```bash
git clone https://github.com/carolinedunn/facial_recognition.git
```
Change into the directory:

```bash
cd facial_recognition
```

Delete the sample directory:

```bash
rm -r dataset/Z
```

## Take Headshots

If using a webcam, first modify the code with the person’s name in the dataset directory:

```bash
nano headshots_capture-webcam.py
```

If using a Pi Camera:

```bash
nano headshots_capture-picam.py
```

Change line 7 of the file replacing YOUR_NAME:

```python
PERSON_NAME = "YOUR_NAME"
```

Save and exit by pressing `Ctrl+X`, then `Y`, and hit `Enter`.

Now run the script for the webcam:

```bash
python3 headshots_capture-webcam.py
```

Here's the command if using a Pi Camera:

```bash
python3 headshots_capture-picam.py
```

Look at the camera and press the **spacebar** to take photos. Move your head around and take at least 10 photos.

Press `q` to exit. Repeat this for each person.

You should now see a folder for each person with a set of headshots.

## Train the Model

```bash
python3 model_training.py
```

If successful, you will get a `.pickle` file.

## Run the Facial Recognition Test

If using a webcam:

```bash
python3 face_rec-webcam.py
```

If using a Pi Camera:

```bash
python3 face_rec-picam.py
```

Press `q` to exit. 


Original Tutorial - https://www.tomshardware.com/how-to/raspberry-pi-facial-recognition  \
Updated Code from Core Electronics - https://core-electronics.com.au/guides/face-recognition-with-raspberry-pi-and-opencv/

---

## 📚 Author
Created by **Caroline Dunn**  
- 🌐 [winningintech.com](https://winningintech.com/)  
- 📺 [YouTube.com/Caroline](https://www.youtube.com/caroline)  
- 📘 [A Woman’s Guide to Winning in Tech](https://amzn.to/3YxHVO7)  
