Destination = input("Enter your destination address: ")
Distance = float(input("Enter the distance in kilometer: "))
Speed = float(input("Enter your speed in Km/h: "))

time = Distance/Speed
hour = int(time)
minute = int((time-hour)*60)

print(f"Destination: {Destination}\nDistance: {Distance}\nAverage Speed: {Speed}\n\nEstimated Travel Time: {hour} hours and {minute} minute")
