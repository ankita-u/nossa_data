import re
import os

input_directory_path = "data/input"
output_directory_path = "data/output"
topics = {
    "Climate Risk Management": set(),
    "Water Risk Management": set(),
    "Scope 1": set(),
    "Scope 2": set(),
    "Health": set(),
    "Employees": set(),
    "Forests": set()
}

for file_name in os.listdir(input_directory_path):
    file_path = os.path.join(input_directory_path, file_name)
    with open(file_path) as read_file:
        file_content = read_file.read()
        paragraphs = file_content.split("\n\n")
        for para in paragraphs:
            for topic in topics:
                if re.search(rf"\b{topic}\b", para, re.IGNORECASE):
                    topics[topic].add(para.strip())

        with open(f"{output_directory_path}/{file_name}_results.txt", "w") as write_file:
            for topic, paras in topics.items():
                if paras:
                    write_file.write(f"{'*' * 10} {topic} {'*' * 10} \n\n")
                    write_file.write("\n\n".join(paras))
                    write_file.write(f"\n\n {'-' * 150}\n\n")

        print(f"Topics search for {file_name} completed successfully...")