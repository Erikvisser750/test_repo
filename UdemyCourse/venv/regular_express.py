import re
#regex101.com
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'erikvisser750@hotmail.com'

a = pattern.search(string)
print(a.group())