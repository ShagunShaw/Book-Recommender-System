import gdown
import os

url = "https://drive.google.com/uc?id=YOUR_FILE_ID"
output = "sim.npy"

# Only download if not already present
if not os.path.exists(output):
    print("Downloading sim.npy from Google Drive...")
    gdown.download(url, output, quiet=False)
