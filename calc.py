import pandas as pd
import matplotlib.pyplot as plt

# Load the final weighted confidence files
low_df = pd.read_csv("final_weighted_confidence_low_beam.csv")
high_df = pd.read_csv("final_weighted_confidence_high_beam.csv")

# Apply threshold filter
low_filtered = low_df[low_df["Weighted Confidence"] >= 0.6].reset_index(drop=True)
high_filtered = high_df[high_df["Weighted Confidence"] >= 0.6].reset_index(drop=True)

# Load illumination files with "Video Name"
low_illum = pd.read_csv("Low_Light_with_Illumination_with_Video_Name.csv")
high_illum = pd.read_csv("High_Beam_with_Illumination_with_Video_Name.csv")

# Merge filtered data with illumination
low_merged = pd.merge(low_filtered, low_illum[["Video Name", "Illumination"]], on="Video Name", how="inner")
high_merged = pd.merge(high_filtered, high_illum[["Video Name", "Illumination"]], on="Video Name", how="inner")

# Sort for smoother line
low_merged = low_merged.sort_values(by="Illumination")
high_merged = high_merged.sort_values(by="Illumination")

# Plot
plt.figure(figsize=(14, 8))

# Plot lines with markers
plt.plot(low_merged["Illumination"], low_merged["Weighted Confidence"], label="Low Beam (Filtered)", color='blue', marker='o')
plt.plot(high_merged["Illumination"], high_merged["Weighted Confidence"], label="High Beam (Filtered)", color='orange', marker='s')

# Annotate each point with Video Name
for _, row in low_merged.iterrows():
    plt.annotate(row["Video Name"], (row["Illumination"], row["Weighted Confidence"]),
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='blue',
                 bbox=dict(facecolor='white', alpha=0.7, edgecolor='blue'))

for _, row in high_merged.iterrows():
    plt.annotate(row["Video Name"], (row["Illumination"], row["Weighted Confidence"]),
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='orange',
                 bbox=dict(facecolor='white', alpha=0.7, edgecolor='orange'))

# Threshold line
plt.axhline(y=0.5, color='red', linestyle='--', label='Threshold = 0.6')

plt.title("Thresholded Confidence vs Illumination")
plt.xlabel("Illumination")
plt.ylabel("Weighted Confidence")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.subplots_adjust(bottom=0.1, top=0.95)
plt.show()
