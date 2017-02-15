# Takes: String of text | Returns: List of words sample-text.txt
def generate_tokens(file_name):
    dict = open('./text_files/' + file_name, 'r')
    text = dict.read()
    dict.close()
    return text.split()
