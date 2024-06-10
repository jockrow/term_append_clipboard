import time
import pyperclip


def append_to_file(text, file_path):
    with open(file_path, "a") as file:
        file.write(text + "\n")


def main():
    file_path = "clipboard_history.txt"  # Change the file path as needed

    while True:
        # Get the current clipboard content
        clipboard_text = pyperclip.paste()

        # Check if the clipboard content is different from the last iteration
        if clipboard_text != main.last_clipboard_text:
            # Append the new clipboard content to the file
            append_to_file(clipboard_text, file_path)
            print(f"Appended to file: {clipboard_text}")

            # Update the last clipboard text
            main.last_clipboard_text = clipboard_text

        # Pause for a short duration before checking again
        time.sleep(2)


if __name__ == "__main__":
    # Initialize the last clipboard text
    main.last_clipboard_text = pyperclip.paste()

    # Run the main loop
    main()
