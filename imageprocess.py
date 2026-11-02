import numpy as np

print(np.array([1, 2, 3]))

# Original image represented as a matrix
image = np.array([
    [50, 100, 150],
    [80, 120, 180],
    [90, 140, 200]
])

print("Original Image:")
print(image)

# 1. Reshaping the image matrix
reshaped = image.reshape(1, 9)
print("\nReshaped Image:")
print(reshaped)

# 2. Slicing a specific region
region = image[0:2, 1:3]
print("\nSliced Region:")
print(region)

# 3. Brightness adjustment using broadcasting
bright_image = np.clip(image + 30, 0, 255)
print("\nImage After Brightness Adjustment:")
print(bright_image)

# 4. Matrix multiplication for transformation
transform = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

transformed = np.dot(image, transform)
print("\nTransformed Image:")
print(transformed)

