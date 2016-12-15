import sys

def copy(input, output):
	with open(input) as input_file, open(output, 'w') as output_file:
		#for line in input_file:
		#	output_file.write(line)
		output_file.write(input_file.read())


if __name__ == '__main__':
	#input_file_path, output_file_path = sys.argv[1:3]
	# copy(input_file_path, output_file_path)
	copy('C:\\Users\\user1\\Documents\\Practics\\log.txt', 'C:\\Users\\user1\\Documents\\Practics\\out.txt')