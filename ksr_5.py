def polidrom_str(custom_str):
    reverse_str = custom_str[::-1]
    return custom_str == reverse_str

if __name__ == '__main__':
    print polidrom_str('abcddcba')