def build_list(item, number):
    my_list = []
    for _ in range(0, number):
        my_list.append(item)
    
    return my_list

print(build_list("mum", 5))