def find_max(num_list):
    max_num = num_list[0]       # first pass through loop, first number is assumed maximum
    for num in num_list:
        if num > max_num:
            max_num = num       # update maximum number if this pass thru the loop returns a higher value
    return max_num

print(find_max([4, 9, 1, 17, 2]))   #Output : 17  
print(find_max([-5, -9, -2, -12])) #Output :  -2  
print(find_max([42]))  #Output : 42
