#Task 1: Keyword Highlighter

#Write a program that searches through a series of product reviews for keywords such as
# "good", "excellent", "bad", "poor", and "average".
# Print out each review with the keywords in uppercase so they stand out.


reviews = [ "This product is really good. I'm impressed with its quality.",
            "The performance of this product is excellent. Highly recommended!", 
            "I had a bad experience with this product. It didn't meet my expectations.",
            "Poor quality product. Wouldn't recommend it to anyone.", 
            "The product was average. Nothing extraordinary about it." ]

words_to_upper = ["good", "excellent", "bad", "Poor", "average"]


def highlight_keywords():
    
    for review in reviews:
     
        for word in words_to_upper:
            i = review.find(word)
            
            if i == -1:
                continue
            else:
             
                replace = review.replace(word, word.upper())
        
            print(replace)
        
           
highlight_keywords()    