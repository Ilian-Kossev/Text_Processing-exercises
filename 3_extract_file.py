file_path = input()
reversed_file_path = file_path[::-1]
rev_index_dot = reversed_file_path.index('.')
rev_file_extension = reversed_file_path[:rev_index_dot]
rev_index_slash = reversed_file_path.index('\\', rev_index_dot, len(reversed_file_path))
rev_file_name = reversed_file_path[rev_index_dot + 1: rev_index_slash]
file_name = rev_file_name[::-1]
file_extension = rev_file_extension[::-1]
print(f'File name: {file_name}')
print(f'File extension: {file_extension}')
