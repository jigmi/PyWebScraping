from bs4 import BeautifulSoup
import requests

def request():
    try:
        #sends a GET request and receives the response and saves it into source variable
        user_agent = {'User-agent': 'Mozilla/5.0'} #Sets user_agent because request detault is python and it will get blocked by most websites
        source = requests.get("https://www.imdb.com/chart/top/",headers = user_agent)  #cant tell an error from this
        source.raise_for_status() #if site is not reachable any error, it will cause an actual error in the code
        soup = BeautifulSoup(source.text,'html.parser') #source.text will get the html content of the response, need to parse it through beautiful soup.
        #What soup does above will return it a beautifulsoup object
        #we found out it is within 
        movies = soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3a")
    except Exception as e:
        print(e)
if __name__ == "__main__":
    request()