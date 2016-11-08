def nat_num(num):
    if num % 10 == 0 and num % 3 == 0:
        print 'Chislo kratno 3 i 10!'
    else:
        print 'Chislo ne kratno 3 i 10!'

if __name__ == '__main__':
    print nat_num(40)