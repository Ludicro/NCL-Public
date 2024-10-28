import requests
from datetime import datetime
import keyring

# Retrieve your GitHub token from the keyring
api_token = keyring.get_password('GitHub', 'Ludicro')

# Check if the token was retrieved successfully
if not api_token:
    print("API token not found in the keyring. Please set it first.")
else:
    response = requests.get(
        'https://api.github.com/events',
        headers={'Authorization': f'token {api_token}'}
    )
    
    if response.status_code == 200:
        events = response.json()  # Call the method to get the JSON data

        # Extract all dates from events
        all_dates = [datetime.fromisoformat(event['created_at'][:-1]).date() for event in events]

        # Print the array of dates
        print("All event dates:", all_dates)

        # Specify the date you're interested in (March 26, 2024)
        specific_date = datetime(2024, 3, 26).date()

        # Count events matching the specific date
        count = all_dates.count(specific_date)

        print(f'Total events on {specific_date}: {count}')
    else:
        print(f"Failed to retrieve events: {response.status_code} - {response.text}")
