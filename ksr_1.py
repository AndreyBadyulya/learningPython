def nat_num(num):
    return num % 10 == 0 and num % 3 == 0
    	
        

if __name__ == '__main__':
    print nat_num(40)