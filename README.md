# ISE_Remover

Nowadays, Identity Services Engine is widely used by many customers and users to provide a centralized Network Access Control (NAC) and policy enforcement. Part of the process to achieve NAC is to add network devices (NADs) to ISE DataBase, while this has been an easy task through GUI the current challenge comes when multiple devices need to be deleted. This repository includes a script developed in Python for automating the deletion of multiple network access devices and or Internal Users simultanously, it also prints and/or saves the NADs or the Internal Users using ISE ERS API Calls. Although this process can be done manually via the Web UI, it results very complex to select two or more elements by clicking on each element checkbox, plus it is very prone to human errors.

This script  performs the following actions:
1. Get and print all Network Access Devices from ISE
2. Get and save all Network Access Devices from ISE in a txt file on the same folder of the script
3. Print Network Access Devices saved on the text File
4. Remove Network Access Devices simultaneously based on a CSV file saved on the same folder that this script.
5. Get and Print all internal Users in json data format
6. Remove all internal Users simultaneously based on a CSV file saved on the same folder that this script.


# Files in this Repository

The following is a more detailed explanation of the Files:

1. ISERemover.py: Main Script
2. NADSX.py: Script to Generate 100 TestUsers and Devices
3. TestNADs: CSV file with 1500 NADs to be imported into ISE
4. TestUsers: CSV File with 300 Users to be imported into ISE (CiscoLive2022)
5. GetCodeBased64: Script to get Based64 Credentials using Python library.


# Setting up the environment

- Python v.3.8.2 or above must be installed. This must be the only python version in the virtual environment or host OS

Install the dependencies included in this repository with the following command:
```
pip install -r requirements.txt
```

The following is a more detailed explanation of the Global Variables:

- **ISE_IPAddress**= Address of ISE PAN Node 
- **based64credentails**= ISE ERS Admin Credentials converted in Based64 Encoded 


# Installation

1. Clone this repository 

   https://github.com/EmmanuelCano/ISE_Remover.git

2. change into directory

   cd ISE_Remover

3. Update File_Example_For_NetworkDevices.txt or File_Example_For_Users.txt with the NADs and/or Users names


# Running the Script

In order to run the script issue the following command:

```
python3 ISERemover.py

```

# Example Menu
```
Welcome to ISE Remover!, WARNING: This script uses CSV file to perform action 4 and 6. Network Access Devices are based on names.
Please select one option for Network Access Device or Users:
 1. Print all Network Access Devices 
 2. Save the result in a txt file 
 3. Get the info from File 
 4. Remove the Network Access Devices from CSV File  
 5. Print all internal Users 
 6. Remove all internal Users from CSV file 
 7. Exit 
Type the option: 
```


More information about ISE Restful external API calls available can be found on https://developer.cisco.com/docs/identity-services-engine/3.0/!cisco-ise-api-documentation

Developed by [Emmanuel Cano - Cisco](https://www.linkedin.com/in/emmanuel-cano/)

