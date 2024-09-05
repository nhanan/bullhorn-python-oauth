from auth import start
import requests
import threading

# Set up the initial values
swimlane = # INSERT SWIMLANE
corp_id = # INSERT CORP ID
rest_url = f"https://rest{swimlane}.bullhornstaffing.com/rest-services/{corp_id}"

# Function to refresh BhRestToken
def refresh_bhresttoken():
    global BhRestToken
    global headers
    BhRestToken = start()  # Call the start function to get a new BhRestToken
    headers = {"BhRestToken": BhRestToken}
    print("BhRestToken refreshed.")
    
    # Schedule the next token refresh in 25 minutes (1500 seconds)
    threading.Timer(1500, refresh_bhresttoken).start()

# Initialize the BhRestToken and headers
refresh_bhresttoken()

## INSERT CODE HERE ##
