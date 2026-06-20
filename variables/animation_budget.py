#Declaring and assigning variable names
show_title = "Cyber-Knights"
episode_name = "The Awakening"
episode_length_minutes = 20
frames_per_second = 24
animator_hourly_rate = 35000.0
hours_to_animate_one_minute = 40

#Doing the math
total_seconds = 40*60
total_frames = total_seconds*frames_per_second
total_labor_hours = episode_length_minutes*hours_to_animate_one_minute
total_budget = total_labor_hours*animator_hourly_rate

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("\t STUDIO PRODUCTION DASHBOARD")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(f"Show: {show_title}")
print(f"Episode: {episode_name}\n")
print("--- ANIMATION REQUIREMENTS ---")
print(f"Duration: {episode_length_minutes} minutes")
print(f"Total Seconds: {total_seconds}")
print(f"Total Frames to Draw (at {frames_per_second} FPS): {total_frames} frames\n")
print("--- FINANCIAL BUDGET ---")
print(f"Estimated Labor: {total_labor_hours} hours")
print(f"Animator Rate: Ush{animator_hourly_rate}/hr\n")
print("====================================")
print(f"TOTAL EPISODE BUDGET: Ush{total_budget}")
print("====================================")


