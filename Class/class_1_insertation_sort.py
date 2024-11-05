my_list = [5,3,6,1,2,4]

# for j in my_list[1:]:
for i in range(1, len(my_list)):
    key = my_list[i]
    j = i-1

    while j>=0 and my_list[j]>key:
        my_list[j+1] = my_list[j]
        j = j-1

    my_list[j+1] = key

print(my_list)