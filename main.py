# 1
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# kop = map(lambda value:value * 3,sonlar)
# print(list(kop))

# 2
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# kva = list(map(lambda value: value ** 2,sonlar))
# print(kva)

# 3
# matn = ['a','b','c','d']
# upp = map(str.upper,matn)
# print(list(upp))

# 4
# names = ['Toxir','Ali','Vali','Bakir']
# get_len = map(len,names)
# print(list(get_len))

# 5
# sonlar = [ -3, -6, -7, -10]
# musbat = map(lambda value:value - 2*(value),sonlar)
# print(list(musbat))

# 6
# narxlar = [100,500,462,242,641,630]
# add = list(map(lambda value:value + (value / 100) * 15,narxlar))
# print(add)

# 7
# def get_num(value:list):
#     if value % 2 == 0:
#         return 0
#     elif value % 2 != 0:
#         return value
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# toq = map(get_num,sonlar)
# print(list(toq))

# 8
# royxat = ['salom','gap','idea']
# add = list(map(lambda value:value + '!',royxat))
# print(add)

# 9
# sonlar = [-10, -5, -2, 0, 1, 3, 5, 7, 10, -8, 15, -3, 20, 0, 25]
# ceperate = list(filter(lambda value: value % 2 == 0,sonlar))
# print(ceperate)

# 10
# sonlar = [-10, -5, -2, 0, 1, 3, 5, 7, 10, -8, 15, -3, 20, 0, 25]
# ten = list(filter(lambda value: value > 0 , sonlar))
# print(ten)