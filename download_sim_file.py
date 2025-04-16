import gdown
import os

url = "https://drive.google.com/uc?id=1eTn9zpN5yWyT0PIzBmZIXnNZMX534ZC0"
output = "sim.npy"

# Only download if not already present
if not os.path.exists(output):
    print("Downloading sim.npy from Google Drive...")
    gdown.download(url, output, quiet=False)
