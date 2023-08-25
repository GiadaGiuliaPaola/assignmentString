from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())



def unique_koala_facts(n):
    facts_list = []
    count = 0

    while len(facts_list) < n:
         random_fact = random_koala_fact()
         if random_fact not in facts_list:
              facts_list.append(random_fact)
              count +=1
         if count >= 1000:
              break
         count +=1
    return facts_list
        
print(unique_koala_facts(3))


def num_joey_facts():
   all_string = []
   count = 0
   joey_string = []
   fact = random_koala_fact()

   while all_string.count(fact) < 10:
        fact = random_koala_fact()
        all_string.append(fact)
        count +=1
        for fact in all_string:
         if 'joey' in fact and fact not in joey_string:
            joey_string.append(fact)
            count +=1
            # for fact in joey_string:
         
   
   return joey_string


             
print(num_joey_facts())

    #  for fact in random_koala_fact():
        #   if 'joey' in fact:
            #    print(fact)
            #    unique_joey_facts.append(fact)
            #    count +=1
            #    return joey_fact_list
        #   for element in joey_fact_list:
            #    unique_joey_facts += element
               
    #  print(joey_fact_list)         
    #  print (unique_joey_facts)



def koala_weight(list):
    #  weight_kilograms = 0
     index = 0
     length = 900
     
     














