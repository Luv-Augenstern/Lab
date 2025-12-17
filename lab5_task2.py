import re

with open('task2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all <img> tags with src attributes
img_pattern = r'<img[^>]*src=["\']([^"\']+)["\'][^>]*>'
img_links = re.findall(img_pattern, content)

# Remove duplicates and print results
unique_img_links = list(set(img_links))
for link in unique_img_links:
    print(link)

print(f"\nFound {len(unique_img_links)} unique image links")