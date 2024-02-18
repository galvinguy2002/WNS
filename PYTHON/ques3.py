def alter_string(input_str):
    result_str = ""
    for i in range(len(input_str)):
        if i % 2 == 0:
            result_str += input_str[i]
    return result_str

user_input = input("\n Please enter a string: \n")

result_string = alter_string(user_input)
print("\nResulting String at even positions only: ", result_string)
