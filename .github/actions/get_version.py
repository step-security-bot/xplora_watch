import json
import sys


def main():
    with open("./custom_components/xplora_watch/manifest.json", encoding="utf8") as json_file:
        data = json.load(json_file)
        print(data["version"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
