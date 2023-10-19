import matplotlib.pyplot as plt

# Read data from the JSON file
with open('Lautsprecher_Data.JSON', 'r') as file:
    data = json.load(file)

# Extract PriceIDR and Preference Scores from the data
price_idr = [float(entry["PriceIDR"]) for entry in data[0]["Active Loudspeaker Data"] if entry["PriceIDR"]]
pref_scores = [float(entry["PrefScore"]) for entry in data[0]["Active Loudspeaker Data"] if entry["PriceIDR"]]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(price_idr, pref_scores, marker='o', alpha=0.7)

# Labeling the axes and title
plt.xlabel("Price (IDR)")
plt.ylabel("Preference Scores")
plt.title("Price vs. Preference Scores for Active Loudspeakers")

# Show the plot
plt.show()
