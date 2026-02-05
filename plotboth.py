import pandas as pd
import matplotlib.pyplot as plt

# Load data
hardware_df = pd.read_excel("C:/Users/Abhijeet/Downloads/Gain_Calculations.xlsx")
sim_df = pd.read_csv("C:/Users/Abhijeet/Downloads/cleaned_circuit1_gain_vs_freq.csv")

# Clean column names to remove accidental spaces
hardware_df.columns = hardware_df.columns.str.strip()
sim_df.columns = sim_df.columns.str.strip()

# Print to verify
print("Hardware columns:", hardware_df.columns)
print("Simulation columns:", sim_df.columns)

# Now safely extract the data
hardware_freq = hardware_df["Frequency"]
hardware_gain = hardware_df["Gain (dB)"]

sim_freq = sim_df["Frequency"]
sim_gain = sim_df["Gain (dB)"]

# Plot
plt.figure(figsize=(10, 6))
plt.semilogx(sim_freq, sim_gain, label="Simulation Gain (LTspice)", linestyle="--", color="orange")
plt.plot(hardware_freq, hardware_gain, 'o-', label="Hardware Gain", color="blue")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.title("Hardware vs Simulation Gain")
plt.grid(True, which='both', linestyle='--', linewidth=0.6)
plt.legend()
plt.tight_layout()
plt.show()
