# Check if two words are anagrams 
def find_anagram(word, anagram):

    if(sorted(word)==sorted(anagram)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

str1 ="dance"
str2 ="play"
find_anagram("word", "anagram")

