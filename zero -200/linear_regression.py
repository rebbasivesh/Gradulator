temperature = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
voltage = [1.2, 1.8, 2.5, 3.1, 3.7, 4.2, 4.7, 5.0, 5.3, 5.6]


m = ((voltage[-1,] - voltage[0]) / (temperature[-1] - temperature[0]))
c = voltage[0] - m * temperature[0]

print(f"Slope (m): {m:.5f}")
print(f"Intercept (c): {c:.5f}")

new_temp = 35
predicted_voltage = m * new_temp + c
print(f"Predicted voltage at {new_temp}°C: {predicted_voltage:.2f}")
