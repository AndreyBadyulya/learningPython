def check_space_str(test_str):
    my_list = []
    for i in range(len(test_str)):
        if test_str[i - 1] == ' ' and test_str[i] == ' ':
            i += 1
        else:
            my_list.append(test_str[i])
    return ''.join(my_list)

if __name__ == '__main__':
    print check_space_str('   3               five                         four   three  two one    1')