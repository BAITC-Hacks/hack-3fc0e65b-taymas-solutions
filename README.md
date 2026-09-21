# Taymas Solutions — репетиция HackAlem AI

Решения задач трека **«Агентные системы»** (репетиция).

Стек: Python 3.10+, только стандартная библиотека.

| Задача | Запуск |
|--------|--------|
| Классификатор обращений | `python3 classifier.py` или `python3 classifier/classify.py` |
| Фильтр алертов | `python3 main.py` или `python3 alerts/filter.py` |

---

## 1. Классификатор обращений

Читает `messages.txt` (5 сообщений). Для каждого выводит:
- **категорию**: справка / жалоба / другое
- **черновик ответа** на русском

Классификация — правила по ключевым словам (без LLM).

```bash
python3 classifier.py
# или
python3 classifier/classify.py
```

---

## 2. Фильтр алертов

Читает `events.json` (8 событий с уровнями `info` / `warn` / `critical`).
Печатает только critical и строку `критичных N`.

```bash
python3 main.py
# или
python3 alerts/filter.py
```

Ожидаемый вывод:

```
disk 90% (critical)
payment failed (critical)
db timeout (critical)
критичных 3
```
