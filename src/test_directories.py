import os

# Get the absolute path of the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the script directory
model_dir = os.path.join(script_dir, "../models/fine_tuned_model/")
output_file = os.path.join(script_dir, "../generated_lyrics/lyrics.txt")

# Check if model directory exists
if os.path.exists(model_dir):
    print(f"Model directory exists: {model_dir}")
else:
    print(f"Model directory does not exist: {model_dir}")

# Ensure output directory exists
output_dir = os.path.dirname(output_file)
os.makedirs(output_dir, exist_ok=True)

# Verify if output directory was created
if os.path.exists(output_dir):
    print(f"Output directory exists or was successfully created: {output_dir}")
else:
    print(f"Failed to create output directory: {output_dir}")

# Test writing and reading a file
test_file_path = os.path.join(output_dir, "test_file.txt")

try:
    with open(test_file_path, "w") as test_file:
        test_file.write("Testing file writing permissions.\n")
    print(f"File successfully written to: {test_file_path}")
except Exception as e:
    print(f"Failed to write to file: {e}")

try:
    with open(test_file_path, "r") as test_file:
        content = test_file.read()
    print(f"File successfully read from: {test_file_path}")
    print(f"Content: {content}")
except Exception as e:
    print(f"Failed to read from file: {e}")

# Clean up the test file
os.remove(test_file_path)
print(f"Test file deleted: {test_file_path}")
