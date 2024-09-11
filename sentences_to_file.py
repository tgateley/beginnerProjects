sen1 = input("Enter sentence 1: ")
sen2 = input("Enter sentence 2: ")
sen3 = input("Enter sentence 3: ")

sentences = [sen1 + "\n----------\n", sen2 + "\n----------\n", sen3]

with open("user_sentences.txt", 'w') as file:
    file.writelines(sentences)

print("Sentences have been saved to user_sentences.txt")
