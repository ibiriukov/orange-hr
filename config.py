import os

CONFIG = {
    "username": os.getenv("ORANGE_USERNAME", ""),
    "password": os.getenv("ORANGE_PASSWORD", ""),
    "base_url": os.getenv("ORANGE_BASE_URL", "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"),
}
