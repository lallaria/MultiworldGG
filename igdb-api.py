from flask import Flask, request, jsonify
import os
import requests  # Changed from request to requests
import json
import importlib.util
from typing import Dict, Optional, Tuple
from datetime import datetime

# Get the user's home directory and convert to forward slashes
home_dir = os.path.expanduser('~').replace('\\', '/')
client_id_path = f"{home_dir}/.igdb/clientid"
key_path = f"{home_dir}/.igdb/key"

with open(client_id_path, 'r') as file:
    igdb_client_id = file.readline().strip()
with open(key_path, 'r') as file:
    igdb_key = file.readline().strip()

# url = f"https://id.twitch.tv/oauth2/token?client_id={igdb_client_id}&client_secret={igdb_key}&grant_type=client_credentials"
# response = requests.post(url)
# print(url)
# print(response.json())
# igdb_token = response.json()['access_token']
igdb_token = "ok558j0ne651nzmks56bnfp54apy5j"

def get_igdb_info(api: str, fields: str) -> None:
    """
    Fetches game keywords from IGDB API using the provided game name.
    """
    url = f"https://api.igdb.com/v4/{api}"
    headers = {
        'Client-ID': igdb_client_id,
        'Authorization': f'Bearer {igdb_token}',
        'Content-Type': 'application/json'
    }
    data = f'fields {fields};'
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        print(response.json())
        return
    else:
        print(response)
        return
    
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Call API')
    parser.add_argument('--api', type=str, help='Get api info')
    parser.add_argument('--fields', type=str, help='Use these fields, comma delimted')
    args = parser.parse_args()
    
    get_igdb_info(args.api, args.fields)