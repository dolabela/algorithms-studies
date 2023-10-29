
# O(n)
def is_all_unique(input_str: str):
    seen_set = set()
    for character in input_str:
        if character in seen_set:
            return False
        else:
            seen_set.add(character)
    return True
print(is_all_unique("abcdefghiijklm"))
print(is_all_unique("abcdefghijklm"))

# O(nlogn) (without extra data structure)
def is_all_unique_without_extra_structure(input_str: str):
    input_str = sorted(input_str)
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i-1]:
            return False
    return True


print(is_all_unique_without_extra_structure("abcdefghiijklm"))
print(is_all_unique_without_extra_structure("abcdefghijklm"))

# TODO: Create automated test with time count