def simple_digit():
	n = input('Enter your digit: ')
    	if n % n == 0 and n % 2 == 1 or n % 3 == 1:
        	print (n, 'simple digit')
    	else:
        	print (n, 'not simple digit')

if __name__ == "__main__":
	simple_digit()