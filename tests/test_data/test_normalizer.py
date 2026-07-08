import json

from placementiq.api import InternitoAPI
from placementiq.pipeline.normalizer import normalize_interview


def main():
    client = InternitoAPI()

    raw_interviews = client.fetch_interviews()

    normalized = normalize_interview(raw_interviews[0])

    print(json.dumps(normalized, indent=4))


if __name__ == "__main__":
    main()
