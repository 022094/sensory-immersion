import os

# LOAD EXPORTED DATA
def ask_location():

	""" This function asks the user to input the recording location. """

	filename = input("Enter the path of the recording location: ")
	return filename

RECORDING_LOCATION = ask_location()
os.chdir(RECORDING_LOCATION)


''' files_dict = {}
# empty_dict= {}
# def check_files(folder):
# The goal of this function is to get check if a folder contain the same file structures as the ideal folder.
# ideal_file_structure()
# while print_file_structure() != ideal_file_structure():
#	check_missing()
#	print(results_missing) '''
# Loading csv file onto pandas data frame '''


def print_file_structure(startpath):

	""" This function prints the file structure within the folder. """

	for root, dirs, files in os.walk(startpath):
		level = root.replace(startpath, '').count(os.path.sep)
		indent = ' ' * 4 * level
		print(f'{indent}{os.path.basename(root)}/')
		subindent = ' ' * 4 * (level + 1)
		for f in sorted(files):
			print(f'{subindent}{f}')


if __name__ == '__main__': 

	""" Lets call all of the above functions and look at our data! In case of an import, you need to call the
	function directly. """

	#ask_location()
	print_file_structure(RECORDING_LOCATION)
