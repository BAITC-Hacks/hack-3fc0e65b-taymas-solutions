import json
from pathlib import Path


def main() -> None:
    events_path = Path(__file__).resolve().parent / "events.json"
    with events_path.open("r", encoding="utf-8") as file:
        events = json.load(file)

    critical_events = [event for event in events if event.get("level") == "critical"]

    for event in critical_events:
        print(f"{event['name']} ({event['level']})")

    print(f"критичных {len(critical_events)}")


if __name__ == "__main__":
    main()
