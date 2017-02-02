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
