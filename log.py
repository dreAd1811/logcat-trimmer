import re

def filter_logcat_file(input_file_path, output_file_path):
    regex = re.compile(r'(.*)(error|fatal)(.*)', re.IGNORECASE)

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            if re.search(regex, line):
                output_file.write(line)

if __name__ == '__main__':
    input_file_path = "/path/to/your/input_logcat_file.log"  # Replace with the path to your input logcat file
    output_file_path = "/path/to/your/output_filtered_logcat_file.log"  # Replace with the path to your output filtered logcat file
    filter_logcat_file(input_file_path, output_file_path)
    print(f"Filtered log messages saved to {output_file_path}.")
