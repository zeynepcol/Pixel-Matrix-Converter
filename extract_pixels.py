from PIL import Image

# Load your image (replace 'your_image.png' with the actual image name)
img = Image.open('your_image.png')

# Resize the image to make output manageable (Optional: Adjust dimensions)
img = img.resize((50, 50))  

# Convert the image to RGB mode
img = img.convert('RGB')

# Store pixel data as (x, y, r, intensity)
coordinates = []

# Get image dimensions
width, height = img.size

# Extract pixel data
for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))

        # Calculate pixel intensity (or use any other logic you need)
        intensity = (r + g + b) // 3

        # Append only the necessary elements (x, y, r, intensity)
        coordinates.append((x, y, r, intensity))

# Print output in C++ array format
print("{", end="")
for coord in coordinates:
    print(f"{{ {coord[0]}, {coord[1]}, {coord[2]}, {coord[3]} }},", end="")
print("}")
