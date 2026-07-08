from placementiq.api import InternitoAPI
from placementiq.pipeline.normalizer import normalize_interview
from placementiq.pipeline.writer import write_interviews


def main():
    client = InternitoAPI()

    raw_interviews = client.fetch_interviews()

    normalized = [normalize_interview(interview) for interview in raw_interviews]

    write_interviews(normalized)

    print(f"Successfully wrote {len(normalized)} interviews.")


if __name__ == "__main__":
    main()
