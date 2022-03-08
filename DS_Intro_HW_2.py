def reverse(sentence, reverse_word):
    sentence_split=sentence.split()
    index=-1
    if type(sentence)==str and type(reverse_word)==str:
        for i in sentence_split:
            index+=1
            if i == reverse_word:
                reverse_word=reverse_word[::-1]
                sentence_split[index]=reverse_word
                return " ".join(sentence_split)
        else:
            return "The word was not found" 
    else:
        print("invalid input")
print(reverse("i bla bla like banana", "bla"))
            

        


















                
    
    
    
    
    
    
    
    
    
    
    
    
    
#     if type(sentence)==str and type(reverse_word)==str:
#         sentence_split=sentence.split()
#         if reverse_word in sentence_split:
#             print("yes")
#         else:
#             print("no")

        
        

    














































