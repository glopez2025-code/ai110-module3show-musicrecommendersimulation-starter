import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initialize the Recommender with a list of songs."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        if not self.songs:
            raise ValueError("No songs available for recommendation")

        song_dicts = [vars(song) for song in self.songs]
        user_prefs = {
            'favorite_genre': user.favorite_genre,
            'favorite_mood': user.favorite_mood,
            'target_energy': user.target_energy,
            'likes_acoustic': user.likes_acoustic,
        }

        ranked = recommend_songs(user_prefs, song_dicts, k=k)
        return [Song(**song_dict) for song_dict, _, _ in ranked]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        genre_match = song.genre == user.favorite_genre
        mood_match = song.mood == user.favorite_mood
        energy_closeness = 1.0 - abs(song.energy - user.target_energy)
        acoustic_target = 1.0 if user.likes_acoustic else 0.0
        acoustic_closeness = 1.0 - abs(song.acousticness - acoustic_target)

        return (
            f"Recommended because genre={'matches' if genre_match else 'differs'} the preferred genre, "
            f"mood={'matches' if mood_match else 'differs'} the preferred mood, "
            f"energy closeness={energy_closeness:.2f}, "
            f"acousticness closeness={acoustic_closeness:.2f}."
        )

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    try:
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            songs: List[Dict] = []
            for row in reader:
                songs.append({
                    'id': int(row['id']),
                    'title': row['title'],
                    'artist': row['artist'],
                    'genre': row['genre'],
                    'mood': row['mood'],
                    'energy': float(row['energy']),
                    'tempo_bpm': float(row['tempo_bpm']),
                    'valence': float(row['valence']),
                    'danceability': float(row['danceability']),
                    'acousticness': float(row['acousticness']),
                })
            return songs
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Song file not found: {csv_path}") from exc


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5, ranking_mode: str = "default") -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    if not songs:
        raise ValueError("Songs list must not be empty")

    want_acoustic = 1.0 if user_prefs.get('likes_acoustic', False) else 0.0
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        genre_score = 1.0 if song.get('genre') == user_prefs.get('favorite_genre') else 0.0
        mood_score = 1.0 if song.get('mood') == user_prefs.get('favorite_mood') else 0.0
        energy_score = 1.0 - abs(song.get('energy', 0.0) - float(user_prefs.get('target_energy', 0.0)))
        acoustic_score = 1.0 - abs(song.get('acousticness', 0.0) - want_acoustic)

        # Adjust weights based on ranking mode
        if ranking_mode == "genre-first":
            genre_weight = 0.6
            mood_weight = 0.25
            energy_weight = 0.25
            acoustic_weight = 0.2
        elif ranking_mode == "energy-first":
            genre_weight = 0.3
            mood_weight = 0.25
            energy_weight = 0.5
            acoustic_weight = 0.2
        else:  # default
            genre_weight = 0.3
            mood_weight = 0.25
            energy_weight = 0.25
            acoustic_weight = 0.2

        score = (
            genre_weight * genre_score
            + mood_weight * mood_score
            + energy_weight * energy_score
            + acoustic_weight * acoustic_score
        )

        explanation = (
            f"genre_match={genre_score:.1f}, mood_match={mood_score:.1f}, "
            f"energy_closeness={energy_score:.2f}, acousticness_closeness={acoustic_score:.2f}"
        )
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)

    # Apply artist penalty to prevent duplicates in top k
    selected: List[Tuple[Dict, float, str]] = []
    seen_artists = set()
    for song, score, explanation in scored_songs:
        artist = song.get('artist')
        if artist not in seen_artists:
            selected.append((song, score, explanation))
            seen_artists.add(artist)
        else:
            # Penalize additional songs by the same artist
            penalized_score = score - 0.2
            selected.append((song, penalized_score, explanation + " (artist penalty applied)"))
            # Note: We add even if penalized to ensure we reach k results

        if len(selected) == k:
            break

    return selected
