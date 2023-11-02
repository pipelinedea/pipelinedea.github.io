import os
import re

directory_path = '.'  # Change this to the directory containing your HTML files
html_files = [file for file in os.listdir(directory_path) if (file.startswith('202') and file.endswith('.html'))]

for file_name in html_files:
    inside_block = False
    output_lines = []

    with open(os.path.join(directory_path, file_name), "r") as file:
        for line in file:
            if 'image-block-outer-wrapper' in line:
                inside_block = True
            if '<img ' in line:
                pattern = r'<img[^>]*src="([^"]+)"[^>]*>'
                replacement = r'<img src="\1">'
                output_lines.append(re.sub(pattern, replacement, line))
            else:
                if not inside_block:
                    output_lines.append(line)
            if '</figure>    </div>' in line:
                inside_block = False
            if '<figcaption' in line:
                inside_block = False
    
    with open(os.path.join(directory_path, file_name), "w") as file:
        file.writelines(output_lines)
