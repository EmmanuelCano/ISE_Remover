# ISE_Remover

Nowadays, Identity Services Engine is widely used by many customers and users to provide a centralized Network Access Control (NAC) and policy enforcement. Part of the process to achieve NAC is to add network devices (NADs) to ISE DataBase, while this has been an easy task through GUI the current challenge comes when multiple devices need to be deleted. This repository includes a script developed in Python for automating the deletion of multiple network access devices and or Internal Users simultanously, it also print and/or save the NADs or the Internal Users using ISE ERS API Calls. Although this process can be done manually via the Web UI, it results very complex to select two or more elements by clicking on each element checkbox, plus it is very prone to human errors.

This script  performs the following actions:
1. Get and print all Network Access Devices from ISE
2. Get and save all Network Access Devices from ISE in a txt file on the same folder of the script
3. Print Network Access Devices saved on the text File
4. Remove Network Access Devices simultaneously based on a CSV file saved on the same folder that this script.
5. Get and Print all internal Users in json data format
6. Remove all internal Users simultaneously based on a CSV file saved on the same folder that this script.


The following is a more detailed explanation of the Global Variables:
ISE_IPAddress= Address of ISE PAN Node 
based64credentails= ISE ERS Admin Credentials converted in Based64 Encoded 


#Installation

1. Clone this repository 

https://github.com/EmmanuelCano/ISE_Remover.git

2. change into directory

cd ISE_Remover

3. Update File_Example_For_NetworkDevices.txt or File_Example_For_Users.txt with the NADs and/or Users names


#Running the Script

In order to run the script issue the following command:

Python3 ISE_Remover.py

More information about ISE Restful external API calls available can be found on https://developer.cisco.com/docs/identity-services-engine/3.0/!cisco-ise-api-documentation

Developed by Emmanuel Cano - Cisco

