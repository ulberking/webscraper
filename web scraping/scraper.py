import csv
import enum
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
startURL = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome(
    'C:/Users/Minho/Downloads/chromedriver_win32/chromedriver')
browser.get(startURL)
time.sleep(10)
planetdata = []


def scrapData():
    headers = ['NAME','LIGHT-YEARS FROM EARTH','PLANET MASS','STELLAR MAGNITUDE','DISCOVERY DATE']
    for a in range(1, 5):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        allul = soup.find_all('ul', attrs={'class', 'exoplanet'})
        for eachul in allul:
            allLi = eachul.find_all('li')
            temlist = []
            for index, eachli in enumerate(allLi):
                if index == 0:
                    temlist.append(eachli.find_all('a')[0].contents[0])
                else:
                    temlist.append(eachli.contents[0])
            planetdata.append(temlist)
        browser.find_element(
            By.XPATH, '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    with open('test.csv', 'w', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetdata)


scrapData()
