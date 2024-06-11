import time
import pyperclip


def append_to_file(text, file_path):
    with open(file_path, "a") as file:
        file.write(text + "\n")


def main():
    file_path = "clipboard_history.txt"

    while True:
        clipboard_text = pyperclip.paste()

        if clipboard_text != main.last_clipboard_text:
            append_to_file(clipboard_text, file_path)
            print(f"Appended to file: {clipboard_text}")

            main.last_clipboard_text = clipboard_text

        time.sleep(2)


if __name__ == "__main__":
    main.last_clipboard_text = pyperclip.paste()

    main()
