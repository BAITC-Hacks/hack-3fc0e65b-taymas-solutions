#!/usr/bin/env python3
"""Классификатор обращений: категория + черновик ответа."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

CATEGORIES = ("справка", "жалоба", "другое")

# Правила: ключевые слова → категория. Порядок важен: первое совпадение побеждает.
RULES: list[tuple[str, tuple[str, ...]]] = [
    (
        "жалоба",
        (
            "очеред",
            "холодн",
            "пропал",
            "не работ",
            "сломал",
            "плохо",
            "ужас",
            "жалоб",
            "wi-fi",
            "wifi",
            "вайфай",
        ),
    ),
    (
        "справка",
        (
            "справк",
            "как получ",
            "где ",
            "парковк",
            "как найти",
            "как оформить",
            "документ",
            "аттестат",
        ),
    ),
]


@dataclass(frozen=True)
class Result:
    message: str
    category: str
    draft: str


def load_messages(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [line.strip() for line in text.splitlines() if line.strip()]


def classify(message: str) -> str:
    lower = message.lower()
    for category, keywords in RULES:
        if any(kw in lower for kw in keywords):
            return category
    return "другое"


def draft_reply(message: str, category: str) -> str:
    lower = message.lower()

    if category == "справка":
        if "учёб" in lower or "учеб" in lower or "справк" in lower:
            return (
                "Справку о месте учёбы можно получить в деканате "
                "или через личный кабинет студента (раздел «Справки»). "
                "Обычно готовность — 1–3 рабочих дня."
            )
        if "парков" in lower:
            return (
                "Гостевая парковка расположена у главного входа, "
                "въезд со стороны улицы Университетской. "
                "Нужно взять пропуск на охране."
            )
        return (
            "Спасибо за вопрос. Уточните, пожалуйста, детали — "
            "подскажем, куда обратиться и какие документы нужны."
        )

    if category == "жалоба":
        if "столов" in lower or "ед" in lower or "очеред" in lower:
            return (
                "Спасибо, что сообщили. Передадим замечание "
                "администрации столовой. Если есть фото или время инцидента — "
                "пришлите, это поможет разобраться быстрее."
            )
        if "wi-fi" in lower or "wifi" in lower or "вайфай" in lower:
            return (
                "Приняли обращение по Wi‑Fi. Техподдержка проверит "
                "точку доступа в указанном корпусе. "
                "Если удобно — напишите этаж и аудиторию."
            )
        return (
            "Жалоба зафиксирована. Мы передадим её ответственному "
            "отделу и вернёмся с ответом."
        )

    # другое
    if "консультац" in lower or "запис" in lower:
        return (
            "Запись на консультацию доступна в личном кабинете "
            "или у куратора. Напишите ФИО и удобное время — "
            "поможем подтвердить слот на завтра."
        )
    return (
        "Спасибо за обращение. Уточните, пожалуйста, "
        "чего именно нужно добиться — направим в нужный отдел."
    )


def process(messages: list[str]) -> list[Result]:
    results: list[Result] = []
    for msg in messages:
        category = classify(msg)
        results.append(
            Result(message=msg, category=category, draft=draft_reply(msg, category))
        )
    return results


def format_report(results: list[Result]) -> str:
    lines: list[str] = []
    lines.append("═" * 56)
    lines.append("  КЛАССИФИКАТОР ОБРАЩЕНИЙ")
    lines.append("═" * 56)

    for i, r in enumerate(results, start=1):
        lines.append("")
        lines.append(f"[{i}] {r.message}")
        lines.append(f"    категория : {r.category}")
        lines.append(f"    черновик  : {r.draft}")

    counts = {c: sum(1 for r in results if r.category == c) for c in CATEGORIES}
    lines.append("")
    lines.append("─" * 56)
    lines.append(
        "итог: "
        + ", ".join(f"{c} — {n}" for c, n in counts.items())
    )
    lines.append("═" * 56)
    return "\n".join(lines)


def main() -> None:
    path = Path(__file__).with_name("messages.txt")
    messages = load_messages(path)
    if not messages:
        raise SystemExit(f"Файл пуст: {path}")

    report = format_report(process(messages))
    print(report)


if __name__ == "__main__":
    main()
