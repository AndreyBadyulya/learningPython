def wrapper(f):
	def replacement_function(*args, **kwargs):
		import time
		print 'Spleeping for 2 sec'
		time.sleep(2)
		return f(*args, **kwargs)
	return replacement_function


	
def arg_wrapper(seconds):
	def wrapper(f):
		def replacement_function(*args, **kwargs):
			import time
			print 'Sleeping {} seconds'.format(seconds)
			time.sleep(seconds)
			return f(*args, **kwargs)
		return replacement_function
	return wrapper