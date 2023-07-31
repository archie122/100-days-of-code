with open("file1.txt") as f1, open("file2.txt") as f2:
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()


new_lines = [int(num.strip()) for num in f1_lines if num in f2_lines]
print(new_lines)