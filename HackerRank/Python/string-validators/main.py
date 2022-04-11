s = "123"

result = {"alphanumeric": False, "alphabetic": False, "lowercase": False, "uppercase": False, "numeric": False}
for l in str(s):
    if l.isalnum():
        result["alphanumeric"] = True
    if l.isalpha():
        result["alphabetic"] = True
    if l.isdigit():
        result["numeric"] = True
    if l.islower():
        result["lowercase"] = True
    if l.isupper():
        result["uppercase"] = True


print(result["alphanumeric"])
print(result["alphabetic"])
print(result["numeric"])
print(result["lowercase"])
print(result["uppercase"])
