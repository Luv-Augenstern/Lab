import re
import csv

with open('task3.txt', 'r') as f:
    items = f.read().split()

# Classify data using regular expressions
ids = [item for item in items if re.fullmatch(r'\d+', item)]
surnames = [item for item in items if re.fullmatch(r'[A-Z][a-zA-Z-]+', item)]
emails = [item for item in items if re.fullmatch(r'[\w.-]+@[\w.-]+\.\w+', item)]
dates = [item for item in items if re.fullmatch(r'\d{4}-\d{2}-\d{2}', item)]
urls = [item for item in items if re.fullmatch(r'https?://[\w.-]+\.\w+(?:/[\w.-]*)*', item)]

# Check if data is consistent
lengths = {len(ids), len(surnames), len(emails), len(dates), len(urls)}
if len(lengths) == 1:
    # Combine data and sort by ID
    data = sorted(zip(ids, surnames, emails, dates, urls), key=lambda x: int(x[0]))

    # Write to CSV
    with open('lab5_task3_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Surname', 'Email', 'Date', 'Website'])
        writer.writerows(data)

    print(f"Successfully saved {len(data)} records to lab5_task3_data.csv")
else:
    print("Error: Data is not consistent. Found:")
    print(f"  IDs: {len(ids)}, Surnames: {len(surnames)}, Emails: {len(emails)}")
    print(f"  Dates: {len(dates)}, URLs: {len(urls)}")