import re

input_file = "combined_cleaned1.txt"
output_file = "combined_cleaned2.txt"

cleaned_lines = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        # Remove leading/trailing spaces
        cleaned = line.strip()

        # Remove all English words (A-Z, a-z)
        cleaned = re.sub(r"[A-Za-z]+", "", cleaned)

        # Remove extra spaces created after removing English
        cleaned = cleaned.strip()

        # Keep only non-empty lines
        if cleaned != "":
            cleaned_lines.append(cleaned)

# Save cleaned file
with open(output_file, "w", encoding="utf-8") as f:
    for line in cleaned_lines:
        f.write(line + "\n")

print("Finished! All English words removed.")
