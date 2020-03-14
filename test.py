import app


# print(app.get_cross_list(1,2))

# arr = [5, 2, 4, 7, 3, 0, 6, 1] # local optima
arr =[0, 2, 5, 7, 1, 3, 0, 6]   # local optima
min_list = app.check_min_move(arr)
print(min_list)

arr =[2, 2, 5, 7, 1, 3, 0, 6]   # local optima
min_list = app.check_min_move(arr)
print(min_list)

arr =[4, 2, 5, 7, 1, 3, 0, 6]   # local optima
min_list = app.check_min_move(arr)
print(min_list)

# print(app.check_min_move(arr))

# value = app.check_local_optima(arr,min_list)

# print("local optima check: ", value)

# number = 0

# for number in range(10):
#     if number == 5:
#         continue    # pass here

#     print('Number is ' + str(number))

# print('Out of loop')


# app.check_shoulder(arr)
