artist_name = "The Midnight Echo"
album_name = "Neon Dreams"
track1_streams = 150000
track2_streams = 350000
pay_per_stream = 0.004
studio_fee = 450.0

#Calculations
total_streams = track1_streams + track2_streams
gross_revenue = total_streams * pay_per_stream
net_profit = gross_revenue - studio_fee

print("#####################################")
print("\t BEAT-STREAM ANALYTICS")
print("##################################### \n")
print(f"Artist: {artist_name}")
print(f"Album: {album_name}\n")
print("--- STREAMING DATA ---")
print(f"Track 1 (Intro): {track1_streams} plays")
print(f"Track 2 (Starlight): {track2_streams} plays")
print(f">> Total Streams: {total_streams}\n")
print("--- REVENUE CALCULATIONS ---")
print(f"Gross Revenue (${pay_per_stream}/stream): ${gross_revenue}")
print(f"Studio Recording Fee: ${studio_fee}\n")
print("========================================")
print(f"FINAL ARTIST PAYOUT: ${net_profit}")
print("========================================")

