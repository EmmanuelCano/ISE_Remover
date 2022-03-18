""" Generate Base64 Encoding """ 
import base64 

Creds=input("provide the creds in this format:password: ")
ENCODED = base64.b64encode(Creds.encode('UTF-8'))
print(ENCODED.decode('utf-8'))

