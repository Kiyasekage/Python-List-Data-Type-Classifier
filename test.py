def group_types(i_list):
    output = dict.fromkeys(i_list)
    for keys in output:
        if isinstance(keys,int):
            output[keys] = "Integer"
        else:
            output[keys] = "String"
    return output
custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
