from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title= "top rated movies"
sheet.append(["MovieRank","Name","Year","IMBDrating"])
print(excel.sheetnames)

source = requests.get("https://www.imdb.com/chart/top/")
source.raise_for_status()

soup = BeautifulSoup(source.text,"html.parser")

movies = soup.find("tbody",class_="lister-list").find_all("tr")


for movie in movies:

    name=movie.find("td",class_="titleColumn").a.text

    rank = movie.find("td", class_="titleColumn").text.split(".")[0]

    year = movie.find("td", class_="titleColumn").span.text.strip("()")

    rating = movie.find("td", class_="ratingColumn imdbRating").strong.text

    sheet.append([rank, name, year, rating])


excel.save("C:\\Users\\Qaseem Shahid\\Desktop\\scrap.xlsx")