import re

from collections import Counter


def task1_variant6_simple():
    with open('task1-en.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    print("Task 1 : Extract the following from English text")
    print("=" * 50)

    # 1.Extract all integers less than 10
    print("\n1. All integers less than 10 :")

    # Match integer pattern
    integer_pattern = r'(?<![-\d])(-?[0-9])(?![\d])'
    integers = re.findall(integer_pattern, text)

    # Convert to integers and filter
    integer_values = []
    for num_str in integers:
        try:
            num = int(num_str)
            if -9 <= num <= 9:
                integer_values.append(num)
        except ValueError:
            pass

    print(f"Found {len(integer_values)} integers less than 10")
    print(f"Complete list: {integer_values}")

    # Statistics
    counter = Counter(integer_values)
    print("\nDistribution statistics:")
    for num in sorted(counter.keys()):
        print(f"  Number {num}: {counter[num]} times")

    # 2.Extract all combinations containing both letters and numbers
    print("\n" + "=" * 50)
    print("\n2. All combinations containing both letters and numbers:")

    # Match words containing both letters and numbers
    alphanum_pattern = r'\b(?=[A-Za-z]*\d)(?=\d*[A-Za-z])[A-Za-z\d]+\b'
    alphanum_matches = re.findall(alphanum_pattern, text)

    print(f"Found {len(alphanum_matches)} combinations with both letters and numbers")
    print(f"Complete list: {alphanum_matches}")

    # Remove duplicates
    unique_alphanum = sorted(set(alphanum_matches))
    print(f"\n{len(unique_alphanum)} unique combinations after deduplication:")
    for item in unique_alphanum:
        print(f"  {item}")

    return integer_values, alphanum_matches


if __name__ == "__main__":
    integers, alphanum = task1_variant6_simple()