import os

input_directory_path = "data/input"

for file_name in os.listdir(input_directory_path):
    file_path = os.path.join(input_directory_path, file_name)

    with open(file_path) as file:
        file_content = file.readlines()
        count = 0
        for content in file_content:
            words = content.split()
            for word in words:
                if word.isalnum():
                    count = count + 1
        print(f"{file_name}: {count}")


