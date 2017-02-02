#
# def is_palindrome(string):
#     mid = len(string) / 2
#     if len(string) % 2 == 0:
#         left_start = mid - 1
#         right_start = mid
#
#     else:
#         right_start = mid + 1
#         left_start = mid - 1
#
#     for x in range(mid):
#
#         if string[left_start - x] != string[right_start + x]:
#            return False
#     return True

def palindrome(string):
    x = 0
    y = -1
    for x in range(len(string) / 2):
        if string[x] != string[y]:
            return False
        x += 1
        y -= 1
    return True


def with_spaces(string):
    no_space_string = "".join(string.split(" "))
    return palindrome(no_space_string)

print palindrome("franklin")
print palindrome("racecar")
print palindrome('here')
print palindrome("ezze")
