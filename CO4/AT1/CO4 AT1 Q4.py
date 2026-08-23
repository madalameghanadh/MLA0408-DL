# Q4 - LSTM and BPTT
# Stock Market Trend Prediction
# Simple Python Demonstration

print("=" * 60)
print("LSTM BASED STOCK MARKET TREND PREDICTION")
print("=" * 60)

# Historical stock data
# Format: Day, Open, High, Low, Close, Volume

stock_data = [
    [1, 100, 105, 98, 103, 5000],
    [2, 103, 108, 101, 106, 5200],
    [3, 106, 110, 104, 109, 5500],
    [4, 109, 112, 107, 108, 5300],
    [5, 108, 111, 105, 106, 5100],
    [6, 106, 109, 103, 104, 4900],
    [7, 104, 107, 101, 102, 4800],
    [8, 102, 106, 100, 105, 5200],
    [9, 105, 109, 103, 108, 5600],
    [10, 108, 113, 106, 111, 6000]
]

print("\n1. Historical Stock Data")
print("-" * 60)

for row in stock_data:
    print(
        "Day:", row[0],
        "Open:", row[1],
        "High:", row[2],
        "Low:", row[3],
        "Close:", row[4],
        "Volume:", row[5]
    )

# Create time-series sequences
time_steps = 3

print("\n2. Time-Series Window")
print("Previous", time_steps, "days are used to predict the next day.")

for i in range(len(stock_data) - time_steps):
    sequence = stock_data[i:i + time_steps]

    print("\nSequence:")
    for day in sequence:
        print("Day", day[0], "Closing Price =", day[4])

    next_day = stock_data[i + time_steps]

    if next_day[4] > sequence[-1][4]:
        trend = "UP"
    elif next_day[4] < sequence[-1][4]:
        trend = "DOWN"
    else:
        trend = "STABLE"

    print("Predicted Trend:", trend)

# LSTM architecture
print("\n3. LSTM Architecture")
print("-" * 60)

print("Input: Historical Stock Data")
print("       ↓")
print("Time-Series Sequence")
print("       ↓")
print("LSTM Layer")
print("       ↓")
print("Forget Gate")
print("       ↓")
print("Input Gate")
print("       ↓")
print("Cell State")
print("       ↓")
print("Output Gate")
print("       ↓")
print("Dense Layer")
print("       ↓")
print("Stock Trend")

# BPTT
print("\n4. Backpropagation Through Time (BPTT)")
print("-" * 60)

print("Forward Pass:")
print("Day 1 → Day 2 → Day 3 → Prediction")

print("\nBackward Pass:")
print("Prediction → Day 3 → Day 2 → Day 1")

print("\nBPTT calculates the error and updates")
print("the LSTM weights through all time steps.")

# LSTM advantages
print("\n5. Why LSTM is Preferred over Standard RNN")
print("-" * 60)

advantages = [
    "Stores important information for a long time",
    "Reduces the vanishing gradient problem",
    "Uses Forget, Input and Output gates",
    "Handles long-term dependencies",
    "Suitable for time-series prediction"
]

for i, advantage in enumerate(advantages, 1):
    print(i, ".", advantage)

# Final prediction
print("\n6. Final Stock Trend Prediction")
print("-" * 60)

last_close = stock_data[-1][4]
previous_close = stock_data[-2][4]

if last_close > previous_close:
    final_prediction = "UP"
elif last_close < previous_close:
    final_prediction = "DOWN"
else:
    final_prediction = "STABLE"

print("Previous Closing Price:", previous_close)
print("Latest Closing Price:", last_close)
print("Predicted Trend:", final_prediction)

print("\n" + "=" * 60)
print("LSTM STOCK TREND PREDICTION COMPLETED")
print("=" * 60)
