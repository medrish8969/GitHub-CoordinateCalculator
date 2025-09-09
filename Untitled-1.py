x = input("Please enter a coordinate in DDMMSS format: 449027")
type(x)
degrees = int(x[0:2])
minutes = int(x[2:4])
seconds = int(x[4:6])
print("Degrees:", degrees, "Minutes:", minutes, "Seconds:", seconds)
decimal_degrees = degrees + minutes/60 + seconds/3600
decimal_degrees = round(decimal_degrees, 2)
print("Your final result is:", decimal_degrees, "degrees")


