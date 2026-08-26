import numpy as np
import matplotlib.pyplot as plt

f = 5
duration = 1

# Continuous reference signal
t = np.linspace(0, duration, 1000)
signal = np.sin(2 * np.pi * f * t)

# Try different sampling frequencies
for fs in [100, 20, 10, 5]:

    # Sample instants
    ts = np.arange(0, duration, 1 / fs)

    # Sampled values
    samples = np.sin(2 * np.pi * f * ts)

    # Create graph
    plt.figure(figsize=(8, 3))

    # Original signal
    plt.plot(
        t,
        signal,
        color='lightgray',
        label='Original 5 Hz signal'
    )

    # Sample points
    plt.stem(
        ts,
        samples,
        linefmt='C0-',
        markerfmt='C0o',
        basefmt=' '
    )

    # Sampled signal
    plt.plot(
        ts,
        samples,
        'r--',
        label=f'Sampled from fs={fs} Hz'
    )

    plt.title(
        f'fs = {fs} Hz\n(Nyquist requires fs > 100 Hz)'
    )

    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.tight_layout()
    plt.show()