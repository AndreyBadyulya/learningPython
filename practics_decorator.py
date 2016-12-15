def logger(path):
	def wrapper(func):
		def replacement_function(*args, **kwargs):
			import time
			with open(path, 'a') as log_file:
				log_file.write('Function {} called at {}!\n'
					.format(func.__name__, time.asctime()))
		return replacement_function
	return wrapper

@logger('C:\Users\user1\Documents\Practics\log.txt')
def summirize(x, y):
	return x + y	

if __name__ == '__main__':
	print str(summirize(2, 3))