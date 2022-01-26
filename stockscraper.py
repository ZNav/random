#imports
from bs4 import BeautifulSoup
import requests

#variables
link = 'HELP'
url = 'https://robinhood.com/stocks/'
runAgain = 'True'

#functions
def select():
    global link
    link = input('Input the stock ticker symbol or cmd for a list of commands: ').upper()
    print(link)
    if(link == 'HELP'):
        print('Help: use a browser to see a stocks ticker symbol, for instance AAPL for Apple. Do list in input field to see list of stock ticker symbols.')
        return
    elif(link == 'LIST'):
        print('List:\nAAPL:\tApple\nSPY:\tS&P 500 ETF\nTSLA:\tTesla\nAMC:\tAMC Entertainment\nF:\tFord Motor\nSNDL:\tSundial Growers\nMSFT:\tMicrosoft\nAMZN:\tAmazon\nDIS:\tDisney\nNIO:\tNIO')
        return
    elif(link == 'CMD'):
        print('help: gives information on how to input a stock via ticker symbol\nlist: gives a list of a few major stocks and their ticker symbol\ncmd: yields this information')
        return
    getInfo()

def getInfo():
    global link
    global url
    page = requests.get(url+link)
    if(page.status_code == 404):
        print('Stock not found or available!')
        return
    soup = BeautifulSoup(page.content, 'html.parser')
    value = soup.find("span", class_='up')
    value = (value['aria-label'])
    priceChanges = soup.find(id="sdp-price-chart-price-change").findAll('span')[0].text
    print('Current stock price of '+link+': '+str(value)+'\nTotal change today: '+priceChanges)

#main
while(runAgain == 'True'):
    select()
    runAgain = input('Would you like to run again? y/n: ').upper()
    if(runAgain == 'Y'):
        runAgain = 'True'