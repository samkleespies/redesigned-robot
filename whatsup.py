sam_age = 20            # integer
jordan_age = 24.1       # float
is_jordan_sick = True   # boolean
derger = "ben"          # string
percentage = 0.5

#       0  1  2  3  4
list = [100, 200, 225, 250, 300]
V = [list[i] * percentage for i in range(len(list))]

print("How old is sam", sam_age)
print("How old is jordan exactly", jordan_age)
print("Is this mofo sick rn?", is_jordan_sick)
print("Is a derger:", derger)

print(V)
