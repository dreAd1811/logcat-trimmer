import argparse
import re

def filter_logcat_file(input_file_path, output_file_path):
    regex = re.compile(r'(.*)(error|fatal)(.*)', re.IGNORECASE)

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            if re.search(regex, line):
                output_file.write(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter logcat file based on error or fatal messages.')
    parser.add_argument('input_file_path', help='Path to the input logcat file')
    parser.add_argument('output_file_path', help='Path to the output filtered logcat file')
    args = parser.parse_args()

    filter_logcat_file(args.input_file_path, args.output_file_path)
    print(f"Filtered log messages saved to {args.output_file_path}.")
