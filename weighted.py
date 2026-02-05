import pandas as pd
import matplotlib.pyplot as plt

# Load weighted confidence values
low_conf_df = pd.read_csv("final_weighted_confidence_low_beam.csv")
high_conf_df = pd.read_csv("final_weighted_confidence_high_beam.csv")

# Load illumination data
low_illum_df = pd.read_csv("Low_Light_with_Illumination_with_Video_Name.csv")
high_illum_df = pd.read_csv("High_Beam_with_Illumination_with_Video_Name.csv")

# Convert Row and Position into Video Name format
def format_video_name(row):
    row_str = row["Row"].replace(" ", "")
    pos_str = row["Position"].replace(" ", "").replace("Position", "Pos")
    return f"{row_str}_{pos_str}.mp4"

# Apply formatting
low_illum_df["Video Name"] = low_illum_df.apply(format_video_name, axis=1)
high_illum_df["Video Name"] = high_illum_df.apply(format_video_name, axis=1)

# Merge illumination with weighted confidence
low_merged = pd.merge(low_conf_df, low_illum_df[["Video Name", "Illumination"]], on="Video Name", how="inner")
high_merged = pd.merge(high_conf_df, high_illum_df[["Video Name", "Illumination"]], on="Video Name", how="inner")

# Sort by illumination for smoother plots
low_merged = low_merged.sort_values("Illumination")
high_merged = high_merged.sort_values("Illumination")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(low_merged["Illumination"], low_merged["Weighted Confidence"], label="Low Light", color='blue', marker='o')
plt.plot(high_merged["Illumination"], high_merged["Weighted Confidence"], label="High Beam", color='orange', marker='s')

plt.title("Confidence vs Illumination (Weighted Average)")
plt.xlabel("Illumination")
plt.ylabel("Weighted Confidence")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
