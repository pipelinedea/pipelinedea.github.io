import os
import re

# Initialize an empty dictionary
url_dictionary_old = {}

# Read the contents of old_links.txt into a list
with open('old_links.txt', 'r') as file:
    links = file.readlines()

# Create the dictionary
for link in links:
    link = link.strip()  # Remove leading/trailing whitespace
    key = link.split('/')[-1]  # Get the last part after the last /
    url_dictionary_old[key] = link

# Initialize an empty dictionary
url_dictionary_new = {}

# Read the contents of new_links.txt into a list
with open('new_links.txt', 'r') as file:
    links = file.readlines()

# Create the dictionary
for link in links:
    link = link.strip()  # Remove leading/trailing whitespace
    key = link[11:][:-5].rstrip()  # Get the key based on the first 11 and last 5 characters stripped
    url_dictionary_new [key] = 'https://pipelinedea.github.io/' + link

html_directory = '.' 
# Loop through HTML files
for filename in os.listdir(html_directory):
    if filename.endswith(".html"):
        html_file_path = os.path.join(html_directory, filename)

        # Read the contents of the HTML file
        with open(html_file_path, 'r') as file:
            content = file.read()

        # Replace URLs based on the old dictionary with values from the new dictionary
        for key, value in url_dictionary_old.items():
            content = content.replace(value, url_dictionary_new.get(key, value))

        # Write the updated content back to the HTML file, overwriting it
        with open(html_file_path, 'w') as file:
            file.write(content)

        print(f"Updated {filename}")

print("URL replacements completed.")