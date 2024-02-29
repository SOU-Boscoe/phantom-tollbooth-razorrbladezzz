import phantom_tollbooth

book = phantom_tollbooth.get_text().lower()


def punctuation(): # removes punctuation
    punctuation_chars = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    # odd = "—"
    
    no_punct = ''.join(char for char in book if char not in punctuation_chars)
    return no_punct

def prepositions(): # removes prepositions
    prepositions_words = ["about", "above", "across", "after", "against", "again", "along",
                          "among", "around", "as", "at", "away", "because", "behind", "below",
                          "beneath", "beside", "between", "beyond", "by", "down", "during",
                          "except", "for", "from", "in", "inside", "into", "like", "near", "of",
                          "off", "on", "onto", "out", "outside", "over", "past", "through",
                          "to", "toward", "under", "until", "up", "upon", "with", "within",
                          "without"]

    
    no_prepositions = ' '.join(word for word in punctuation().split() if word not in prepositions_words)
    return no_prepositions

def pronouns(): # removes pronouns
    pronouns_words = ["dr", "he", "hed", "her", "hers", "herself", "him", "himself", "his", "i", 
                      "id", "ill", "im", "it", "its", "itself", "me", "mr", "mrs", "ms", "my", 
                      "our", "she", "theirs", "they", "theyd", "them", "we", "wed", "well", "you", 
                      "youd", "youll", "youre", "your", "yours"]
    
    no_pronouns = ' '.join(word for word in prepositions().split() if word not in pronouns_words)
    return no_pronouns

def articles(): # removes articles
    articles_words = ["a", "an", "that", "the"]
    
    no_articles = ' '.join(word for word in pronouns().split() if word not in articles_words)
    return no_articles

def conjuctions(): # removes conjuctions
    conjuctions_words = ["and", "but", "for", "or", "nor", "so", "yet"]
    
    no_conjuctions = ' '.join(word for word in articles().split() if word not in conjuctions_words)
    return no_conjuctions

def misc(): # removes words that i don't know how to categorize
    misc_words = ["all", "also", "arent", "are", "be", "been", "came", "can", "cant", "didnt", "do", "does", 
                  "even", "even", "get", "had", "have", "how", "if", "is", "just", "like", "liked", 
                  "made", "many", "must", "no", "not", "now", "only", "said", "says", "seem", 
                  "seemed", "see", "take", "than", "that's", "theirs", "then", "there", "theres", 
                  "these", "theyre", "too", "very", "want", "was", "way", "we're", "went", "what", 
                  "when", "where", "why", "will", "would"]
    
    no_misc = ' '.join(word for word in conjuctions().split() if word not in misc_words)
    return no_misc

def calculate_word_frequency():
    updated_book = misc()
    word_list = updated_book.split()
    freq_table = {}
    for word in word_list:
        if word not in freq_table:
            freq_table[word] = 0
        freq_table[word] += 1
    sorted_freq_table = dict(sorted(freq_table.items(), key=lambda x: x[1], reverse=True))
    first_50 = {item: value for i, (item, value) in enumerate(sorted_freq_table.items()) if i < 50}
    
    print(f'{"Fifty most common words in:":^30}\n{"~The Phantom Tollbooth~":^30}\n')
    print(f'=' * 31)
    print(f'| {"Word":<12} || {"Occurrences"} |')
    print(f'=' * 31)
    for i, (word, freq) in enumerate(first_50.items(), start=1):
        print(f'{i}. {word:<14}{":":<2}{freq}')
        
    # print(f'{"Number":<6} || {"Word":<12} || {"Occurrences":<14}')
    # print(f'=' * 30)
    # for i, (word, freq) in enumerate(first_50.items(), start=1):
    #     print(f'{i:<6}: {word:<12}: {freq}')
    


    