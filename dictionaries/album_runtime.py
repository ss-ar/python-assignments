ep_tracks = {"Intro":1.5,"Neon Nights":3.2,"Chill Vibes":4.0,"Outro":2.1}
total_runtime =0
for song,length in ep_tracks.items():
  print(f"Track: {song} - {length} mins")
  total_runtime+=length
print(f"Total Runtime: {total_runtime}")
