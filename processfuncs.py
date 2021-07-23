

def process_text(text):
    import re

    text = text.strip()
    removefword = re.compile(re.escape('fucking'), re.IGNORECASE)
    text = removefword.sub('', text)

    return text 

def get_tokens(text, tokenizer):
    import pickle
    from keras.preprocessing.sequence import pad_sequences
    
    text_list=[text]

   
    
    tokenized_text_list = tokenizer.texts_to_sequences(text_list)
    tokenized_text_list = pad_sequences(tokenized_text_list, maxlen = 200)
    return tokenized_text_list

def get_probs(text, comment_model, tokenizer):

    from keras import models 
    text = process_text(text)
    token_list = get_tokens(text, tokenizer)

    #comment_model = models.load_model('comment_class_model.h5')
    probs = comment_model.predict(token_list)
    probs = probs.flatten()
    probs = probs.tolist()
    labels = ['toxic', 'severely toxic', 'obscene', 'threat', 'insult', 'identity hate']
    prob_dictionary = dict(zip(labels,probs)) 
    
    return prob_dictionary

def is_toxic(text, model, tokenizer):

    proba_dict = get_probs(text, model, tokenizer)
    
    for key in proba_dict:
        if proba_dict[key] > 0.5:
            return True 

    return False 



