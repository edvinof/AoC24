grid = []
matches = 0

# Load grid from file
with open('four.csv') as input:
    for line in input:
        grid.append(line.strip())  # Remove trailing newline characters

# Define all 8 directions (dx, dy)
directions = [
    (0, 1),    # Right
    # (0, -1),   # Left
    (1, 0),    # Down
    # (-1, 0),   # Up
    (1, 1),    # Diagonal Down-Right
    (1, -1),   # Diagonal Down-Left
    # (-1, 1),   # Diagonal Up-Right
    # (-1, -1)   # Diagonal Up-Left
]

# Function to check for XMAS or SAMX in a given direction
def find_word(x, y, dx, dy):
    global matches
    word = ""
    for i in range(4):
        nx, ny = x + i * dx, y + i * dy  # Move in the given direction
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):  # Check bounds
            word += grid[nx][ny]
        else:
            return  # Stop if out of bounds
    if word == "XMAS" or word == "SAMX":
        matches += 1

# Loop through the grid and check all directions
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "X" or grid[x][y] == "S":
            for dx, dy in directions:
                find_word(x, y, dx, dy)

print(matches)