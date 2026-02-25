from statistics import mean, median

temps = [35, 35, 33, 34, 34, 35, 36, 36, 37, 38]
humidity = [40, 42, 38, 41, 39, 43, 45, 44, 46, 48]
aqi = [110, 105, 98, 102, 115, 120, 108, 112, 125, 118]

lines = []
lines.append(f"Average Temp: {mean(temps)}")
lines.append(f"Median Temp: {median(temps)}")
lines.append(f"Average Humidity: {mean(humidity)}")
lines.append(f"Median Humidity: {median(humidity)}")
lines.append(f"Average AQI: {mean(aqi)}")
lines.append(f"Median AQI: {median(aqi)}")

with open("results.txt", "w") as f:
    f.write("\n".join(lines))

print("Saved results to output.txt")