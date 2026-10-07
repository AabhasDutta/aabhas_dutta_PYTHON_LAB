import re
text = "a ab abb abbb"
print(re.findall(r'ab+', text))  