import re
text = "abc aXc a9c"
print(re.findall(r'a.c', text))  