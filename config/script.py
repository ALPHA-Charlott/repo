import json
import sys

def main(config_path):
    with open(config_path, 'r') as file:
        config = json.load(file)
    print("Configuration Loaded:")
    print(config)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <config_path>")
        sys.exit(1)
    config_path = sys.argv[1]
    main(config_path)