import os
import dj_database_url

# Function to load environment variables from the .env file
def load_env():
    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ.setdefault(key, value)
    except FileNotFoundError:
        print("No .env file found. Environment variables are not loaded.")

# Load environment variables
load_env()

# Database settings
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}

# Secret key
SECRET_KEY = 'f1e+eese09-c447@zmhsdnap=cdti1r9ujk2_4apmqh75@t+m+'