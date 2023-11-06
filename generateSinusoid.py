from microbit import sleep, pin0
import math

def generate_sinusoid(frequency, duration_ms):
    # Constants
    SAMPLE_RATE = 1000  # Sample rate in Hz (1000 samples per second)
    TWO_PI = 2 * math.pi

    num_samples = duration_ms

    # Generate and output the sinusoid
    for i in range(num_samples):
        # Calculate the current angle (in radians)
        angle = TWO_PI * frequency * i / SAMPLE_RATE
        sin_val = math.sin(angle)
        analog_val = int((sin_val + 1) * 512)
        pin0.write_analog(analog_val)
        sleep(1)
