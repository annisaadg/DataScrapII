from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = "D:\Polban\SEMESTER 2\PROYEK1 PPLD SEM2\webScrap2\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.metacritic.com/browse/movies/score/metascore/all/filtered?sort=desc")

now = datetime.now()
movielist = []
i = 1

for movie in driver.find_elements_by_tag_name("tr"):
    print(movie.text)
    for tag in movie.find_elements_by_tag_name("a"):
        for img in tag.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))
            urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
            i = i+1
            movielist.append(
                {"Rating": movie.text.split("\n")[0],
                 "No": movie.text.split("\n")[1],
                 "Judul": movie.text.split("\n")[2],
                 "Platform": movie.text.split("\n")[3],
                 "Release": movie.text.split("\n")[4],
                 "waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S\n"),
                 "Image": img.get_attribute("src")
                 }
            )
            
hasil_scraping = open("NewMovie.json","w")
json.dump(movielist, hasil_scraping, indent=5)
hasil_scraping.close()

driver.quit()
