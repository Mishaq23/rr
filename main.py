import random, math
import requests                                                 
from bs4 import BeautifulSoup
 

class Converter():

    def __init__(self, dollars: float, rubles: float, choice: str):
        self.dollars = dollars
        self.rubles  = rubles
        self.choice = choice
    
    def main(self) -> str:
        if self.choice == 'Dollars to rubles':
            return str(round(self.dollar_to_ruble(), 2))
        elif self.choice == 'Rubles to dollars':
            return str(round(self.ruble_to_dollar(), 2))
        else:
            return 'Undefined choice to convert'

    def change(self) -> float:
        link = 'https://www.google.com/search?q=dollar+to+ruble&oq=dollar+&aqs=chrome.1.69i57j0i131i433i512l3j0i512l3j46i199i465i512j0i512j46i199i465i512.2664j0j7&sourceid=chrome&ie=UTF-8'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
        full_page1 = requests.get(link, headers=headers)
        soup1 = BeautifulSoup(full_page1.content, 'html.parser')
        convert = soup1.find_all("span", {'class': 'DFlfde SwHCTb', 'data-precision': "2"})

        value = float(convert[0].text.replace(',', '.'))
        return value

    def dollar_to_ruble(self) -> float:
        rubles_in_doll = self.change()
        return self.dollars * rubles_in_doll

    def ruble_to_dollar(self) -> float:
        dollars_in_rubles = 1/self.change()
        return self.rubles * dollars_in_rubles 


if __name__ == '__main__':
    num_of_dollar = float(input())
    num_of_ruble = float(input())
    print('''If you want to convert dollars to rubles input: Dollars to rubles
If you want to convert rubles to dollars input: Rubles to dollars''')
    choice = input()

    object1 = Converter(num_of_dollar, num_of_ruble, choice)
    print(object1.main())
