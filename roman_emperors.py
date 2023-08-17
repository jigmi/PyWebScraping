# This script will strengthen my web request/scraping capabilties by outputting 
# a list of roman emperors in a specified period.
from bs4 import BeautifulSoup
import requests

def app():
    # function for intitiating request and passing response
    source = request()
    if (source == "error"):
        return source
    emperor_periods,all_emperors = html(source)
    selection(emperor_periods,all_emperors)
        
def request():
    try:
        user_agent = {"User-Agent":"Mozilla/4.0"}
        source = requests.get("https://en.wikipedia.org/wiki/List_of_Roman_emperors",headers=user_agent)
        # If there is an error response (e.g 404/403/..) cause an error in the code
        source.raise_for_status()
        return source
    except Exception as e:
        # print error response
        print("The website has responded with the following error: " + str(e) + "\n")
        return "error"

def html(text):
    emperor_periods = []
    # Parsing HTML respones of the wikapedia page through beautifulsoup to perform extraction on
    html_text = BeautifulSoup(text.text,'html.parser')
    # Grepping all emperor periods through the use of specific html tags, however attribute ordering changes, 
    # so need to implement 2 statements
    all_emperors = html_text.find_all('table',class_="wikitable plainrowheaders",style="text-align:center; width:100%;")  
    all_emperors.extend(html_text.find_all('table',class_="wikitable plainrowheaders",style="width:100%; text-align:center;"))  
    for periods in all_emperors:
        emperor_periods.append(periods.find("span",class_="sr-only").text)
    return emperor_periods,all_emperors

def selection(emperor_periods,all_emperors):
    user_choice = ""
    print("""
          Welcome to Roma Emperor Periods, this simple application allows you to list out all
          the periods of rome, allowing you to select a period and list out all roman emperors 
          and relevant information, to get started type 'help' for a list of commands
          """)
    while (True):
        user_choice = input("(Roman Emperor App) Type a command:")
        if (user_choice == "help"):
            print("list - lists out all the periods of rome and their number ranking to select from")
            print("select number - selects the period")
        elif (user_choice == "list"):
            list_periods(emperor_periods)
        elif ("select" in user_choice):
            
            selection = int(user_choice.split(" ")[1])
            if (selection in range(1,26)):
                #gets the user choice e.g, 1 - 1 = 0, 2 -1 = 1. 
                user_choice = emperor_periods[selection - 1] 
                selected_period(user_choice,all_emperors)
            else:
                print("You have entered in a ranking out of the given range")
            
        else:
            print("""
                You have typed in a command incorrectly or one that does not exist.
                Remember you can type in 'help' to get a list of commands
                """)

def list_periods(emperor_periods):
    print("list of emperors, select a time period:")
    for ranking in range(0,len(emperor_periods)):
        print(f'{ranking+1}. {emperor_periods[ranking]}')

def selected_period(user_choice,all_emperors):
    print("You have selected the " + user_choice + " period.\n")
    print("The following emperors in descending time order are:\n")
    # enumerate through all the periods, and if the seleced user_choice matches 
    # with the span tag for the designated period, save the specified html for the
    # period
    for periods in all_emperors: 
        if user_choice == periods.find("span",class_="sr-only").text:
            chosen_period = periods     
            break
    # finds all tags that contain the naming element of the emperor
    naming_tag = chosen_period.find_all("th",scope="row")
    emperor_names = []
    for i in naming_tag:
        if (i.find("a") != None):
            emperor_names.append(i.find("a").get('title'))
    each_emperor = chosen_period
    # relevant information for each emperor is contained in the <tr> tag, saving 
    # it to a list
    each_emperor = each_emperor.find_all("tr")
    emperor_values = []
    for i in each_emperor:
        # specific value containing the reigning and description information for
        # each emperor is stored in the <td> tag 
        emperor_attributes = i.find_all("td")
        emperor_values.append(emperor_attributes)
    # first index contains irrelevant data
    emperor_values.pop(0)
    counter = 0
    reign = []
    description = []
    for l in range(0,len(emperor_values)):
        try:
            # reign value contained at index 1, description at index 2.
            # goes through each emperor related tags and extracts their information
            reign.append(emperor_values[l][1].text)
            description.append(emperor_values[l][2].text)
        except Exception as e:
            print("Error occured" + str(e))
    # Prints out relevant information by iterating through all the lists 
    for index in range(0,len(emperor_names)):
        print(str(index+1) +"." + emperor_names[index] + " reigned from " + reign[index] + description[index])
    print("\n")

if __name__ == "__main__":
    app()
