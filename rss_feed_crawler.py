import os
import xml.etree.ElementTree as ET
import csv


basepath = '/Users/felipesepulveda/PycharmProjects/news/data_copy/bergens_tidende'

print("########### BERGENS TIDENDE - OK ########### \n")


def items():
    table = []
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
                date = child.find("lastBuildDate").text
                description = item.find("description").text
                table.append((date, title, description, link))
    return table


def writer():
    with open('test.csv', 'a', newline='') as f:
        fieldnames = ['date', 'title', 'link', 'description']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        thewriter.writeheader()

        for item in items():
            thewriter.writerow({'date': item, 'title': item, 'link': item, 'description': item})


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
                # TODO Create new file here append that information"""


"""basepath = '/Users/felipesepulveda/PycharmProjects/news/data/e_24_finans'

print("########### E24 FINANS - OK ########### \n")

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
                description = item.find("description").text
                filename = "test.csv"
                strPath = r"/Users/felipesepulveda/PycharmProjects/news/data_copy"
                os.chdir(strPath)
                txt_out = open(os.path.basename(filename), 'a')
                if description is not None:
                    txt_out.write("Description: " + description + "\n")
                txt_out.write("Date: " + date + "\n" + "Title: " + title + "\n" + "URL: " + link + "\n")"""


# There is no need for description here. In this RSS feed <Description> has URL's and pictures
"""basepath = '/Users/felipesepulveda/PycharmProjects/news/data/dn'

print("########### DAGENS NÆRINGSLIV - OK ########### \n")

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
                date = child.find("pubDate").text
                filename = "test.csv"
                strPath = r"/Users/felipesepulveda/PycharmProjects/news/data_copy"
                os.chdir(strPath)
                txt_out = open(os.path.basename(filename), 'a')
                txt_out.write("Date: " + date + "\n" + "Title: " + title + "\n" + "URL: " + link + "\n")"""



"""basepath = '/Users/felipesepulveda/PycharmProjects/news/data/adressa'

print("########### ADRESSA - OK ########### \n")

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
                description = item.find("description").text
                filename = "test.csv"
                strPath = r"/Users/felipesepulveda/PycharmProjects/news/data_copy"
                os.chdir(strPath)
                txt_out = open(os.path.basename(filename), 'a')
                if description is not None:
                    txt_out.write("Description: " + description + "\n")
                txt_out.write("Date: " + date + "\n" + "Title: " + title + "\n" + "URL: " + link + "\n")"""



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
