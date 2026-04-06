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
            "Hip-Hop Fan (Genre-First)",
            {
                "favorite_genre": "pop",
                "favorite_mood": "energetic",
                "target_energy": 0.9,
                "likes_acoustic": False,
                "ranking_mode": "genre-first",
            },
        ),
        (
            "Acoustic Low-Energy Listener (Energy-First)",
            {
                "favorite_genre": "indie pop",
                "favorite_mood": "relaxed",
                "target_energy": 0.3,
                "likes_acoustic": True,
                "ranking_mode": "energy-first",
            },
        ),
        (
            "High-Tempo EDM Listener (Default)",
            {
                "favorite_genre": "synthwave",
                "favorite_mood": "upbeat",
                "target_energy": 0.95,
                "likes_acoustic": False,
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
        print(tabulate(table_data, headers=["Rank", "Title", "Artist", "Score", "Reason"], tablefmt="grid"))
        print()  # Blank line after table


if __name__ == "__main__":
    main()
