#!/usr/bin/env python3
"""Фильтр алертов: оставляет только critical-события."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_events(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("events.json должен содержать массив событий")
    return data


def critical_only(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [e for e in events if e.get("level") == "critical"]


def main() -> None:
    path = Path(__file__).with_name("events.json")
    events = load_events(path)
    critical = critical_only(events)

    for event in critical:
        msg = event.get("message", "")
        print(f"{msg} (critical)")

    print(f"критичных {len(critical)}")


if __name__ == "__main__":
    main()
