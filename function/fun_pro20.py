# - Write a function longest_word(sentence) that accepts a sentence and returns the longest word in the sentence.
def longest_word(sentence):
    words=sentence.split()
    longest=""
    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest
sentence=input("enter a sentence")
print("longest words is:",longest_word(sentence))
