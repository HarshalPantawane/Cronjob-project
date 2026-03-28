

import requests
import os
from datetime import datetime
from notifier import send_email

API_KEY = os.getenv("GOLD_API_KEY")
API_URL = "https://www.goldapi.io/api/XAU/INR"

def fetch_gold_price():
    headers = {
        "x-access-token": API_KEY
        
    }
    
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("price")
    else:
        print("failed to fetch price")
        return None
    
def main(): 
    price = fetch_gold_price()
    
    if price:
        message = f"[{datetime.now()}] Gold Price (INR): {price}" 
        print(message)
        
        send_email(message)
    else:
        print("No data received")
        
if __name__ == "__main__":
    main()               