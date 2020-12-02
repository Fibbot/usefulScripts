import requests
import json
import os
import argparse
import re

parser = argparse.ArgumentParser(description="Grab all projects from group")
parser.add_argument("--token", dest="token", required=True, help="Your git token")
parser.add_argument("--groupID", dest=groupID, required=True, help="Target group")

args = parser.parse_args()

headers = {"Private-Token": args.token}

a = requests.get(
    "https://YOURGITLABINSTANCE.COM/api/v4/groups/" + args.groupID + "/projects",
    headers=headers,
    verify=False
)

data = json.loads(a.text)

for id in data:
    b = id["http_url_to_repo"]
    b = b.replace("https://","")
    cmd = ("git clone " + "https://gitlab-ci-token:" + args.token + "@" + b)
    os.system(cmd)