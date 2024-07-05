import tkinter as tk
from tkinter import filedialog
import hashlib

def get_file_hash():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select a file
    file_path = filedialog.askopenfilename()

    if not file_path:
        print("No file selected.")
        return

    # Read the file content in binary mode
    with open(file_path, 'rb') as file:
        content = file.read()

    # Calculate the SHA-256 hash
    sha256_hash = hashlib.sha256(content).hexdigest()

    print(f"SHA-256 hash of '{file_path}': {sha256_hash}")

if __name__ == "__main__":
    get_file_hash()
