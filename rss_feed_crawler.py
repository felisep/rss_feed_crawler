import os
import xml.etree.ElementTree as ET
import csv

"""
rss_feed_crawler.py iterates through a folder that contains several xml files with RSS feeds from news related articles.
It rsscreates a csv file with the url, title, date, and description of each article.
"""


# bt_items method goes through a folder of xml files and returns the tags
def bt_items():
    basepath = '/Users/felipesepulveda/PycharmProjects/news/data_copy/bergens_tidende'

    table = []

    for fname in os.listdir(basepath):
        if fname != "last_feed.xml":
            files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        items = root.find("channel").findall("item")
        for item in items:
            date = item.find("pubDate").text
            title = item.find("title").text
            description = item.find("description").text
            link = item.find("link").text
            #table.append((date, title, description, link))
    return table


def e24item():
    basepath = '/Users/felipesepulveda/PycharmProjects/news/data_copy/e_24_finans'

    table = []
    for fname in os.listdir(basepath):
        if fname != "last_feed.xml":
            files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        for child in root:
            items = root.find("channel").findall("item")
            for item in items:
                date = child.find("pubDate").text
                title = item.find("title").text
                description = item.find("description").text
                link = item.find("link").text
                #table.append((date, title, description, link))
    return table


# There is no need for description here. In this RSS feed <Description> has URL's and pictures
def dnitem():
    basepath = '/Users/felipesepulveda/PycharmProjects/news/data_copy/dn'

    table = []
    for fname in os.listdir(basepath):
        if fname != "last_feed.xml":
            files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        for child in root:
            items = root.find("channel").findall("item")
            for item in items:
                date = child.find("pubDate").text
                title = item.find("title").text
                link = item.find("link").text
                #table.append((date, title, link))
    return table


def adressaitem():
    basepath = '/Users/felipesepulveda/PycharmProjects/news/data_copy/adressa'

    table = []

    for fname in os.listdir(basepath):
        if fname != "last_feed.xml":
            files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        for child in root:
            items = root.find("channel").findall("item")
        for item in items:
            date = child.find("pubDate").text
            title = item.find("title").text
            description = item.find("description").text
            link = item.find("link").text
            table.append((date, title, description, link))
    return table


def writer():
    # CSV writer for Bergens Tidende
    if not bt_items():
        print("BT doesn't have any items")
    else:
        print("########### BERGENS TIDENDE - CSV FILE CREATED ###########")
        with open('ba.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in bt_items():
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for E24
    if not e24item():
        print("E24 doesnt have any items")
    else:
        print("########### E24 - CSV FILE CREATED ###########")
        with open('e24.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in e24item():
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for DN
    if not dnitem():
        print("DN doesnt have any items")
    else:
        print("########### DN - CSV FILE CREATED ###########")
        with open('dn.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, link in dnitem():
                writer.writerow({'date': date, 'title': title, 'link': link})

    # CSV writer for Adressa
    if not adressaitem():
        print("DN doesnt have any items")
    else:
        print("########### Adressa - CSV FILE CREATED ###########")
        with open('adressa.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in adressaitem():
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})


def main():
    writer()


main()

"""# HER MÅ DET JOBBES LITT MED, HER ER DET BOOLEAN PÅ ABONNERING
basepath = '/Users/felipesepulveda/PycharmProjects/news/data/bergens_avisen'

print("########### BERGENS AVISEN ########### \n")

for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        pass
    elif fname != "last_feed.xml":
        files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        for child in root:
            items = root.find("channel").findall("item")
            for item in items:
                #link = item.find("link").text
                #title = item.find("title").text
                date = item.find("pubDate").text
                #description = item.find("description").text
                print("Date: " + date)
                #print("Title: " + title)
                #if description is not None:
                   # print("Description: " + description)
                #print("URL: " + link + "\n")
                # TODO Create new file here append that information
"""

#HER MÅ DET JOBBES LITT MED
"""basepath = '/Users/felipesepulveda/PycharmProjects/news/data/kommunal_rapport'

print("########### KOMMUNAL RAPPORT ########### \n")

for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        pass
    elif fname != "last_feed.xml":
        files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        for child in root:
            items = root.find("channel").findall("item")
            for item in items:
                title = item.find("title").text
                print(title)"""


"""basepath = '/Users/felipesepulveda/PycharmProjects/news/data/aftenposten'

print("########### AFTENPOSTEN ########### \n")

for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        pass
    elif fname != "last_feed.xml":
        files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        for child in root:
            items = root.find("channel").findall("item")
            for item in items:
                title = item.find("title").text
                link = item.find("guid").text
                description = item.find("description").text
                print("Title: " + title)
                if description is not None:
                    print("Description: " + description)
                print("Link: " + link + "\n")


basepath = '/Users/felipesepulveda/PycharmProjects/news/data/vg'

print("########### VG ########### \n")

for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        pass
    elif fname != "last_feed.xml":
        files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        for child in root:
            items = root.find("channel").findall("item")
            for item in items:
                link = item.find("link").text
                title = item.find("title").text
                date = item.find("pubDate").text
                print("Date: " + date)
                description = item.find("description").text
                print("Title: " + title)
                if description is not None:
                    print("Description: " + description)
                print("URL: " + link + "\n")"""
            # TODO Create new file here append that information

"""basepath = '/Users/felipesepulveda/PycharmProjects/news/data/hagnar'

print("########### HAGNAR ########### \n")

for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        pass
    elif fname != "last_feed.xml":
        files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        for child in root:
            items = root.find("channel").findall("item")
            for item in items:
                link = item.find("link").text
                title = item.find("title").text
                date = item.find("pubDate").text
                print("Date: " + date)
                description = item.find("description").text
                print("Title: " + title)
                if description is not None:
                    print("Description: " + description)
                print("URL: " + link + "\n")
            # TODO Create new file here append that information"""


"""basepath = '/Users/felipesepulveda/PycharmProjects/news/data/nrk'

print("########### NRK ########### \n")

for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        pass
    else:
        files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        for child in root:
            items = root.find("channel").findall("item")
            for item in items:
                link = item.find("link").text
                title = item.find("title").text
                date = item.find("pubDate").text
                print("Date: " + date)
                description = item.find("description").text
                print("Title: " + title)
                if description is not None:
                    print("Description: " + description)
                print("URL: " + link + "\n")
            # TODO Create new file here append that information"""

"""basepath = '/Users/felipesepulveda/PycharmProjects/news/data/tu'

print("########### TU ########### \n")

for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        pass
    else:
        files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        for child in root:
            items = root.find("channel").findall("item")
            for item in items:
                link = item.find("link").text
                title = item.find("title").text
                date = item.find("pubDate").text
                print("Date: " + date)
                print("Title: " + title)
                print("URL: " + link + "\n")
            # TODO Create new file here append that information"""


"""basepath = '/Users/felipesepulveda/PycharmProjects/news/data/sysla'

print("########### SYSLA ########### \n")

for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        pass
    else:
        files = ET.parse(os.path.join(basepath, fname))
        root = files.getroot()
        for child in root:
            items = root.find("channel").findall("item")
            for item in items:
                link = item.find("link").text
                title = item.find("title").text
                date = item.find("pubDate").text
                print("Date: " + date)
                description = item.find("description").text
                print("Title: " + title)
                if description is not None:
                    print("Description: " + description)
                print("URL: " + link + "\n")
            # TODO Create new file here append that information"""
