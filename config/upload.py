import os
from dotenv import load_dotenv
load_dotenv()

class Upload:
    UPLOAD_FOLDER = os.getenv('UPLOADED_IMAGES_DEST')
