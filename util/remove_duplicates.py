import json

input_file = 'input_file.json'
output_file = 'output_file.json'

with open(input_file, 'r') as f:
    data = json.load(f)

seen = set()
unique_items = []
duplicates = []

for item in data:
    name = item.get('Name', '').strip().lower()
    if name in seen:
        duplicates.append(item)
    else:
        seen.add(name)
        unique_items.append(item)

print(f"Found {len(duplicates)} duplicates:")
for d in duplicates:
    print(d)

with open(output_file, 'w') as f:
    json.dump(unique_items, f, indent=4)

print(f"\nUnique entries written to {output_file}")
