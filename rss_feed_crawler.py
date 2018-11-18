import os
import xml.etree.ElementTree as ET
import csv

"""
rss_feed_crawler.py iterates through a folder that contains several xml files with RSS feeds from news related articles.
It creates a csv file with the date, title, description, and link of each article.
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


# dnitem method goes through a folder of xml files and returns the tags
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
            #table.append((date, title, description, link))
    return table


def apitem():
    basepath = '/Users/felipesepulveda/PycharmProjects/news/data_copy/aftenposten'

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


def vgitem():
    basepath = '/Users/felipesepulveda/PycharmProjects/news/data_copy/vg'

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


def hagnaritem():
    basepath = '/Users/felipesepulveda/PycharmProjects/news/data/hagnar'

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


def nrkitem():
    basepath = '/Users/felipesepulveda/PycharmProjects/news/data_copy/nrk'

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


def syslaitem():
    basepath = '/Users/felipesepulveda/PycharmProjects/news/data_copy/sysla'

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


# MÅ JOBBES MED

def tuitem():
    basepath = '/Users/felipesepulveda/PycharmProjects/news/data_copy/tu'

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


# Writer for all the
def writer():
    # CSV writer for Bergens Tidende
    if not bt_items():
        print("CSV for BT was not created")
    else:
        print("########### BERGENS TIDENDE - CSV FILE CREATED ###########\n")
        with open('bt.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in bt_items():
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for E24
    if not e24item():
        print("CSV for E24 was not created")
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
        print("CSV for DN was not created")
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
        print("CSV for Adressa was not created")
    else:
        print("########### Adressa - CSV FILE CREATED ###########")
        with open('adressa.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in adressaitem():
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for Aftenposten
    if not apitem():
        print("CSV for DN was not created")
    else:
        print("########### Aftenposten - CSV FILE CREATED ###########")
        with open('aftenposten.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in apitem():
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for VG
    if not vgitem():
        print("CSV for VG was not created")
    else:
        print("########### VG - CSV FILE CREATED ###########")
        with open('vg.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in vgitem():
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for Hegnar
    if not hagnaritem():
        print("CSV for Hegnar was not created")
    else:
        print("########### Hegnar - CSV FILE CREATED ###########")
        with open('hegnar.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in hagnaritem():
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for NRK
    if not nrkitem():
        print("CSV for NRK was not created")
    else:
        print("########### NRK - CSV FILE CREATED ###########")
        with open('nrk.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in nrkitem():
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for TU
    if not tuitem():
        print("CSV for TU was not created")
    else:
        print("########### TU - CSV FILE CREATED ###########")
        with open('tu.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in tuitem():
                writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})

    # CSV writer for SYSLA
    if not syslaitem():
        print("CSV for Sysla was not created")
    else:
        print("########### Sysla - CSV FILE CREATED ###########")
        with open('sysla.csv', 'w', newline='') as f:
            fieldnames = ['date', 'title', 'description', 'link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for date, title, description, link in syslaitem():
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