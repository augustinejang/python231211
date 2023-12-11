# List, Tuple, Set, Dict 생성
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 각 데이터 타입의 내용 출력
print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dict:", my_dict)

# List와 Tuple 비교
print("List와 Tuple 비교:", my_list == list(my_tuple))

# Set과 List의 합집합, 교집합 출력
union_set = my_set.union(set(my_list))
intersection_set = my_set.intersection(set(my_list))

print("Set과 List의 합집합:", union_set)
print("Set과 List의 교집합:", intersection_set)

# Dict에서 특정 키의 값 출력
key_to_lookup = 'c'
value = my_dict.get(key_to_lookup, "키를 찾을 수 없습니다.")
print(f"Dict에서 '{key_to_lookup}' 키의 값:", value)
