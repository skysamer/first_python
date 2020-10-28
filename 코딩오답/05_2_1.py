def flatten(data):
    output=[]
    for list_data in data:
        if type(list_data)==list:
            output+=flatten(list_data)
        else:
            output.append(list_data)
    return output

example=[[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(flatten(example))
