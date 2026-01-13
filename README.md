# 📞 Business Mobile Number Extractor

This project extracts publicly available mobile phone numbers for business establishments in Udupi using their business names and district information.

## 🛠 Tools Used

* Python
* pandas
* requests
* BeautifulSoup
* regex

## 📂 Files

* `SampleDataIntern.xlsx` – Input dataset
* `extract_numbers.py` – Python script to fetch mobile numbers
* `Final_With_PhoneNumbers.xlsx` – Output file with extracted numbers

## ▶ How to Run

1. Install dependencies:

   ```
   pip install pandas requests beautifulsoup4 openpyxl
   ```

2. Run the script:

   ```
   python extract_numbers.py
   ```

3. The output file will be created as:

   ```
   Final_With_PhoneNumbers.xlsx
   ```

## 🧠 Approach

The script automatically searches business directories such as IndiaMART using business names and district details.
It extracts valid Indian mobile numbers using pattern matching techniques and stores them in the dataset.
