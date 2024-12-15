from flask import jsonify
import requests

# 3 storage services, one, two, and three. where 0 is encountered returned not found
# two functions: check status and get data (with eg. round robyn or straight up random?)

#list of storages
storages = ['https://storage1.com', 'https://storage2.com', 'https://storage3.com']

def getStatus():
    #get status using REST call and return in JSON format
    pass

def getData():
    #get data using REST call and return in JSON format and randomised
    pass

if __name__ == '__main__':
    pass