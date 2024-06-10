import requests


class currencyConverter():

  def __init__(self):
    print("Welcome to Currency Python App")
    self.URL = "https://open.er-api.com/v6/latest/"
    self.CurrencyListURL = "https://openexchangerates.org/api/currencies.json"
    self.fetchCurrency()

  def fetchCurrency(self):
    try:
      self.currencyList = requests.get(self.CurrencyListURL)
      if self.currencyList.status_code == 200:
        self.clist = self.currencyList.json()
    except Exception as e:
      print(e)
      print("Error in API fetching for all currency")
      print("But We support all the UN Recognised Currencies")

  def baseCurrency(self, baseCurr):
    if baseCurr.upper() in self.clist:
      self.baseCurrency = baseCurr
    else:
      print("Enter valid currency symbol ")

  def convertCurrency(self, conCurr):
    if conCurr.upper() in self.clist:
      self.connCurr = conCurr
    else:
      print("Enter valid currency symbol ")

  def printCurrency(self):
    try:
      if self.clist:
        print("We support all the UN Recognised Currencies")
        print("The Currency List is as follows")
        print()
        for symbol, currencyName in self.clist.items():
          print(symbol, " = ", currencyName)
    except Exception as e:
      print("Error in API fetching for all currency")

  def fetchSymbol(self):
    self.symbolURL = 'https://restcountries.com/v3.1/all?fields=currencies'
    try:
      self.symbolList = requests.get(self.symbolURL)
      if self.symbolList.status_code == 200:
        self.slist = self.symbolList.json()
    except Exception as e:
      print(e)
      print("Error in API fetching for all currency")
      print("But We support all the UN Recognised Currencies")

    for i in self.slist:
      for key, value in i['currencies'].items():
        if key == self.baseCurrency:
          self.baseSymbol = value['symbol']
        elif key == self.connCurr:
          self.connSymbol = value['symbol']

  def getCurrencyData(self):
    self.convertdata = requests.get(f'{self.URL}{self.baseCurrency}')
    try:
      if self.convertdata.status_code == 200:
        self.convertList = self.convertdata.json()
    except Exception as e:
      print("Error in API fetching for converting currency")
      print("Kindly try after some time")

  def conversionRate(self, conversionCurrency):
    self.getCurrencyData()
    try:
      if self.convertList:
        if conversionCurrency in self.convertList['rates']:
          self.rate = self.convertList['rates'][f'{conversionCurrency}']
        else:
          print('Currency not available')
    except Exception as e:
      print("Error in API fetching for converting currency")
      print("Kindly try after some time")

  def convert(self, amt):
    self.fetchSymbol()
    self.conAmount = amt * self.rate
    print(
        f'{self.baseCurrency} {self.baseSymbol}{amt} is equal to {self.connCurr} {self.connSymbol}{self.conAmount:.2f}'
    )


def main():
  cur = currencyConverter()
  choice = 1
  while choice:
    print("""
        Main Menu : Enter the number to 
        1 - Convert Currency
        2 - Show all available Currencies
        3 - Exit
    """)
    choice = int(input())

    if choice == 1:
      flag = True
      while flag:
        base = input('Enter the Base Currency Symbol ').strip().upper()
        if base in cur.clist:
          cur.baseCurrency(base)
          flag = False
        else:
          print("Enter valid currency symbol ")

      flag = True
      while flag:
        cunc = input('Enter the Converted Currency Symbol ').strip().upper()
        if cunc in cur.clist:
          cur.convertCurrency(cunc)
          flag = False
        else:
          print("Enter valid currency symbol ")

      cur.getCurrencyData()
      cur.conversionRate(cur.connCurr)

      while True:
        ch = input(
            f'Do you want to convert {cur.baseCurrency} to {cur.connCurr.upper()} (y/n)? '
        )
        if ch.lower() == 'y':
          amount = float(input(f'Enter the amount of {cur.baseCurrency} '))
          print()
          cur.convert(amount)
        else:
          break
    elif choice == 2:
      cur.printCurrency()
    elif choice == 3:
      print("Thank you for using Our Currency Python App")
      quit()
    else:
      print('Enter a valid choice')


if __name__ == '__main__':
  main()
