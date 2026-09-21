# Фильтр алертов

Скрипт читает `events.json`, отбрасывает шум (`info` / `warn`)
и печатает только события с уровнем `critical`, затем итог: `критичных N`.

## Запуск

```bash
python3 filter.py
```

Нужен Python 3.10+. Зависимостей нет. Агенты и тулы не используются — обычный `filter`.

## Входные данные

В `events.json` — 8 событий из задания:

| message | level |
|---------|-------|
| disk 90% | critical |
| user login | info |
| cpu 40% | info |
| payment failed | critical |
| heartbeat | info |
| db timeout | critical |
| cache miss | warn |
| deploy ok | info |

## Ожидаемый вывод

```
disk 90% (critical)
payment failed (critical)
db timeout (critical)
критичных 3
```
