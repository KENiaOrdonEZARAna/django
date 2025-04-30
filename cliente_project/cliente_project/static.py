import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

