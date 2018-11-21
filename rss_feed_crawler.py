import io
import os
import xml.etree.ElementTree as ET
import csv

"""
rss_feed_crawler.py iterates through a folder that contains several xml files with RSS feeds from news related articles.
It creates a csv file with the date, title, description, and link of each article.
"""


# item(folder_dir) Retrieves content from elements pubDate, title, description and link returns.
# if folder name is in folder directory.
def item(folder_dir):

    table = []

    for fname in os.listdir(folder_dir):
        try:
            if fname != "last_feed.xml" and fname != ".DS_Store":
                files = ET.parse(os.path.join(folder_dir, fname))
                root = files.getroot()
                items = root.find("channel").findall("item")
                f = io.StringIO("no element found: line 1, column 0")
                for item in items:
                    if item is f:
                        pass
                    else:
                        date = item.find("pubDate").text
                        title = item.find("title").text
                        description = item.find("description").text
                        link = item.find("link").text
                        table.append((date, title, description, link))
        except Exception as e:
            print(fname, e)
    return table


# Writer for all the items. Checks if the folder exist, if not creates folder and add
# each csv file to the folder with name.
def writer():
    cwd = os.path.dirname(os.path.realpath(__file__))
    paper_dir = os.path.join(cwd, "data")

    for folders in os.listdir(paper_dir):
        if folders != ".DS_Store":
            folder_dir = os.path.join(paper_dir, folders)
            if not item(folder_dir):
                print(folders + " was not created")
            else:
                #print(folders + " csv file created")
                csv_dir = os.path.join(cwd, "csv_files")
                if not os.path.exists(csv_dir):
                    os.makedirs(csv_dir, exist_ok=True)
                csv_path = os.path.join(csv_dir, folders)
                with open(csv_path + '.csv', 'w', newline='') as f:
                    fieldnames = ['date', 'title', 'description', 'link']
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    for date, title, description, link in item(folder_dir):
                        writer.writerow({'date': date, 'title': title, 'description': description, 'link': link})


def main():
    writer()


main()
