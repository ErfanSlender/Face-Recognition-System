from pathlib import Path

# Main Project Path
BASE_DIR = Path(__file__).resolve().parent

# Face Images Path
KNOWN_DIR = BASE_DIR / 'known'

# Data Base Path
DATABASE_PATH = BASE_DIR / 'face_logs.db'

# Time interval for re-registration of each individual
LOG_INTERVAL = 30

# Facial recognition sensitivity level
TOLERANCE = 0.5
 
# Camera number
CAMERA_INDEX = 0 