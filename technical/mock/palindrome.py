
def palindrome(string):
    mid = len(string) / 2
    if len(string) % 2 == 0:
        left_start = mid - 1
        right_start = mid

    else:
        right_start = mid + 1
        left_start = mid - 1

    for x in range(mid):

        if string[left_start - x] != string[right_start + x]:
           return False
    return True

print palindrome("franklin")
print palindrome("racecar")
print palindrome('here')
print palindrome("ezze")
