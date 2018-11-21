import csv
import os
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_csv_files():
    csv_file_path_list = []

    cwd = os.path.dirname(os.path.realpath(__file__))
    csv_dir = os.path.join(cwd, "csv_files")
    for csv_file in os.listdir(csv_dir):
        csv_file_path = os.path.join(csv_dir, csv_file)
        csv_file_path_list.append(csv_file_path)
    return csv_file_path_list


def get_links():
    try:
        for links in get_csv_files():
            with open(links) as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    print(row['link'])
    except Exception:
        print("Didn't find any links")


# First process of cleaning the data
# Removes duplicates from rows in the set
def remove_duplicates():
        for path in get_csv_files():
            rows = open(path).read().split('\n')
            newrows = []
            for row in rows:
                if row not in newrows:
                    newrows.append(row)

            f = open(path, 'w')
            f.write('\n'.join(newrows))
            f.close()
            print("All duplicates were removed")


def main():
    get_links()


main()
