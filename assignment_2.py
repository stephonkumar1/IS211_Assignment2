"Stephon Kumar"
"Assignment 2"

import argparse
import urllib.request
import logging
import datetime

def fetch_data(url):
    """Retrieve data from the given URL."""
    try:
        response = urllib.request.urlopen(url)
        return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching data: {e}")
        exit()

def process_data(file_content):
    """Process the data and create a dictionary of person information."""
    person_data = {}
    lines = file_content.splitlines()

    for line_num, line in enumerate(lines, start=1):
        try:
            person_id, name, birthday_str = line.split(',')
            birthday = datetime.datetime.strptime(birthday_str, '%d/%m/%Y').date()
            person_data[person_id] = (name, birthday)
        except ValueError:
            logging.error(f"Error processing line #{line_num} with data: {line}")

    return person_data

def display_person(person_id, person_data):
    """Display information about a person based on their ID."""
    if person_id in person_data:
        name, birthday = person_data[person_id]
        print(f"Person #{person_id} is {name} with a birthday of {birthday.strftime('%Y-%m-%d')}")
    else:
        print(f"No user found with ID #{person_id}")

def main(url):
    """Main entry point."""
    print(f"Running main with URL = {url}...")

    # Fetch data from the provided URL
    file_content = fetch_data(url)

    # Process the data and create a dictionary of person information
    person_data = process_data(file_content)

    # Allow the user to interactively look up person information by ID
    while True:
        try:
            user_input = int(input("Enter an ID to lookup (enter a negative number or 0 to exit): "))
            if user_input <= 0:
                break
            display_person(user_input, person_data)
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

if __name__ == "__main__":
    """Main entry point."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    
    # Run the main program with the provided URL
    main(args.url)
