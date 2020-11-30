# $ ==> End of Line
# ^ ==> Search ofr just any character
# + ==> Unlimited entries after


# E-mail Validator

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = 'b@b.com'
a = pattern.search(string)
print(a)
print(a.group())


# O/P: <re.Match object; span=(0, 7), match='b@b.com'>
# b@b.com
# b@b.com
