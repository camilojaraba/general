# Author: Camilo Jaraba - camilo.jaraba@gmail.com
#   Cloudflare Firewall Rules Export Script
#   This python script uses python3 to export firewall rules (WAF) to a JSON file
#   you can use later the fw-rules-import.py script to read the JSON file and create the rules in your desired domain
#
import json
import requests

zone_id = "<zone id for the domain you are exporting the rules from"
api_key = "your API key"
api_email = "your email from cloudflare account"

url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules?per_page=1000"
headers = {
    "X-Auth-Email": api_email,
    "X-Auth-Key": api_key,
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
rules = response.json()["result"]
with open("firewall_rules.json", "w") as f:
    json.dump(rules, f)
