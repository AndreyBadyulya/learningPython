def check_space_str(test_str):
    return (test_str.replace('   ', ' ')).replace('   ', ' ')

if __name__ == '__main__':
    print check_space_str('     five    four   three  two one ')