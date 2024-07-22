import requests
import json
import time
from datetime import datetime

# OpenSky Network API URL
API_URL = "https://opensky-network.org/api/states/all"

def fetch_flight_data():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def process_flight_data(data):
    if data and 'states' in data:
        flights = data['states']
        for flight in flights:
            icao24 = flight[0]
            callsign = flight[1]
            origin_country = flight[2]
            time_position = flight[3]
            last_contact = flight[4]
            longitude = flight[5]
            latitude = flight[6]
            altitude = flight[7]
            on_ground = flight[8]
            velocity = flight[9]
            heading = flight[10]
            vertical_rate = flight[11]
            print(f"Flight {callsign} ({icao24}) from {origin_country}")
            print(f"Position: ({latitude}, {longitude}) at {altitude} meters")
            print(f"On ground: {'Yes' if on_ground else 'No'}")
            print(f"Velocity: {velocity} m/s, Heading: {heading}, Vertical Rate: {vertical_rate} m/s")
            print(f"Last contact: {datetime.utcfromtimestamp(last_contact)} UTC")
            print("="*40)
    else:
        print("No flight data available")

def main():
    while True:
        flight_data = fetch_flight_data()
        process_flight_data(flight_data)
        # Wait for 60 seconds before fetching data again
        time.sleep(60)

if __name__ == "__main__":
    main()
