from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()

# Configure for preview
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

# Start preview
picam2.start_preview(Preview.QTGL)

# Start camera
picam2.start()
# Wait for a short period
time.sleep(2)
