# This script will strengthen my web request/scraping capabiltiies by outputting a list of roman emperors in a specified period.
from bs4 import BeautifulSoup
import requests, openpyxl

def request():
    try:
        user_agent = {"User-Agent":"Mozilla/4.0"}
        source = requests.get("https://en.wikipedia.org/wiki/List_of_Roman_emperors",headers=user_agent)
        source.raise_for_status()
        html(source)
    except Exception as e:
        print(e)

def html(text):
    html_text = BeautifulSoup(text.text,'html.parser')

    emperor_periods = ["Julio-Claudian dynasty","Year of the Four Emperors"]
    user_choice = input("1. Julio-Claudian dynasty (27 BC – AD 68) \n2. Year of the Four Emperors (68–69) \nInput a number to select which period you want to display:  ")
 
    user_choice = emperor_periods[int(user_choice) - 1] #gets the user choice e.g, 1 - 1 = 0, 2 -1 = 1.
 
    all_emperors = html_text.find_all('table',class_="wikitable plainrowheaders",style="text-align:center; width:100%;")
    
    #start a for loop to find the ones that contain the period

    for periods in all_emperors:
        if user_choice == periods.find("span",class_="sr-only").text:
            x = periods        
            break
    

    x = x.find("tbody").find_all("i")
    for i in x:
        print(i.text)   
    #periods saved as last
    '''
    name = periods.find_all("i")
    for emperors in name:
        print(emperors.text)
    '''    





if __name__ == "__main__":
    request()
