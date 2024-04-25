import time
import csv
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime

# Constants
WAIT_TIME = 30  # The time interval between checking different numbers should be adjusted based on your internet speed.

# Function to check if a number is available on WhatsApp
def is_number_available(driver, number, csv_writer):
    # Get the HTML source of the page
    checkingpagesrc = driver.page_source

    # Check if the specified HTML code snippet is present in the page source
    if (
        '<span dir="ltr" aria-label="" class="_ao3e" style="min-height: 0px;">Messages are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Click to learn more</span>'
        in checkingpagesrc
    ):
        print(number + " is Available!")
        csv_writer.writerow([number, "Available"])
    else:
        print(number + " is not Available!")
        csv_writer.writerow([number, "Not Available"])


# ASCII art for introduction
introart = """
██     ██  █████   ██████ ██   ██ ███████  ██████ ██   ██ ███    ███  █████  ████████ ███████ 
██     ██ ██   ██ ██      ██   ██ ██      ██      ██  ██  ████  ████ ██   ██    ██    ██      
██  █  ██ ███████ ██      ███████ █████   ██      █████   ██ ████ ██ ███████    ██    █████   
██ ███ ██ ██   ██ ██      ██   ██ ██      ██      ██  ██  ██  ██  ██ ██   ██    ██    ██      
 ███ ███  ██   ██  ██████ ██   ██ ███████  ██████ ██   ██ ██      ██ ██   ██    ██    ███████ 
                                                                                              
                                                                                              
"""

# Function to generate CAPTCHA for user verification
def generate_captcha():
    # Generate two random numbers
    num1, num2 = random.randint(1, 9), random.randint(1, 9)

    # Compute the sum
    captcha_sum = num1 + num2

    while True:
        # Ask the user for input
        # time.sleep(10)
        try:
            user_input = int(
                input(f"Please enter the sum {num1} + {num2} to proceed: ")
            )
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        # Check if the user's input is correct
        if user_input == captcha_sum:
            print(
                "CAPTCHA successfully solved! WhatsApp number verification process initiated."
            )
            break
        else:
            print("CAPTCHA failed. Please try again.")


# Main program starts here
print(introart)
print("WACheckmate - WhatsApp Bulk Number Checker & Validator Tool\n")
print(
    "WACheckmate is a bulk WhatsApp number checking tool crafted with Python and utilizing Selenium.\n"
)
print("1. Configure Parameters and Initiate Automation:")
print(
    "- Adjust the WAIT_TIME parameter to match your internet speed (default is 30 seconds)."
)
print("- Press the enter button to start the automation process.")

print("\n2. Log into WhatsApp Account and Solve Captcha:")
print("- Scan the provided QR code to log into your WhatsApp account.")
print(
    "- After logging into WhatsApp, solve the basic captcha through the terminal when prompted."
)

print("\n3. Validate Numbers with Country Code:")
print(
    "- Ensure that numbers in the numbers.txt file include the country code format, like +918516853332 (where +91 represents the country code)."
)
print(
    "- The script will then extract and validate each number listed in the numbers.txt file."
)

print("\n4. Results:")
print(
    "- After validation, the results will be saved in a CSV file within the folder.\n"
)

input("Please press Enter key to continue.")

# WhatsApp Web URL
base_url = "https://web.whatsapp.com"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open WhatsApp Web and generate CAPTCHA
driver.get(base_url)
time.sleep(10)  # Wait to login into WhatsApp!
print("Please solve the CAPTCHA only after logging into WhatsApp Web.")
generate_captcha()

# Generate CSV file name with microseconds
csvseconds = datetime.now().microsecond
csvfilename = f"WACheckmate_{csvseconds}.csv"

# Read numbers from file and write availability status to CSV
with open("numbers.txt", "r") as file, open(csvfilename, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Number", "Status"])  # Header row
    for line in file:
        number = line.strip()

        # Construct URL to open chat with the number
        chat_url = f"https://web.whatsapp.com/send/?phone={number}&text&type=phone_number&app_absent=0"

        # Open chat with the number
        driver.get(chat_url)
        time.sleep(WAIT_TIME)
        is_number_available(driver, number, csv_writer)

# Close the WebDriver session
driver.quit()
print(
    f"WhatsApp number checking completed! The results have been saved into {csvfilename}.csv"
)
