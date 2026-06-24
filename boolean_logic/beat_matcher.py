bpm = int(input("Enter the track BPM: "))
vibe_rating = float(input("Enter the vibe rating (1-10): "))
is_perfect_match = bpm>=70 and bpm<=90 and bpm%2==0 and vibe_rating>8.0
print(f"\nIs this a perfect Lo-Fi match? {is_perfect_match}")


