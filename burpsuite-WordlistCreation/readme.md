beginning of my project to create ongoing wordlists based off burpsuite projects

under proxy --> http history --> select all --> right click and 'copy urls' --> save this to 'infile'
filter:
- add what you want here, i typically filter out css, gif, png, woff, etc.
- i also will keep it to in-scope items, but that's up to you

how to run:
python wordlist.py infile outfile
