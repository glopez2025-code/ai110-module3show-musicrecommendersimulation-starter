"""
Command line runner for the Music Recommender Simulation.
"""

from pathlib import Path
from tabulate import tabulate
from recommender import load_songs, recommend_songs


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    songs_path = script_dir.parent / "data" / "songs.csv"

    try:
        songs = load_songs(str(songs_path))
    except FileNotFoundError as exc:
        print(exc)
        return

    profiles = [
        (
            "High Energy + Acoustic",
            {
                "favorite_genre": "pop",
                "favorite_mood": "happy",
                "target_energy": 0.9,
                "likes_acoustic": True,
                "ranking_mode": "default",
            },
        ),
        (
            "Mood-Energy Mismatch",
            {
                "favorite_genre": "rock",
                "favorite_mood": "chill",
                "target_energy": 0.95,
                "likes_acoustic": False,
                "ranking_mode": "default",
            },
        ),
        (
            "Niche Genre Conflict",
            {
                "favorite_genre": "ambient",
                "favorite_mood": "intense",
                "target_energy": 0.1,
                "likes_acoustic": True,
                "ranking_mode": "default",
            },
        ),
    ]

    for label, user_prefs in profiles:
        ranking_mode = user_prefs.get('ranking_mode', 'default')
        recommendations = recommend_songs(user_prefs, songs, k=5, ranking_mode=ranking_mode)

        table_data = []
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            table_data.append([
                rank,
                song['title'],
                song['artist'],
                f"{score:.2f}",
                explanation,
            ])

        print()  # Blank line before label
        print(f"=== {label} ===")
        print()  # Blank line after label
        print(tabulate(table_data, headers=["Rank", "Title", "Artist", "Score", "Reason"], tablefmt="grid"), flush=True)
        print()  # Blank line after table


if __name__ == "__main__":
    main()
