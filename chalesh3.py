import requests
import json
from colorama import Fore,init
init()

http = requests.get("https://api.wallex.ir/v1/account/otc/price").text

myjson = json.loads(http)

print(myjson)