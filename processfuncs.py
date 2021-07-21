

def process_text(text):
    import re

    text = text.strip()
    removefword = re.compile(re.escape('fucking'), re.IGNORECASE)
    text = removefword.sub('', text)

    return text 

def get_tokens(text):
    import pickle
    
    text_list=[text]

    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    tokenized_text_list = tokenizer.texts_to_sequences(text_list)

    return tokenized_text_list

