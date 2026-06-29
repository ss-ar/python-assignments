episode_length = [24,25,22,24,26,23]
total_minutes = 0
average_length = 0
for minutes in episode_length:
  total_minutes+=minutes
  average_length=total_minutes/len(episode_length)

print(f"Total time watched: {total_minutes} minutes")
print(f"Average episode length: {average_length} minutes")

