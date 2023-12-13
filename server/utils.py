import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from pyvi import ViTokenizer, ViPosTagger
import demoji
import re
import re


def remove_words_not_in_list(text):
    with open('./TuDon.txt', 'r', encoding='utf-8') as file:
        word_list = file.read().splitlines()
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word in word_list]
    return ' '.join(filtered_tokens)


def correct_spelling(text):
    words = ViTokenizer.tokenize(text)
    corrected_words = ViPosTagger.postagging(words)
    corrected_text = ' '.join(corrected_words[0])
    return corrected_text

def remove_emojis(text):
    return demoji.replace_with_desc(text)

def remove_stopwords(text):
    with open("./vietnamese-stopwords.txt", 'r', encoding='utf-8') as file:
        stop_words = [word.strip() for word in file.readlines()]
    if isinstance(text, str):  # Kiểm tra nếu text là chuỗi
        words = text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(filtered_words)
    else:
        return ''  # Returns empty string if not a string

def process_data(review):
    # Convert text to lowercase
    review = review.lower()
    # Removing punctuation
    review = re.sub(r'[^\w\s]', '', review)
    # remove word not in world list
    review = remove_words_not_in_list(review)
    # Remove stop word
    review = remove_stopwords(review)
    # correct spelling and tokenize
    review = correct_spelling(review)
    # Dealing with emojis and emoticon
    review = remove_emojis(review)
    return review



