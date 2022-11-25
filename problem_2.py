import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path == None:
        return None
    file_list = []
    dir_list = os.listdir(path)
    for dir in dir_list:
        file = os.path.join(path, dir)
        if (os.path.isfile(file) and file.endswith(suffix)):
            file_list.append(file)
        elif os.path.isdir(file):
            file_list += find_files(suffix, file)
    return file_list

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
# Test Case 1
# Find all files with '.c' from root folder
print(find_files(
    '.c', 'testdir'))

# Test Case 2
# Test Case 2
# Find all files with '.c' from a empty folder
print(find_files('.c', 'testdir'))

# Test Case 3
# Test Case 3
# Find all files with '.c' from a folder does not contain '.c' suffix file
print(find_files('.c', 'testdir'))