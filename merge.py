files = ['1.txt', '2.txt', '3.txt']

file_counts = {}
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        file_counts[file] = len(f.readlines())

sorted_files = sorted(file_counts, key=file_counts.get)

with open('merge.txt', 'w', encoding='utf-8') as merged_file:
    for file in sorted_files:
        with open(file, 'r', encoding='utf-8') as f:
            merged_file.write(f.read())
            merged_file.write('\n')
