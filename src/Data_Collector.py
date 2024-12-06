# I intend to "scrape" my data within this file
from bs4 import BeautifulSoup
import requests
from lxml import html
import pandas as pd

URL = "https://www.tfrrs.org/lists/4516/2024_NCAA_Division_II_Outdoor_Qualifying_FINAL"
page = requests.get(URL)
tree = html.fromstring(page.content)

mens100m_data = tree.xpath('//*[@id="body"]')
womens100m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[3]/div/table/tbody')
mens200m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[4]/div/table/tbody')
womens200m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[5]/div/table/tbody')
mens400m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[6]/div/table/tbody')
womens400m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[7]/div/table/tbody')
mens800m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[8]/div/table/tbody')
womens800m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[9]/div/table/tbody')
mens1500m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[10]/div/table/tbody')
womens1500m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[11]/div/table/tbody')
mens5000m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[12]/div/table/tbody')
womens5000m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[13]/div/table/tbody')
mens10000m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[14]/div/table/tbody')
womens10000m_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[15]/div/table/tbody')
mens110h_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[16]/div/table/tbody')
womens100h_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[17]/div/table/tbody')
mens400h_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[18]/div/table/tbody')
womens400h_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[19]/div/table/tbody')
mens3000s_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[20]/div/table/tbody')
womens3000s_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[21]/div/table/tbody')
mensHJ_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[26]/div/table/tbody')
womensHJ_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[27]/div/table/tbody')
mensPV_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[28]/div/table/tbody')
womensPV_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[29]/div/table/tbody')
mensLJ_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[30]/div/table/tbody')
womensLJ_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[31]/div/table/tbody')
mensTJ_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[32]/div/table/tbody')
womensTJ_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[33]/div/table/tbody')
mensSP_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[34]/div/table/tbody')
womensSP_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[35]/div/table/tbody')
mensDT_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[36]/div/table/tbody')
womensDT_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[37]/div/table/tbody')
mensHT_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[38]/div/table/tbody')
womensHT_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[39]/div/table/tbody')
mensJT_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[40]/div/table/tbody')
womensJT_data = tree.xpath('/html/body/div[5]/div/div/turbo-frame/div[2]/div[41]/div/table/tbody')
print(mens100m_data)

# second try
page1 = requests.get(URL).text
soup = BeautifulSoup(page1, "html.parser")
print('Classes of each table:')
for table in soup.find_all('div'):
    print(table.get('class'))

male_tables = soup.find_all('div', class_='gender_m')
female_tables = soup.find_all('div', class_='gender_f')

df = pd.DataFrame(columns=["Athlete", "Team", "Time", "Meet"])

male_events = soup.find_all('h3')
for event in male_events:
    print(event.text)
# print(male_events)
male_dict = {}
# for table in male_tables:
#     print(table.get('class'))
#     event1 = table.get('h3')
#     event = event1.get('class')
#     male_dict['x%s' % event] = 0
#
# print(male_dict)
