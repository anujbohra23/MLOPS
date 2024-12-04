from pathlib import Path

# Go up two levels from the current file's directory to reach the root directory
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Define the paths relative to the root directory
CONFIG_FILE_PATH = ROOT_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"

print("Root directory:", ROOT_DIR)
print("Config file path:", CONFIG_FILE_PATH)
print("Params file path:", PARAMS_FILE_PATH)
print("Config file exists:", CONFIG_FILE_PATH.exists())
print("Params file exists:", PARAMS_FILE_PATH.exists())
