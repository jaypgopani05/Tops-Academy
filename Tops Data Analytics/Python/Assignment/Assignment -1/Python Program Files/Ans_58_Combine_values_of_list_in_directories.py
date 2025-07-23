# Sample data (as provided in your question)
# [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# Import the Counter class from collections module
from collections import Counter

# Create a list of dictionaries with 'item' and 'amount' keys
data = [
    {'item': 'item1', 'amount': 400},   # First dictionary
    {'item': 'item2', 'amount': 300},   # Second dictionary
    {'item': 'item1', 'amount': 750}    # Third dictionary (same item as first)
]

# Create an empty Counter to store the total amount for each item
result = Counter()

# Loop through each dictionary in the list
for d in data:
    item = d['item']         # Get the 'item' value from the dictionary
    amount = d['amount']     # Get the 'amount' value from the dictionary
    result[item] += amount   # Add the amount to the total for that item

# Display the combined result as a dictionary inside a Counter format
print("✅ Combined totals:")
print("Counter(", dict(result), ")")   # Convert Counter to dict for clean display
