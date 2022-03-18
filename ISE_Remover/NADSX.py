#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


Credentials='Basic ZXJzYWRtaW46Q2lzY28xMjM='


def create_TestDevices(iseip):

  for i in range(1, 101):
    #Create variables to be use on the payload.
    name="NAD"
    NADs=name + str(i)

    IP_Address="1.1.1."
    NADIP=IP_Address + str(i)

   #ISE API Call to create NADS using NADs and NADIP
    url = "https://"+iseip+":9060/ers/config/networkdevice"

    payload="{\n    \"NetworkDevice\": {\n        \"name\": \""+NADs+"\",\n        \"description\": \"\",\n        \"authenticationSettings\": {\n            \"networkProtocol\": \"RADIUS\",\n            \"radiusSharedSecret\": \"C1sco12345\"\n        },\n        \"tacacsSettings\": {\n            \"sharedSecret\": \"C1sco12345\",\n            \"connectModeOptions\": \"OFF\"\n        },\n        \"NetworkDeviceIPList\": [\n            {\n                \"ipaddress\": \""+NADIP+"\",\n                \"mask\": 32\n            }\n        ],\n        \"NetworkDeviceGroupList\": [\n            \"Location#All Locations\",\n            \"IPSEC#Is IPSEC Device#No\",\n            \"Device Type#All Device Types\"\n        ]\n    }\n}"
    
    headers = {
    'Content-Type': 'application/json',
     'Accept': 'application/json',
    'Authorization': Credentials
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print ("Creating NAD: NAD"+ str(i))

def create_TestUsers(iseip):

    
  for i in range(1, 101):
    #Create variables to be use on the payload.
    name="CiscoLive"
    user=name + str(i)


   #ISE API Call to create Users using user variable
    url = "https://"+iseip+":9060/ers/config/internaluser"
    payload="{\n    \"InternalUser\": {\n        \"name\": \""+user+"\",\n        \"password\": \"C1sco12345\",\n        \"enablePassword\": \"C1sco12345\",\n        \"enabled\": true,\n        \"changePassword\": false\n        }\n    \n}\n"   
    
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': Credentials
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print ("Creating user: Cisco Live"+ str (i))


if __name__ == '__main__':

 iseip=input("Type ISE IP Address: ")

 print ("++++++++++++++++++++++++++++++++")     
 print ("Creating 100 NADs and 99 users")
 print ("+++++++++++++++++++++++++++++++++")

 create_TestDevices(iseip)
 create_TestUsers(iseip)

 print ("Users and Devices created successfully. Please continue with ISE_Remover script")     
 