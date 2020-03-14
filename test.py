import app


# print(app.get_cross_list(1,2))

# arr = [5, 2, 4, 7, 3, 0, 6, 1] # local optima
# arr =[0, 2, 5, 7, 1, 3, 0, 6]   # local optima
# min_list = app.check_min_move(arr)
# print("min-list", min_list)

# arr =[2, 2, 5, 7, 1, 3, 0, 6]   # local optima
# min_list = app.check_min_move(arr)
# print("min-list", min_list)

# arr =[4, 2, 5, 7, 1, 3, 0, 6]   # local optima
# min_list = app.check_min_move(arr)
# print("min-list", min_list)

# print(app.check_min_move(arr))

# value = app.check_local_optima(arr,min_list)

# print("local optima check: ", value)

# number = 0

# for number in range(10):
#     if number == 5:
#         continue    # pass here

#     print('Number is ' + str(number))

# print('Out of loop')

arr =[0, 2, 5, 7, 1, 3, 0, 6]   # local optima
# min_list = app.check_min_move(arr)
# print("min-list", min_list)
# arr = [1, 2, 3, 4, 3, 2, 4, 7]
s1 = app.check_shoulder(arr)
print("eq: ", s1)


# list_1 = [{'unique_id':'001', 'key1':'AAA', 'key2':'BBB', 'key3':'EEE'}, 
#           {'unique_id':'002', 'key1':'AAA', 'key2':'CCC', 'key3':'FFF'}]
# list_2 = [{'unique_id':'001', 'key1':'AAA', 'key2':'DDD', 'key3':'EEE'},
#           {'unique_id':'002', 'key1':'AAA', 'key2':'CCC', 'key3':'FFF'}]
# pairs = zip(list_1, list_2)
# print(not any(x != y for x, y in pairs))
# False