import requests
import os
from datetime import datetime
from notifier import send_email

API_KEY = os.getenv("GOLD_API_KEY")
API_URL = "https://www.goldapi.io/api/XAU/INR"

def fetch_gold_price():
    if not API_KEY:
        print("Error: GOLD_API_KEY not set")
        return None
    
    try:
        headers = {
            "x-access-token": API_KEY
        }
        
        response = requests.get(API_URL, headers=headers)
        
        if response.status_code == 200:
            return response.json().get("price")
        else:
            print(f"Failed to fetch price: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    
def main(): 
    try:
        price = fetch_gold_price()
        
        if price:
            message = f"[{datetime.now()}] Gold Price (INR): {price}" 
            print(message)
            
            send_email(message)
        else:
            print("No data received")
    except Exception as e:
        print(f"Error in main: {e}")
        
if __name__ == "__main__":
    main()               