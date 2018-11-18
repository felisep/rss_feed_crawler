import csv
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

path = "/Users/felipesepulveda/PycharmProjects/news/csv_files/sysla.csv"


def geturl():
    url_list = []
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)


def main():
    geturl()


main()

# for url in url_list:  # Parse through each url in the list.
#    page = urlopen(url[0]).read()
#    soup = BeautifulSoup(page, "html.parser")
