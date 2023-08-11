import requests

def get_random_activity():
    url = "https://www.boredapi.com/api/activity"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        activity = data.get("activity", "No activity suggestion available.")
        return activity
    else:
        return "Failed to retrieve activity suggestion."

if __name__ == "__main__":
    suggested_activity = get_random_activity()
    print("Suggested Activity:", suggested_activity)
