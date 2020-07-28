text = input('Enter a sentence please : ')
char_dict = {}
for i in text:
    if i not in char_dict.keys():
        char_dict[i] = 1
    else:
        char_dict[i] += 1
print(char_dict)