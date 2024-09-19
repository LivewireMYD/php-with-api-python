import requests
from datetime import datetime, date,timedelta



import pandas as pd
import requests
from datetime import datetime
import subprocess
# Function to check if today is the user's birthday


# Function to send birthday wish via API
def send_birthday_wish(name, phone_number,content):
    api_url = "http://127.0.0.1:3000/send/message"  # Replace with actual API URL
    headers = {
      'Content-Type': 'application/json'  # Ensure the content type is JSON
    }
    payload = {
        
        'phone': "+91"+str(phone_number) +'@s.whatsapp.net',
        'message': f"{content} - {name}!"
    }
    print(payload)
    # Sending POST request with JSON body
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print(f"Sent due date to {name} ({phone_number}) successfully.")
    else:
        print(f"Failed to send due date to {name} ({phone_number}). Status Code: {response.status_code}")

# Function to process the Excel file and send wishes
def send_wishes_from_excel():
        url="http://localhost/restapi12/index.php"

        headers = {
            'Authorization': '123456'
        }

        # Make the GET request
        info = requests.get(url, headers=headers)
        info = info.json()
        data=info["data"]
        print(data)

        today=date.today()
        print(today)

        for data1 in data:
            name=data1["name"]
            phone_number=data1["phoneno"]
            duedate = datetime.strptime(data1["duedate"], "%Y-%m-%d").date()
            due=today - duedate
            print(duedate)
            
            if duedate==today+timedelta(days=2):
                    content="due date 2 dates"
                    print(content)
                    send_birthday_wish(name, phone_number,content)
            if duedate==today+timedelta(days=1):
                     
                    content="due date 1 dates"
                    print(content)
                    send_birthday_wish(name, phone_number,content)
            if duedate==today:
                        content="due date today dates"
                        print(content)
                        send_birthday_wish(name, phone_number,content)
            if duedate==today+timedelta(days=-1):    
                    content="your due date is finished"
                    print(content)
                    send_birthday_wish(name, phone_number,content)
            else:
                  print("one data mismatch to this")
            
                 
  
def run_background_command(command):
    try:
        # Run the command in the background using subprocess
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Running command: {' '.join(command)}")
    except Exception as e:
        print(f"Failed to start background process: {e}")

# Example usage
if __name__ == "__main__":
    # Command to run in the background (replace with your actual command)
    background_command = ["windows-amd64"]  
    
    # Run the command in the background
    run_background_command(background_command)


send_wishes_from_excel()
