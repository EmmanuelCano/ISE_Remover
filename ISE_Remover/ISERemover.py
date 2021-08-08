#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import sys
import csv



# Add Global Variables
ISE_IPAddress="10.10.10.10"
urldevices = "https://"+ISE_IPAddress+":9060/ers/config/networkdevice"
urlusers="https://"+ISE_IPAddress+":9060/ers/config/internaluser"
based64credentails= "Basic ZWNhbm9ndXQxOkNpc2NvMTIz"


def get_devices():


    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': based64credentails
    }

    response = requests.request("GET", urldevices,headers=headers, verify=False)


    if response.status_code == requests.codes.ok:
        #token = response.json()
        return response

def get_users():

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': based64credentails
    }

    # Get Token and save in response variable
    response = requests.request("GET", urlusers,headers=headers, verify=False)


    if response.status_code == requests.codes.ok:

        return response



if __name__ == '__main__':


    devices=get_devices()
    users=get_users()

    print('Welcome to ISE Remover!, WARNING: This script uses CSV file to perform action 4 and 6. Network Access Devices are based on names.\nPlease select one option for Network Access Device or Users:')
    Option= int(input(" 1. Print all Network Access Devices \n 2. Save the result in a txt file \n 3. Get the info from File \n 4. Remove the Network Access Devices from CSV File  \n 5. Print all internal Users \n 6. Remove all internal Users from CSV file \n 7. Exit \nType the option: "))

    if Option == 1:

        print(devices.text)

    elif Option == 2:

        original_stdout = sys.stdout
        filename=str(input('Define a name for the file: '))
        with open(filename+'.txt', 'w') as f:
         sys.stdout = f
         print(devices.text)
         sys.stdout = original_stdout

    elif Option == 3:
        samplefile = open('Devices.txt')
        samplereader = csv.reader(samplefile)
        sampledata = list(samplereader)

        for x in sampledata:
           print(x[0])

    elif Option == 4:
         Filename=input(str("¿What is the filename?: "))

         with open(Filename+".csv","r", newline='') as csvfile:
          spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
          for row in spamreader:
           device=(', '.join(row))

           url= "https://"+ISE_IPAddress+":9060/ers/config/networkdevice/name/" + device


           headers = {
           'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Authorization': based64credentails
           }

           response = requests.request("DELETE", url,headers=headers, verify=False)
           print(response)
    elif Option == 5:
         print(users.text)

    elif Option == 6:
         Filename=input(str("¿What is the filename?: "))

         with open(Filename+".csv","r", newline='') as csvfile:
          spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
          for row in spamreader:
           users=(', '.join(row))

           url= "https://"+ISE_IPAddress+":9060/ers/config/internaluser/name/" + users


           headers = {
           'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Authorization': based64credentails
           }


           response = requests.request("DELETE", url,headers=headers, verify=False)
           print(response)

    elif Option == 7:
          exit()

    else:
        print ("Number not Valid")
