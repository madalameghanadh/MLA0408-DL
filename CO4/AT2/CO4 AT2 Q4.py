# Q4: LSTM and BPTT
# Stock Price Prediction
# Pure Python

import math

# Sigmoid function
def sigmoid(x):

    return 1 / (1 + math.exp(-x))


# Simulated historical stock prices
prices = [
    100,
    102,
    101,
    105,
    107,
    110,
    108,
    112
]

print("LSTM STOCK PRICE PREDICTION")
print("---------------------------")

print("\nHistorical Prices:")

for price in prices:
    print(price)


# Initial states
cell_state = 0
hidden_state = 0

print("\nLSTM Processing:")

for price in prices:

    # Normalize price
    x = price / 100

    # Forget gate
    forget_gate = sigmoid(
        x + hidden_state
    )

    # Input gate
    input_gate = sigmoid(
        x
    )

    # Candidate memory
    candidate = math.tanh(
        x
    )

    # Update cell state
    cell_state = (
        forget_gate * cell_state
        +
        input_gate * candidate
    )

    # Output gate
    output_gate = sigmoid(
        x
    )

    # Hidden state
    hidden_state = (
        output_gate *
        math.tanh(cell_state)
    )

    print(
        "Price:",
        price,
        "Hidden State:",
        round(hidden_state, 4)
    )


# Prediction
predicted_price = (
    100 + hidden_state * 10
)

print("\nPredicted Next Price:")
print(
    round(predicted_price, 2)
)

print("\nBPTT:")
print("The prediction error is propagated")
print("backward through previous time steps")
print("to update the LSTM weights.")
