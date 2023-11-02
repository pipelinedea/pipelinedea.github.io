# remove empty lines
find . -type f -name "202*.html" -exec perl -i -lne 'print if /\S/' {} \;

# remove justify from links
find . -type f -name "202*.html" -exec sed -i '' 's/style="white-space:pre-wrap;"//g' {} \;

# collapse div class line with following
find . -type f -name "202*.html" -exec sh -c 'awk "{ORS = /<div class=\"/ ? \"\" : \"\\n\"} 1" "{}" > temp && mv temp "{}"' \;

# collapse figure class line with following
find . -type f -name "202*.html" -exec sh -c 'awk "{ORS = /<figure class=\"/ ? \"\" : \"\\n\"} 1" "{}" > temp && mv temp "{}"' \;

# collapse figure line with following
find . -type f -name "202*.html" -exec sh -c 'awk "{ORS = /<\/figure>/ ? \"\" : \"\\n\"} 1" "{}" > temp && mv temp "{}"' \;

# remove crap
# python3 clean.py