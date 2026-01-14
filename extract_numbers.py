import pandas as pd
import requests
import re
import time
from bs4 import BeautifulSoup

df = pd.read_excel("SampleDataIntern.xlsx")
df["Mobile_Number"] = None

headers = {
    "User-Agent": "Mozilla/5.0"
}

def extract_phone_numbers(text):
    pattern = r"[6-9]\d{9}"
    phones = re.findall(pattern, text)
    return list(set(phones))

for index, row in df.iterrows():
    name = str(row["EnterpriseName"])
    district = str(row["District"])

    search_query = f"{name} {district}"
    search_query = search_query.replace(" ", "+")

    url = f"https://dir.indiamart.com/search.mp?ss={search_query}"

    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        phones = extract_phone_numbers(soup.text)

        if phones:
            df.at[index, "Mobile_Number"] = phones[0]
            print(f"Found: {phones[0]} for {name}")
        else:
            print(f"No number found for {name}")

        time.sleep(3)

    except Exception as e:
        print(f"Error for {name}: {e}")

df.to_excel("Final_With_PhoneNumbers.xlsx", index=False)
print("Completed. File saved as Final_With_PhoneNumbers.xlsx")
