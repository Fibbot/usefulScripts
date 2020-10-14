#!/usr/bin/python3
'''
azureLoot.py:
    requires: cid (client id) tid (tenant id) cs (client secret)
    to run: python azureLoot.py -cid client_id_here -tid tenant_id_here -cs client_secret_here

    todo: find some valid creds to format and parse response
    '''
import argparse
import os
import requests

def args():
    parser = argparse.ArgumentParser(description='you\'ll need the client ID, client secret, and tenant ID\'s')
    parser.add_argument("-cid", "--client", dest="cid", required=True, help="Client ID")
    parser.add_argument("-cs", "--secret", dest="cs", required=True, help="Client secret")
    parser.add_argument("-tid", "--tenant", dest="tid", required=True, help="Tenant ID")

    args = parser.parse_args()

    if not args.cid or not args.cs or not args.tid:
        parse.print_help()
        raise SystemExit(-1)
    return args


urlArgs = args()
msURL = "https://login.microsoftonline.com/" + urlArgs.tid + "/oauth2/v2.0/token"
urlObj = {
    'client_id':urlArgs.cid,
    'scope': 'https://graph.microsoft.com/.default',
    'client_secret': urlArgs.cs,
    'grant_type':'client_credentials'
}


getIt = requests.post(msURL, data = urlObj)

#need to find some valid creds to test and refine results
print(getIt.text)
