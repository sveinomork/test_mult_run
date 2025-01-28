from python_high_usage import consume_cpu_and_memory
from generate_bat import gen_bat_file2
import click
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# URL of the dividend page
url = "https://www.gjensidige.com/investor-relations/dividend"

# Fetch the web page content
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the table containing dividend data
dividend_table = soup.find("table", class_="table")

# Initialize a list to store dividend data
dividends = []

# Extract rows from the table
rows = dividend_table.find_all("tr")[1:]  # Skip the header row

for row in rows:
    columns = row.find_all("td")
    
    # Extract the required data from each column
    price_per_share = columns[0].text.strip()
    ex_date = columns[1].text.strip()
    payout_date = columns[2].text.strip()
    
    # Store the data in a dictionary
    dividend = {
        "Price per share": price_per_share,
        "Ex-date": ex_date,
        "Payout date": payout_date
    }
    
    # Add the dictionary to the list
    dividends.append(dividend)

# Print the extracted data
for dividend in dividends:
    print(dividend)


























@click.command()
@click.argument('memory',type=int)
@click.argument('processor',type=int)
@click.argument('sleep',type=int)
def cli(memory,processor,sleep):
    consume_cpu_and_memory(memory,processor,sleep)

if __name__ == "__main__":
    gen_bat_file2(Path('python_high_usage.py'),Path('performance1.bat'),memory=10**7,processor=10**7,sleep=60)

    print("starting")
    cli()
