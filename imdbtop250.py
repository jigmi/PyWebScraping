from bs4 import BeautifulSoup
import requests

def request():
    try:
        #sends a GET request and receives the response and saves it into source variable
        user_agent = {'User-agent': 'Mozilla/4.0'} #Sets user_agent because request detault is python and it will get blocked by most websites
        source = requests.get("https://www.imdb.com/chart/top/",headers = user_agent)  #cant tell an error from this
        source.raise_for_status() #if site is not reachable any error, it will cause an actual error in the code
        soup = BeautifulSoup(source.text,'html.parser') #source.text will get the html content of the response, need to parse it through beautiful soup.
        #What soup does above will return it a beautifulsoup object
        #we found out it is within
        movies = soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3a353071-0 wTPeg compact-list-view ipc-metadata-list--base",role="presentation").find_all("li") # basically 
         # code is pointed to each of these li tags containing the movie names.  #ant to ierate through each tag and access the name, also returns a list.
        rankings = {}
        for movie in movies:
            finding = movie.find('div',class_="sc-14dd939d-0 fBusXE cli-children") #gets the element tag of the movie containing the name, gets all of it so <h3 .... >, only need the text of the tag
            name_rank = finding.find('h3',class_="ipc-title__text")
            movie_year = finding.find("span",class_="sc-14dd939d-6 kHVqMR cli-title-metadata-item").text
            text = name_rank.text.split(".") # gets the text inside the tags, also splits 1. name into rank name
            movie_name = text[1][1:]
            movie_rank = text[0]
            rankings.update({movie_name:[movie_rank,movie_year]})
        return rankings
    except Exception as e:
        print(e)

if __name__ == "__main__":
    rankings = request()
    print(rankings["Stand by Me"])