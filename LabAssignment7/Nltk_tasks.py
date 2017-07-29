import nltk
from nltk import pos_tag
from nltk.corpus import wordnet as wn, stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
#nltk.download('all')

file = file('text.txt').read()

print('--Without stopwords--')
removal = set(stopwords.words('english'))
words = word_tokenize(file)
Filtered = []
for r in words:
    if r not in removal:
        Filtered.append(r)
print(Filtered)

print ('--Lemmatized words--')
lem = WordNetLemmatizer()
temp_list = []
for i in Filtered:
    lm = lem.lemmatize(i)
    temp_list.append(lm)
print(temp_list)

print('--POS--')
sent = pos_tag(temp_list)
print [s for s in sent if s[1] != 'VBG']

print ('--Word Frequency--')
fdist = nltk.FreqDist(temp_list)
vocab = fdist.keys()
print (vocab[:50])

print ('--Top 5 words--')
for word, frequency in fdist.most_common(5):
    print(u'{};{}'.format(word, frequency))

print ('--Original text in my file--')
print (file)
