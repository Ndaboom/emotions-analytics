import string
import requests
import re
from googlesearch import search
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


#clean the text
text = open('data.txt', encoding="utf-8").read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
print("Text cleaned...")

#Tokenization
tokenized_words = word_tokenize(cleaned_text, "english")
print("Text tokenized...")

#Stop words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words("english"):
        final_words.append(word)

print("Stop word removed...")

print("Applying the NLP Algorithm...")
#Identifying emotion, NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        
        #Counting emotions
        if word in final_words:
            emotion_list.append(emotion)

#Emotions founded 
print("Emotions founded after analyzing data :")
print(emotion_list)

#count of each emotion found

print("Count each emotion in the emotion list...")
w = Counter(emotion_list)
print("Result after calculation :")
print(w)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']

    if neg > pos:
        print("Negative sentiment")
    elif pos > neg:
        print("Positive sentiment")
    else:
        print("Neutral sentiment")

sentiment_analyse(cleaned_text)

fig, axl = plt.subplots()
axl.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()