filename1 = '-c input.txt'
# Counting characters
with open(filename1, 'r',encoding='utf-8') as f:
    text = f.read()
    num_chars = len(text)
print(f'The number of characters in the file is: {num_chars}')
filename2 = '-w input.txt'
# Counting words
with open(filename2, 'r',encoding='utf-8') as f:
    text = f.read()
    num_words = len(text.split())
print(f'The number of words in the file is: {num_words}')
stop=input("Press <enter>")