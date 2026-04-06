# 🎵 Music Recommender Simulation

## Project Summary

I built a simple content-based music recommender in Python. It takes a user's 
preferences — like their favorite genre, mood, and energy level — and scores 
every song in the catalog based on how close it is to those preferences. The 
top scoring songs get returned as recommendations. I also added an artist 
penalty to keep results diverse, and multiple ranking modes so you can 
prioritize genre or energy differently.

---

## How The System Works

Real world apps like Spotify look at your listening habits and what a song 
sounds like to guess what you'll want to hear next. My version does something 
similar but simpler — it takes what a user likes (genre, mood, energy, etc.) 
and compares it to each song. Every song gets a score based on how close it 
is to those preferences, then they get sorted and the best ones come out on top.

**Song attributes:** genre, mood, energy, tempo_bpm, valence, danceability, acousticness

**UserProfile stores:** preferred genre, preferred mood, target energy, target tempo

**Scoring:** each feature gets scored with 1 - |song_value - target_value|, 
then weighted and added up. Closer to what the user wants = higher score.

**Ranking:** sorted highest to lowest score, top results get recommended.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

- Tested 3 different user profiles: a hip-hop fan, an acoustic low-energy 
  listener, and a high-tempo EDM listener — each returned very different results
- Added an artist penalty so the same artist doesn't dominate the top 5
- Tried genre-first and energy-first ranking modes and noticed genre-first 
  pushed pop songs much higher for the hip-hop profile
- EDM profile strongly favored synthwave songs when genre matched

---
### Terminal Output Screenshots






## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

Building this made it clear how much a recommender's output depends on what 
you decide to weight. Just changing the genre weight completely shifted the 
results. It also showed how easy it is for a system like this to create a 
filter bubble — if someone only likes chill lofi, that's basically all they'll 
ever see. Real apps like Spotify have the same problem at a much bigger scale, 
and that's where human judgment still matters for things like introducing 
variety or catching when the algorithm is being unfair.