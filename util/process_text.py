import re
import json

# Input raw text (replace this string with your full text block)
raw_text = """
TEXT
"""  # <-- Replace with the full text you provided

# Split the text into lines and prepare a list to hold parsed entries
lines = raw_text.strip().split("\n")
entries = []

for line in lines:
    # Split by tabs (multiple tabs allowed)
    parts = re.split(r'\t+', line)

    # Default fields
    name, location, email, phone = "", "", "", ""

    # Assign based on how many parts were parsed
    if len(parts) == 4:
        name, location, email, phone = parts
    elif len(parts) == 3:
        name, location, email = parts
    elif len(parts) == 2:
        name, location = parts

    # Extract phone number using regex
    phone_match = re.search(r'[\d\(\)\-]+(?: ?x\d+)?', phone)
    phone_number = phone_match.group() if phone_match else ""

    # Append structured entry
    entries.append({
        "Name": name.strip(),
        "Location": location.strip(),
        "Email": email.strip(),
        "Phone Number": phone_number
    })

# Export to JSON file
with open("extracted_data.json", "w") as f:
    json.dump(entries, f, indent=4)

print("Conversion complete. JSON saved as 'exctracted_data.json'.")
