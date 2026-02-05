import pandas as pd
import matplotlib.pyplot as plt

# Load CSVs
confidence_df = pd.read_csv("final_weighted_confidence_low_beam.csv")
illumination_df = pd.read_csv("Low_Light_with_Illumination_with_Video_Name.csv")

# Clean column names
confidence_df.columns = confidence_df.columns.str.strip()
illumination_df.columns = illumination_df.columns.str.strip()

# Create 'Video Name' column in illumination data
illumination_df["Video Name"] = (
    illumination_df["Row"].str.replace(" ", "") + "_" +
    illumination_df["Position"].str.replace(" ", "").str.replace("Position", "Pos") +
    ".mp4"
)

# Merge the two dataframes on 'Video Name'
merged_df = pd.merge(confidence_df, illumination_df[["Video Name", "Illumination"]], on="Video Name", how="inner")

# Sort for clean line plot
merged_df = merged_df.sort_values(by="Illumination")

# Plot
plt.figure(figsize=(10, 6))
plt.plot(merged_df["Illumination"], merged_df["Weighted Confidence"], color='blue', marker='o', linestyle='-', linewidth=2)
plt.title("Confidence vs Illumination (Low Beam)")
plt.xlabel("Illumination")
plt.ylabel("Confidence")
plt.grid(True)
plt.tight_layout()
plt.show()
