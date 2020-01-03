
# NLP -TASKS


# NATURAL LANGUAGE PROCESSING

TASK 1 

  - assign a sentence to a variable
  - assign a multiline paragraph to a variable -use triple quotes
  - assign a text in any language(except english) to a variable
  - Additional Tasks
     -Finding Frequencies of each word in the paragraph
     -Finding unique words and counting the number of words
     -Converting the paragraph in to a vector of words


Task 2
  - Finding errors in Google translate
  - Finding and analysing the reason for popularity of a politician in COCA(concordance search)
  - using Readable.com to just learn and know the parameters for readabolity of any paragraph

Character Encoding identification algorithm:
  - Library used chardet
  - Refrences
    - [mozilla auto char encoding detection](https://www-archive.mozilla.org/projects/intl/universalcharsetdetection)
    - [Chardet Documentation](https://chardet.readthedocs.io/en/latest/index.html)


Charset detection Mozilla project 
  - what it is?
    Based on the bytes of data it guess the charset.
  - What it is not?
    It doesn't just look at the meta data and find the encoding,it guess the encoding on unreliable data.
  - [Refrence](https://www-archive.mozilla.org/projects/intl/chardet.html)
      
Char detection:
we could easily detect UTF-8 encoding as the top bits have a pattern and as the pattern reccurs we can confirm the encoding as UTF-8.This similar pattern recognition is used for UTF-1.
    
Other Refrences:
  - [ICU Project](http://site.icu-project.org/)
  - [Charset detector](https://unicode-org.github.io/icu-docs/apidoc/released/icu4j/com/ibm/icu/text/CharsetDetector.html)
      



Typographic:
  - It basically is the visual component of a word.The font the stress in which it is written conveys meaning and emotion.

Orthographic:
  - Related to the conventional spelling of a word.Derived from greek words Ortho(Correct) and Graph(Writing).
    Eg: School is written as skool or awesome is written as ossum.
    This makes it difficult for processing.

Suprasegmental:
  - When we speak , we also include sounds that are above the level of segments,this is called Suprasegmental or Prosody.The primary     pieces of suprasegmental information are pitch,stress,loudness.


JIEBA(A python moudle for chinese text segmentation)
  - segmenting the wiki of Zhu Shenghao
    ![Output](./out/jieba.png?raw=true "Output of segmentation of text using jieba")

Detecting sentences in a text without punctuations:
  [code](https://github.com/ottokart/punctuator2)
  [demo](http://bark.phon.ioc.ee/punctuator)



Tokenization:
  - It is the process in which a sequence of characters are chopped up into pieces(tokens).
  - Methods:
    - 1.using python split() function
    - 2.using regex
    - 3.using Spacy
    - 4.using keras
    -  5.using nltk
  - Refrences:
    [IBM](https://www.ibm.com/developerworks/community/blogs/nlp/entry/tokenization?lang=en)
    [Spacy](https://spacy.io/api/tokenizer)
    [StanfordNLP](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html)

Task 3:
  - working with brown and inaugural corpus
  - Removing stopwords from Lincoln's speech
  - finding the most used words in his speech
  - finding freqDist for the categories in brown corpus
  - finding the avg number of words in the president's speech.

