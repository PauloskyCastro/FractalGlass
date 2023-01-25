import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_glass():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    glass = f.generate()
    # Add noise to the fractal shape to make it look more like glass
    noise = np.random.normal(0, 0.05, glass.shape)
    glass = glass + noise
    glass = np.clip(glass, 0, 1)
    # Return the fractal glass
    return glass

# Generate 10 fractal glass images
for i in range(10):
    glass = generate_fractal_glass()
    plt.imshow(glass, cmap='gray')
    plt.savefig("fractal_glass_{}.png".format(i))
