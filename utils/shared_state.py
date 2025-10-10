import json
import os

TEMP_FILE = "temp_shared_state.json"

def save_value(key: str, value: str, filename: str = TEMP_FILE) -> None:
    data = {}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass
    data[key] = value
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_value(key: str, filename: str = TEMP_FILE) -> str | None:
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as f:
        try:
            data = json.load(f)
            return data.get(key)
        except json.JSONDecodeError:
            return None
