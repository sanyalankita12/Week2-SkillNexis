def count_from_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print("Error: File not found.")
        return None


def count_words(content):
    words = len(content.split())
    print(f"The number of words in the file are: {words}.")


def count_lines(content):
    lines = len(content.splitlines())
    print(f"The number of lines in the file are: {lines}.")


def count_char(content):
    chars = len(content)
    print(f"The number of characters in the file are: {chars}.")


content = count_from_file(
    r"/assignments/sample.txt"
)

if content is not None:
    count_words(content)
    count_lines(content)
    count_char(content)
