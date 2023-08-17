import requests
from bs4 import BeautifulSoup
# separate file containing configuration information (user/pass)
import config 

def main():
    username = config.username
    password = config.password
    user_agent = {'User-agent': 'Mozilla/4.0'}
    payload = {
        "action":"login",
        "user":username,
        "pass":password,
        "token":None,
        "remember":0
    }
    # http/https is stateless, therefore every request sent must be within session
    with requests.session() as session:
        session.post("https://whirlpool.net.au/profile/ajax.cfm",data=payload)
        source = session.get("https://whirlpool.net.au/profile/?action=account")
        source = BeautifulSoup(source.text,'html.parser')
        print(source)

if __name__ == '__main__':
    main()
