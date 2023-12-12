# DemoStr.py

#print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p", 7))

print("demo.ppt".startswith("demo"))
print("demo.ppt".endswith("ppt"))
print("MBC2580".isalnum()) #앞의 문자열이 알파벳과 숫자로 구성되었는지 확인
print("MBC:2580".isalnum())
print("2580".isdecimal()) #앞의 문자열이 숫자로 구성되었는지 확인

data = "<<< spam and ham >>>"
result = data.strip("<> ") #결과값을 변수로 저장해서 가지고 있어야 지속 사용 가능(result에 저장)
print(data)
print(result)
result2 = result.replace("spam", "spam egg")
print(result2)
print("---리스트로 분리---")
lst = result2.split() # 공백문자를 기준으로 자동으로 잘라냄(split)
print(lst)
print("---하나의 문자열---")
print(":)".join(lst))
