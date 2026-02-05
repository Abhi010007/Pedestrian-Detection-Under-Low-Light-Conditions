import pandas as pd
import matplotlib.pyplot as plt

# Load phase data from CSV
df = pd.read_csv("C:/Users/Abhijeet/Downloads/phase_data.csv")

# Plot Phase Bode Plot
plt.figure(figsize=(10, 6))
plt.semilogx(df["Frequency (Hz)"], df["Phase"], marker='s', color='purple', label='Measured Phase (degrees)')
plt.title("Bode Plot - Phase vs Frequency")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.axvline(0.05, color='green', linestyle='--', label="Cutoff = 0.05 Hz")  # Optional
plt.legend()
plt.tight_layout()
plt.show()
