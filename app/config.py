import os
from dotenv import load_dotenv

load_dotenv()

MIKROTIK_HOST = os.getenv("MIKROTIK_HOST", "192.168.88.1")
MIKROTIK_PORT = int(os.getenv("MIKROTIK_PORT", "8728"))
MIKROTIK_USERNAME = os.getenv("MIKROTIK_USERNAME", "admin")
MIKROTIK_PASSWORD = os.getenv("MIKROTIK_PASSWORD", "")
MIKROTIK_USE_SSL = os.getenv("MIKROTIK_USE_SSL", "false").lower() == "true"
