import re

def extract_data_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    # Date pattern
    date_pattern = r'\s(\d{1,4}[-/.\s]\d{1,2}[-/.\s]\d{1,4})'

    # Email pattern
    email_pattern = r'\s([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'

    # Website URL pattern
    url_pattern = r'\s(https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[a-zA-Z0-9./?=%&_-]*)?)'

    # Find all matches
    dates = re.findall(date_pattern, content)
    emails = re.findall(email_pattern, content)
    urls = re.findall(url_pattern, content)

    # Deduplicate and take first 5
    unique_dates = []
    seen_dates = set()
    for date in dates:
        if date not in seen_dates and len(unique_dates) < 5:
            unique_dates.append(date)
            seen_dates.add(date)

    unique_emails = []
    seen_emails = set()
    for email in emails:
        if email not in seen_emails and len(unique_emails) < 5:
            unique_emails.append(email)
            seen_emails.add(email)

    unique_urls = []
    seen_urls = set()
    for url in urls:
        # Ensure URL is complete
        if url not in seen_urls and len(unique_urls) < 5:
            unique_urls.append(url)
            seen_urls.add(url)

    return unique_dates, unique_emails, unique_urls


def main():
    file_path = 'task_add.txt'

    try:
        dates, emails, urls = extract_data_from_file(file_path)

        print("Dates found:")
        for i, date in enumerate(dates, 1):
            print(f"{i}. {date}")

        print("\nEmail addresses found:")
        for i, email in enumerate(emails, 1):
            print(f"{i}. {email}")

        print("\nWebsite addresses found:")
        for i, url in enumerate(urls, 1):
            print(f"{i}. {url}")


    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()