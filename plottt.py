import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your data
df = pd.read_excel("C:/Users/Abhijeet/Downloads/CMRR_Calculations.xlsx")

# Convert Vout (in mV) to Ac in Volts
df["Ac (V)"] = df["Vout (mV)"] / 2000  # 1000 to V, then /2 for Ac = Vout/2

# Calculate CMRR and CMRR in dB
df["CMRR"] = df["Ad (V/V)"] / df["Ac (V)"]
df["CMRR (dB)"] = 20 * np.log10(df["CMRR"])

# Plot the Bode plot
plt.figure(figsize=(10, 6))
plt.semilogx(df["Frequency (Hz)"], df["CMRR (dB)"], marker='o', linestyle='-', label="CMRR (dB)")

# Highlight region between 20-40 Hz
plt.axvspan(20, 40, color='yellow', alpha=0.3, label="20–40 Hz Band")

# Add vertical line at cutoff frequency 0.05 Hz
plt.axvline(0.05, color='green', linestyle='--', label="Cutoff = 0.05 Hz")

# Labels and styles
plt.title("Bode Plot - CMRR vs Frequency")
plt.xlabel("Frequency (Hz)")
plt.ylabel("CMRR (dB)")
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
