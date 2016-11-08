def get_digit_sum(num):
    list_digit = []
    for i in range(100, num):
        digit = i % 10 + i % 100 // 10 + i // 100
        if digit == 7:
            list_digit.append(i)
    return list_digit


if __name__ == '__main__':
    print get_digit_sum(1000)
