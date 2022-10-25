def isAnagram(string1, string2):
    string1_list = list(string1)  # Convert strings into lists
    string2_list = list(string2)
    string1_list.sort()
    string2_list.sort()
      # Check if the two lists are the same after sorting
    if string1_list == string2_list:  # Check if the two strings are the same  
        return True
    else:
        return False

def main():
    s1 = input('Please enter the first word:')   #6s?
    s2 = input('Please enter the second word:')
    if s1 == s2:
        print('These two words are identical.')
    elif isAnagram(s1, s2):          
        print(s2.capitalize(), 'is an anagram of', s1 + '.')   # Capitalize the first letter
    else:
        print(s2.capitalize(), 'is not an anagram of', s1 + '.')

main()


        


