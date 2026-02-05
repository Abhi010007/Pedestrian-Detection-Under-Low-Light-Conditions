import pandas as pd
import matplotlib.pyplot as plt

# Load the confidence and high beam illumination data
confidence_df = pd.read_csv("final_weighted_confidence_high_beam.csv")
high_beam_df = pd.read_csv("High_Beam_with_Illumination_with_Video_Name.csv")

# Fix 'Video Name' to match confidence format
high_beam_df["Video Name"] = (
    high_beam_df["Row"].str.replace(" ", "") + "_" +
    high_beam_df["Position"].str.replace(" ", "").str.replace("Position", "Pos") +
    ".mp4"
)

# Merge the datasets
merged_df = pd.merge(confidence_df, high_beam_df[["Video Name", "Illumination"]], on="Video Name", how="inner")

# Sort by illumination to make the line smooth
merged_df = merged_df.sort_values(by="Illumination")

# Plot line graph
plt.figure(figsize=(10, 6))
plt.plot(merged_df["Illumination"], merged_df["Weighted Confidence"], color='orange', marker='o', linestyle='-', linewidth=2)
plt.title("Confidence vs illumination (High Beam)")
plt.xlabel("Illumination ")
plt.ylabel("Confidence")
plt.grid(True)
plt.tight_layout()
plt.show()
