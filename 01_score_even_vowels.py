# get the score of each word using input from STDIN. Print the score output to STDOUT
# The score of a single word is 2 if the word contains an even number of vowels. Otherwise, the score of this word is 1 
# vowels in the alphabet are a, e, i, o, u and y

def score_words():
    number_of_words = input("enter 2")
    #resolved without using number_of_words
    words = input("enter hello world")
    return get_words_score(words)
    
def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_counter = 0
    for character in word:
        if character in vowels:
          vowel_counter += 1
        
    if vowel_counter % 2 == 0:
        return 2
    else:
        return 1

def get_words_score(words):
    total_words_score = 0
    words = words.split()
    for word in words:
        total_words_score += count_vowels(word)
    
    return total_words_score

if __name__ == '__main__':
    print(score_words())
