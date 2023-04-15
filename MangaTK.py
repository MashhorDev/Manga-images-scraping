import tkinter as tk
import requests
from bs4 import BeautifulSoup
import os

# Set up main window
root = tk.Tk()
root.title("Manga Downloader")

# Create GUI elements
copyright_label = tk.Label(root, text="©2023 MashhorDev @0hak")
manga_label = tk.Label(root, text="Manga Name:")
manga_entry = tk.Entry(root)
chapter_label = tk.Label(root, text="Chapter Number:")
chapter_entry = tk.Entry(root)
download_button = tk.Button(root, text="Download")
status_label = tk.Label(root, text="")

# Layout GUI elements
copyright_label.grid(row=0, column=0)
manga_label.grid(row=1, column=0)
manga_entry.grid(row=1, column=1)
chapter_label.grid(row=2, column=0)
chapter_entry.grid(row=2, column=1)
download_button.grid(row=3, column=1)
status_label.grid(row=4, column=0, columnspan=2)

# Define callback function for download button
def download_manga():
    # Get user inputs
    manga_name = manga_entry.get()
    chapter_number = int(chapter_entry.get())

    # requests web page
    url = f"https://3asq.org/{manga_name}/{chapter_number}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    images_link = soup.find_all("img")
    images = [tag["src"] for tag in images_link]

    # Create Folder If Not exists
    folder = f"{manga_name} {chapter_number}"
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Download Into Folder
    for i, url in enumerate(images):
        filename = f"{i+1}.jpg"
        filepath = os.path.join(folder, filename)
        with open(filepath, "wb") as f:
            f.write(requests.get(url).content)
    status_label.config(text=f"Downloaded {len(images)} images to {folder}, successfully")

# Bind download button to callback function
download_button.config(command=download_manga)

# Start main loop
root.mainloop()
