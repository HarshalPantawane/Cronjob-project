import requests
import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

GOLD_API_URL = "https://www.goldapi.io/api/XAU/INR"
API_KEY = os.getenv("GOLD_API_KEY")
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN") 

sns = boto3.client("sns", region_name="us-east-1")

def get_gold_price():
    headers = {
        "x-access-token": API_KEY,
        "Content-type": "application/json"
    }
    response = requests.get(GOLD_API_URL, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")
    
    data = response.json()
    return data.get("price")

def send_notification(price):
    sns = boto3.client("sns", region_name="us-east-1")
    
    message = f"""
    
Gold Price Alert
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 
Price (INR): {price}
"""

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject="Gold Price Update"
    )   
    
def main():
    try:
        price = get_gold_price()
        print("Gold Price:", price)
        send_notification(price)
    except Exception as e:
        print("Error:", str(e))

if __name__=="__main__":
    main()          
            