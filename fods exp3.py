
import numpy as np

# Columns: Bedrooms, Square Footage, Sale Price
house_data = np.array([
    [3, 1500, 200000],
    [5, 2500, 350000],
    [6, 3000, 450000],
    [4, 1800, 250000],
    [5, 2200, 400000]
])

prices = house_data[house_data[:, 0] > 4, 2]

avg = np.mean(prices)

print("Average sale price:", avg)
