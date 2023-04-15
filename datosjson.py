import re
import json
import yaml
import time

with open ('myfile.json', 'r') as json_file:
    ourjson = json.load (json_file)

print("El token de acceso es: {}".format(ourjson['access_token']))
print("El token expira en {} segundos.".format(ourjson['expires_in']))



