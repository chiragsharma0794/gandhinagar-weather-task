from statistics import mean, median

temps = [35, 35, 33, 34, 34, 35, 36, 36, 37, 38]
humidity = [40, 42, 38, 41, 39, 43, 45, 44, 46, 48]
aqi = [110, 105, 98, 102, 115, 120, 108, 112, 125, 118]

print("Average Temp:", mean(temps))
print("Median Temp:", median(temps))

print("Average Humidity:", mean(humidity))
print("Median Humidity:", median(humidity))

print("Average AQI:", mean(aqi))
print("Median AQI:", median(aqi))
