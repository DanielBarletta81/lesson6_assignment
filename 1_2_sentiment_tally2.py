# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review. 
# Use a predefined list of positive and negative words to check against.
# The function should return the count of positive and negative words for each review.
#python 
# positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
# negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

""" reviews = [ "This product is really good. I'm impressed with its quality.",
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
        
           
highlight_keywords()     """


# Start Task 2 *****   **** ****   *****

reviews = [ "This product is really good. I'm impressed with its quality.",
            "The performance of this product is excellent. Highly recommended!", 
            "I had a bad experience with this product. It didn't meet my expectations.",
            "Poor quality product. Wouldn't recommend it to anyone.", 
            "The product was average. Nothing extraordinary about it." ]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "Poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

total_pos_count = 0
total_neg_count = 0



def sentiment_tally():
   
    global total_pos_count
    global total_neg_count

    

     # If a word is in review and in negative or positive words list
     # Increment counter depending on which list
     # Print counters for both

    
          
    for pos in positive_words:
            for review in reviews:
                 
                 if pos in review:
                         
                    total_pos_count += review.count(pos)
                    
                    
                    print(f"{review}Positive words in reviews: {total_pos_count}") 
            
                
for neg in negative_words:
                for review in reviews:   
                            if neg in review:
                                total_neg_count += review.count(neg)
                                print(f"{review}Neg words: {total_neg_count}")
                           

    

sentiment_tally()