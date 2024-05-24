#1
# def filter(lst3):
#     list = []
#     for x in lst3:
#         if type(x) == int:
#             list.append(x)
#     return list
# print(filter([1, 2, 3, "a", "b", 4])) #-----> [1,2,3,4]
# print(filter([1, "a", "b", 0, 15]))
# print(filter([1, 2, "aasf", "1", "123", 123]))
 #2
# def split(nums):
#     numbers = nums // 2
#     if nums % 2 != 0:
#         return [numbers, numbers + 1]
#     else:
#         return [numbers, numbers]
# print(split(4))#--->[2,2]
# print(split(10))
# print(split(11))
# print(split(-9))
 #3
# def jazzify(lst):
#     list1 = []
#     for x in lst:
#         if '7' in x:
#             list1.append(x)
#         else:
#             list1.append(x + '7')
#     return list1
# print(jazzify(["G", "F", "C"]))#➞ ["G7", "F7", "C7"]
# print(jazzify(["Dm", "G", "E", "A"]))
# print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
# print(jazzify([]))
 #4
# def clone(lst):
#     lst2 = []
#     for x in lst:
#         lst2.append(x)
#     lst2.extend([lst])
#     return lst2
# print(clone([1,1]))#------->[1, 1, [1, 1]]
# print(clone([1, 2, 3]))
# print(clone(['x', 'y']))
 #5
# def find_odd(lst):
#     for x in lst:
#         y = lst.count(x)
#         if y % 2 != 0:
#             return x
#
#
#
# print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])) #----> -1
# print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))#----> 5
# print(find_odd([10]))
 #6
# def move_to_end(lst1,lst2):
#     for x in lst1:
#         if lst2 == x:
#             lst1.remove(lst2)
#             lst1.append(lst2)
#
#     return lst1
#
#
# print(move_to_end([1, 3, 2, 4, 4, 1], 1)) #---> [3, 2, 4, 4, 1, 1]
# # Move all the 1s to the end of the array.
# print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))# ➞ [7, 8, 1, 2, 3, 4, 9]
# print(move_to_end(["a", "a", "a", "b"], "a"))# ➞ ["b", "a", "a", "a"]
#
 #7
# def find_even_nums(num):
#     num2 = []
#     for x in range(1,num + 1):
#         if x % 2 == 0:
#             num2.append(x)
#     return num2
#
#
# print(find_even_nums(8))
# print(find_even_nums(4))
# print(find_even_nums(2))
 #8
# def next_in_line(lst, num):
#     if lst == []:
#         return "No list has been selected"
#     else:
#         lst.append(num)
#         lst.pop(0)
#         return lst
#
#
# print(next_in_line([5, 6, 7, 8, 9], 1))# ➞ [6, 7, 8, 9, 1]
# print(next_in_line([7, 6, 3, 23, 17], 10))
# print(next_in_line([1, 10, 20, 42], 6))
# print(next_in_line([], 6))# ➞ "No list has been selected"
 #9
# def add_indexes(lst):
#     index = 0
#     lst1 = []
#     for i in lst:
#         lst1.append(i + index)
#         index += 1
#     return lst1
#
#
# print(add_indexes([0, 0, 0, 0, 0]))#➞ [0, 1, 2, 3, 4]
# print(add_indexes([1, 2, 3, 4, 5]))
# print(add_indexes([5, 5, 5, 5, 5]))
 #10
# def return_only_integer(lst):
#     lst1 = []
#     for x in lst:
#         if type(x) == int:
#             lst1.append(x)
#     return lst1
# print(return_only_integer([9, 2, "space", "car", "lion", 16])) #➞ [9, 2, 16]
# print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))
# print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))
# print(return_only_integer(["String",  True,  3.3,  1]))
#
 #11
# def return_only_string(lst):
#     lst1 = []
#     for x in lst:
#         if type(x) == str or float:
#             lst1.append(x)
#     return lst1
# print(return_only_string([9, 2, "space", "car", "lion", 16])) #➞ [9, 2, 16]
# print(return_only_string(["hello", 81, "basketball", 123, "fox"]))
# print(return_only_string([10, "121", 56, 20, "car", 3, "lion"]))
# print(return_only_string(["String",  True,  3.3,  1]))

