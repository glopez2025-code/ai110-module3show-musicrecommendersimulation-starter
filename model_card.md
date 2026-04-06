# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name
VibeFinder 1.0

---

## 2. Intended Use
This recommender suggests songs from a small catalog based on a user's preferred 
genre, mood, energy level, and whether they like acoustic music. It's built for 
classroom exploration — not for real users or production use.

---

## 3. How the Model Works
Every song gets a score based on how close it is to what the user wants. Genre 
and mood are either a match or they're not. Energy and acousticness get scored 
by how close the song's value is to the user's target — the closer, the higher 
the score. Each feature has a weight, and they all get added up. Songs are then 
sorted from highest to lowest score and the top results come back as 
recommendations. I also added an artist penalty so the same artist doesn't show 
up too many times, and two extra ranking modes that shift the weights toward 
genre or energy depending on what the user cares about more.

---

## 4. Data
The catalog has 20 songs across genres like pop, lofi, rock, ambient, jazz, 
synthwave, and indie pop. Moods include happy, chill, intense, relaxed, focused, 
moody, and dreamy. I expanded the original 10-song starter dataset to 20 to get 
better coverage. Some genres like jazz and synthwave are still underrepresented, 
and there's nothing covering hip-hop, R&B, or country.

---

## 5. Strengths
Works well for users whose preferences align cleanly with the dataset — like a 
pop/happy/high-energy profile. The scoring is transparent and easy to understand. 
The artist penalty helps keep results varied. The EDM profile in particular 
returned results that felt accurate — synthwave songs with high energy scored 
at the top exactly as expected.

---

## 6. Limitations and Bias
- Genre matching is exact — "indie" won't match "indie pop"
- Dataset is small and leans toward pop and lofi, so those genres dominate
- Low-energy users get weaker matches because most songs in the catalog are 
  mid-to-high energy
- The system has no concept of tempo ranges, lyrics, or listening history
- Genre weight is highest (0.3), so genre mismatches hurt more than anything else
- Could create filter bubbles — if you like chill ambient, that's mostly all 
  you'll ever see

---

## 7. Evaluation
Tested 6 user profiles total — 3 normal and 3 adversarial edge cases. Normal 
profiles (hip-hop fan, acoustic listener, EDM listener) returned results that 
made sense. The adversarial profiles exposed real weaknesses — the mood-energy 
mismatch profile asked for chill rock but got intense rock songs because genre 
and energy outweighed mood. Also ran a weight shift experiment doubling energy 
and halving genre, which changed rankings noticeably and confirmed how sensitive 
the system is to weight choices.

---

## 8. Future Work
- Add fuzzy genre/mood matching so similar genres still get partial credit
- Let users set their own weights instead of using fixed ones
- Expand the dataset with more diverse genres and moods
- Add a "surprise me" mode that occasionally recommends something outside the 
  user's usual preferences to avoid filter bubbles
- Pull in real data from the Spotify API for a bigger, more realistic catalog

---

## 9. Personal Reflection
Building this made me realize how much of a recommender's output comes down to 
decisions the developer makes — what to weight, what to include, what to ignore. 
Those choices have real consequences. It also surprised me how a system this 
simple can still feel somewhat accurate. The EDM profile nailing synthwave songs 
felt almost like magic, even though it's just math. It changed how I think about 
apps like Spotify — there's way more going on under the hood, but the core idea 
isn't that different from what I built here.