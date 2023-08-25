from helpers import get_countries

""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
# if __name__ == "__main__":
    # countries = get_countries()
    
    
    
    

    # """ Write the calls to your functions here. """


def shortest_names(list) :
    list.sort(key = len)
    print(list[:3])




def most_vowels(list):
    vow_list = []
    vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}
    
    for country in list:
        count = 0 
        for i in country:
            if i in vowels:
                count += 1
        vow_list.append([count, country])
    vow_list = sorted(vow_list, reverse=True)
    result = [country for country in vow_list]
    return(result[:3])
       

# print(most_vowels(countries))


def alphabet_set(list):
   alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   list1 = sorted(list, reverse = True)
   count_letters = 0
   for country in list1:
      count = 0
      for letter in country:
            if letter in alphabeth:
                count_letters +=1
                count_letters.append([count, country])
                return alphabeth.remove(count_letters)
            return list1

        
# print(alphabet_set(countries))




if __name__ == "__main__":
    countries = get_countries()
    print(shortest_names(countries))
    print(most_vowels(countries))
    print(alphabet_set(countries))
    

        
    





