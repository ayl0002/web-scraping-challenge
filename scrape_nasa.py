
import os

import csv

from splinter import Browser

def find_browser():
    executable_path = {'executable_path': r'C:\Users\ayl00\OneDrive\Desktop\web-scraping-challenge\Missions_to_Mars\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
def pull_csv():
    
    mars_data = []

    csvfile = (r'C:\Users\ayl00\OneDrive\Desktop\web-scraping-challenge\Missions_to_Mars\final_data.csv')

    csvreader = csv.reader(csvfile, delimiter=',')

    csvpath = os.path.join(r'C:\Users\ayl00\OneDrive\Desktop\web-scraping-challenge\Missions_to_Mars\final_data.csv')

    with open(csvpath, newline='') as csvfile:

        print(csvreader)


    csv_header = next(csvreader)

    browser = find_browser()
    for row in csvreader:
        mars_data.append(row)
        return mars_data


if __name__ == '__main__':
    pull_csv()