import re
p = re.compile("ca.e")
# . : 하나의 문자
# ^ : 문자열의 시작 (^de) desk destination
# $ : 문자열의 끝 (se%) case base

def print_match(m):
    if m:
        print(m.group())
        print(m.string)
        print(m.start())
        print(m.end())
        print(m.span())
    else:
        print("매칭되지 않음")


# m = p.match("caser") # 문자열의 처음부터가 일치하는지 확인 
# print_match(m)

m = p.search("good care")
print_match(m)

lst = p.findall("case of care")
print(lst)

#compile
#match search findall
