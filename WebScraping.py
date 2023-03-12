# Modules
import requests
from bs4 import BeautifulSoup
import os
'''

NOTE!:

Keep in mind that you have to write 
the anime name the same way it appears in the URL


'''
print("------------------- Web Scraping By MashhorDev @Eiitp -------------------")
#input Manga as String , Chapter as Integer
Manga = str(input("Manga Name : "))
Chapter = int(input("Chapter Number  : "))

# requests web page
url = f"https://3asq.org/{Manga}/{Chapter}/"
response = requests.get(url)
soup = BeautifulSoup(response.content , "html.parser")
images_link = soup.find_all("img")
images = [tag["src"] for tag in images_link]

# Create Folder If Not exists
folder = f"{Manga} {Chapter}"
if not os.path.exists(folder):
  os.makedirs(folder)

# Download Into Folder

for i, url in enumerate(images):
  filename = f"{i+1}.jpg"
  filepath = os.path.join(folder,filename)
  with open(filepath, "wb") as f:
    f.write(requests.get(url).content)
print(f"Downloaded {len(images)} images to {folder}")
print("------------------- Done -------------------")
