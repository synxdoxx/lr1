#1
import math
a = 7
b = 3.7
print(a + b, a - b, a * b, a / b)
print(type(a / b))
sq = math.pi * 5 * 5
print(f"Площадь круга с радиусом 5: {round(sq, 2)}")

#2
text = ' Hello, Python! '
text1 = text.strip()
print(text1)
text2 = text1.replace('!', '?')
print(text2)
text3 = text2.upper()
print(text3)

txt = text.strip().lower()
assert(txt == 'hello, python!')

#3
nums = [7, 2, 5]
nums.append(4)
print(nums)
nums.insert(1, 10)
print(nums)
nums.extend([1, 1, 1])
print(nums)
nums.remove(7)
print(nums)
dele = nums.pop()
print(nums, dele)
nums.sort()
print(nums)
nums.reverse()
print(nums)
cnt = nums.count(2)
print(cnt)
ind = nums.index(1)
print(ind)
nums1 = nums.copy()
nums2 = nums.copy()
nums.clear()
print(nums, nums1, nums2)

#4
t = (1, 2, 3)
t1 = (4, 5)
t2 = t + t1
print(t2)
print(t2.count(2))
print(t2.index(4))
print(t)

#5
values = [3, 1, 3, 2, 1, 5, 2]
unique_values = set(values)
print(len(unique_values))
other = {2, 4, 5}
print(unique_values & other)
print(unique_values | other)
print(unique_values - other)
print(other - unique_values)

#6
scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores['Bob'] = 90
print(scores.get('Dave'))
print(scores.get('Alice'))
scores.pop('Alice')
print(scores)
print(scores.keys())
print(scores.values())

#7
from collections import Counter

text ="""
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
print("#1")
text.strip()
text = text.lower()
print(text)
print("#2")
text = text.replace("!", ".")
print(text)
print("#3")
tt = text.split(".")
tt.pop(-1)
for i in range(len(tt)):
    tt[i] = tt[i].replace("\n", "")
    tt[i] = tt[i].lstrip()
print(tt)
print("#7")
print(tt[0].startswith("python "), tt[0].endswith("language"))
print("#5")
tt[0] = tt[0].split(" ")
print(tt)
print("#6")
print(tt[0].count("python"))

print("#8")
c = 0
ca = 0
for i in range(len(tt[0])):
    c += len(tt[0][i])
    ca += tt[0][i].count("a")

c += len(tt[1])
c += len(tt[2])
ca += tt[1].count("a")
ca += tt[2].count("a")
print(c, ca, tt[1].find("data"))


print("#9")

tt[0] = "-".join(tt[0])
tt[1] = "-".join(tt[1].split())
tt[2] = "-".join(tt[2].split())
print(tt)

print("#10")
dd = Counter(text.split())
print(dd)
print("#11")
def clean_text(n):
    n.strip()
    n.rstrip()
    n.lstrip()
    zn = [",", ".", "!", "?", "...", "  "]
    for i in zn:
        while i in n:
            n = n.replace(i, "", 1)
    if n[0] == " ":
        n = n[1:]
    if n[-1] == " ":
        n = n[0:-1]
    return n

p = "   ghhhj sdkffhguhjk   fkigjfg lkg?"
print(clean_text(p))