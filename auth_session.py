import requests
from bs4 import BeautifulSoup
# separate file containing configuration information (user/pass)
import config 

def main():
    username = config.username
    password = config.password
    user_agent = {'User-agent': 'Mozilla/4.0'}
    payload_login = {
        "action":"login",
        "user":username,
        "pass":password,
        "token":None,
        "remember":0
    }
    change_pass = {
        "action":"changePassword",
        "p1":'iluvsecurity',
        "p2":'iluvsecurity',
        "credlogout":1,
        "token":None
    }
    # http/https is stateless, therefore every request sent must be within session
    with requests.session() as session:
        # Authenticating session
        session.post("https://whirlpool.net.au/profile/ajax.cfm",data=payload_login)
        source = session.get("https://whirlpool.net.au/profile/?action=account")
        source = BeautifulSoup(source.text,'html.parser')
        print(source)
        # Changing pass 
        post_response = session.post("https://whirlpool.net.au/profile/ajax.cfm",data=change_pass)
        post_response = BeautifulSoup(source.text,'html.parser')
        print(source)

if __name__ == '__main__':
    main()
