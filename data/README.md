# Данные APL Insight

Файлы в этой папке:

- `stats.json` — локальный срез таблицы и календаря (standings + fixtures) на 5 февраля 2026 года.
- `stats.db` — SQLite база, сгенерированная из `stats.json` (не хранится в репозитории).
- `stats.sql` — SQL-дамп для импорта/проверки, если локальные инструменты не открывают `.db`.
- `seed_db.py` — скрипт для пересоздания базы.
- `fetch_stats.py` — загрузка реальных данных из StatsBomb Open Data и обновление `stats.json`.

## Как пересоздать базу данных

```bash
python data/seed_db.py
```

## Как обновить данные из StatsBomb Open Data

```bash
python data/fetch_stats.py
python data/seed_db.py
```

> Скрипт требует сетевого доступа. Если сеть недоступна, используется локальный срез.

## Проверка, что база открывается

```bash
sqlite3 data/stats.db ".tables"
sqlite3 data/stats.db "SELECT * FROM metadata;"
```

Если `.db` по каким-то причинам не открывается, можно импортировать `stats.sql`:

```bash
sqlite3 data/stats.db < data/stats.sql
```
