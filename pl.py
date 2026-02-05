import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
f = 10  # Frequency in Hz
Vpp = 20e-3  # Peak-to-peak voltage (20 mV)
t = np.linspace(0, 1, 1000)  # Time axis (1 second duration)
Vin = (Vpp / 2) * np.sin(2 * np.pi * f * t)

# Buffer output (ideal unity gain, no phase shift)
Vout = Vin.copy()

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(t, Vin * 1000, label='Input Signal (Vin)', linestyle='--')  # Convert to mV
plt.plot(t, Vout * 1000, label='Output Signal (Vout)', linewidth=2)
plt.title('Buffer Circuit Response')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
