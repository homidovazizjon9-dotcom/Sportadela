import json
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = BASE_DIR / "stats.json"

COMPETITIONS_URL = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/competitions.json"
MATCHES_URL = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/matches/{competition_id}/{season_id}.json"


def load_json(url: str):
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def pick_latest_pl_season(competitions):
    pl = [
        comp
        for comp in competitions
        if comp.get("competition_name") == "Premier League"
    ]
    if not pl:
        raise RuntimeError("Premier League competition not found in StatsBomb data.")
    pl.sort(key=lambda c: (c.get("season_start_date") or ""), reverse=True)
    return pl[0]


def build_standings(matches):
    table = {}
    for match in matches:
        home = match["home_team"]["home_team_name"]
        away = match["away_team"]["away_team_name"]
        home_score = match.get("home_score")
        away_score = match.get("away_score")
        if home_score is None or away_score is None:
            continue
        for team in (home, away):
            if team not in table:
                table[team] = {
                    "team": team,
                    "played": 0,
                    "wins": 0,
                    "draws": 0,
                    "losses": 0,
                    "goals_for": 0,
                    "goals_against": 0,
                    "points": 0,
                }
        home_row = table[home]
        away_row = table[away]
        home_row["played"] += 1
        away_row["played"] += 1
        home_row["goals_for"] += home_score
        home_row["goals_against"] += away_score
        away_row["goals_for"] += away_score
        away_row["goals_against"] += home_score
        if home_score > away_score:
            home_row["wins"] += 1
            home_row["points"] += 3
            away_row["losses"] += 1
        elif home_score < away_score:
            away_row["wins"] += 1
            away_row["points"] += 3
            home_row["losses"] += 1
        else:
            home_row["draws"] += 1
            away_row["draws"] += 1
            home_row["points"] += 1
            away_row["points"] += 1
    standings = sorted(
        table.values(),
        key=lambda r: (r["points"], r["goals_for"] - r["goals_against"], r["goals_for"]),
        reverse=True,
    )
    for idx, row in enumerate(standings, start=1):
        row["position"] = idx
        row["form"] = ""
    return standings


def build_fixtures(matches):
    fixtures = []
    for match in sorted(matches, key=lambda m: (m.get("match_date") or "", m.get("kick_off") or "")):
        date = match.get("match_date")
        time = match.get("kick_off") or ""
        home = match["home_team"]["home_team_name"]
        away = match["away_team"]["away_team_name"]
        venue = match.get("venue") or ""
        status = "Завершен" if match.get("home_score") is not None else "Не начался"
        fixtures.append(
            {
                "date": date,
                "time": time[:5] if time else "",
                "home": home,
                "away": away,
                "venue": venue,
                "status": status,
            }
        )
    return fixtures[-10:]


def main():
    competitions = load_json(COMPETITIONS_URL)
    season = pick_latest_pl_season(competitions)
    matches = load_json(
        MATCHES_URL.format(
            competition_id=season["competition_id"],
            season_id=season["season_id"],
        )
    )
    standings = build_standings(matches)
    fixtures = build_fixtures(matches)
    payload = {
        "source": "StatsBomb Open Data",
        "as_of": datetime.utcnow().strftime("%Y-%m-%d"),
        "season": season.get("season_name"),
        "standings": standings,
        "fixtures": fixtures,
    }
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
