import os
import xml.etree.ElementTree as ET
import csv

"""
rss_feed_crawler.py iterates through a folder that contains several xml files with RSS feeds from news related articles.
It creates a csv file with the date, title, description, and link of each article.
"""


# dnitem method goes through a folder of xml files and returns the tags
# There is no need for description here. In this RSS feed <Description> has URL's and pictures
def item(basepath):

    table = []

    for fname in os.listdir(basepath):
        try:
            if fname != "last_feed.xml" and fname != ".DS_Store":
                files = ET.parse(os.path.join(basepath, fname))
                root = files.getroot()
                items = root.find("channel").findall("item")
                for item in items:
                    date = item.find("pubDate").text
                    title = item.find("title").text
                    description = item.find("description").text
                    link = item.find("link").text
                    table.append((date, title, description, link))
        except Exception as e:
            print(fname, e)
    return table


# Writer for all the
def writer():

    # CSV writer for E24
    if not item(basepath="./data/e_24_finans"):
        print("CSV for E24 was not created")
    else:
        print("########### E24 - CSV FILE CREATED ###########")
        with open('e24.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in item(basepath="./data/e_24_finans"):
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for DN
    if not item(basepath="./data/dn"):
        print("CSV for DN was not created")
    else:
        print("########### DN - CSV FILE CREATED ###########")
        with open('dn.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in item(basepath="./data/dn"):
                writer.writerow({'date': date, 'title': title, 'link': link})

    # CSV writer for Adressa
    if not item(basepath="./data/adressa"):
        print("CSV for Adressa was not created")
    else:
        print("########### Adressa - CSV FILE CREATED ###########")
        with open('adressa.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in item(basepath="./data/adressa"):
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for Aftenposten
    if not item(basepath="./data/aftenposten"):
        print("CSV for DN was not created")
    else:
        print("########### Aftenposten - CSV FILE CREATED ###########")
        with open('aftenposten.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in item(basepath="./data/aftenposten"):
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for VG
    if not item(basepath="./data/vg"):
        print("CSV for VG was not created")
    else:
        print("########### VG - CSV FILE CREATED ###########")
        with open('vg.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in item(basepath="./data/vg"):
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for Hegnar
    if not item(basepath="./data/hagnar"):
        print("CSV for Hegnar was not created")
    else:
        print("########### Hegnar - CSV FILE CREATED ###########")
        with open('hegnar.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in item(basepath="./data/hagnar"):
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for Trønderavisa
    if not item(basepath="./data/trønderavisa"):
        print("CSV for NRK was not created")
    else:
        print("########### Trønderavisa - CSV FILE CREATED ###########")
        with open('trønderavisa.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in item(basepath="./data/trønderavisa"):
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for Bergens Tidende
    if not item(basepath="./data/bergens_tidende"):
        print("CSV for BT was not created")
    else:
        print("########### BERGENS TIDENDE - CSV FILE CREATED ###########\n")
        with open('bt.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in item(basepath="./data/bergens_tidende"):
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for BA
    if not item(basepath="./data/bergens_avisen"):
        print("CSV for BA was not created")
    else:
        print("########### BA - CSV FILE CREATED ###########")
        with open('ba.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in item(basepath="./data/bergens_avisen"):
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})


def main():
    writer()


main()
