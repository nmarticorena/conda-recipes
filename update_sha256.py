#!/usr/bin/env python3
import hashlib
import re
import sys
import urllib.request

if len(sys.argv) != 2:
    print("Usage: update_sha256.py <path/to/recipe.yaml>")
    sys.exit(1)

recipe_file = sys.argv[1]

with open(recipe_file) as f:
    content = f.read()

url_match = re.search(r"url:\s*(\S+)", content)
if not url_match:
    raise ValueError("No URL found in recipe")

url = url_match.group(1)
print(f"Downloading: {url}")

sha256 = hashlib.sha256()
with urllib.request.urlopen(url) as response:
    while chunk := response.read(8192):
        sha256.update(chunk)

digest = sha256.hexdigest()
print(f"sha256: {digest}")

new_content = re.sub(r"(sha256:\s*).*", rf"\g<1>{digest}", content)

with open(recipe_file, "w") as f:
    f.write(new_content)

print(f"Updated {recipe_file}")
