# Author: Camilo Jaraba - camilo.jaraba@gmail.com
#   Cloudflare Firewall Rules Import Script
#   This python script uses python3 to import firewall rules (WAF) from a json file exported with my fw-rules-export.py script
#
import json
import requests

zone_id = "<zone id for the domain you are exporting the rules from"
api_key = "your API key"
api_email = "your email from cloudflare account"

url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules"
headers = {
    "X-Auth-Email": api_email,
    "X-Auth-Key": api_key,
    "Content-Type": "application/json"
}

with open("firewall_rules.json", "r") as f:
    rules = json.load(f)
count = 0
for rule in rules:
    count = count+1
    data = [{
        "description": rule["description"],
        "action": rule["action"],
        "filter": {"expression": rule["filter"]["expression"],"paused": rule["filter"]["paused"]}
    }]
    response = requests.post(url, headers=headers, json=data)
    error = response.json()["errors"]
    if response.status_code != 200:
        print (error)
print ("Total rules imported: " + count)