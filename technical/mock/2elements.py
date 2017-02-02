# def adding_up(array, k):
#     done = []
#     x = 0
#     while x < len(array):
#         first = array[x]
#         if first not in done:
#             y = x + 1
#             while y < len(array):
#                 second = array[y]
#                 if first + second == k:
#                     return True
#                 done.append(array[x])
#                 y += 1
#         x += 1
#     return False

def adding_up(array, k):
    table = {}
    for n in array:
        difference = k - n
        if not(n in table):
            table[n] = difference
        if difference in table:
            print difference
            return True
    return False

array = [1,4,8,8]
k = 10

def compliment(array, k):
    for x in range(len(array) - 1):
        last = array.pop()
        if (k - last) in array:
            return True
    return False

zarray = [2,3,5,6,8,14,20]
zk = 7

print compliment(array, k)
print compliment(zarray, zk)
