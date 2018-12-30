---
title: "Notes on learning NLTK"
description: "In this tutorial I collected a bunch of notes I used during the study of the book *Natural Language Processing with Python*"
last_update: "2018-12-30"
published: true
---

```python
%matplotlib notebook
```

# Notes on learning NLTK
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

This notebook is a collection of notes and codes developed during my studies of the NLTK library.

In this notebook I will follow the [Natural Language Processing with Python](http://www.nltk.org/book/) book, focusing exclusively on the NLTK argument, skipping all the Python related parts of the book. **This is NOT a replacement for reading the book and walk the path yourself!**

## Index
* [Setting Up The Environment](#Setting-Up-The-Environment)
* [NLTK Corpora](#NLTK-Corpora)
    * [Book Corpus](#Book-Corpus)
* [Glossary](#Glossary)
* [NL Concepts](#NL-Concepts)
    * [Concordance](#Concordance)
    * [Distributional Similarity](#Distributional-Similarity)
    * [Common Contexts](#Common-Contexts)
    * [Dispersion Plot](#Dispersion-Plot)
    * [Lexical Diversity](#Lexical-Diversity)
    * [Frequency Distribution](#Frequency-Distribution)
* [Usage Examples](#Usage-Examples)
    * [Counting Vocabulary](#Counting-Vocabulary)

-------------------------------------------------------------------------------
## Setting Up the Environment
NLTK stands for **Natural Language Toolkit** and it is the most used Python library used to work with human language. More information about it can be found on the website [www.nltk.org](www.nltk.org).

At the moment of writing, the following is installed system-wide:

```
C:\nltk>python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.

C:\notebooks>pip list
Package            Version
------------------ -------
backcall           0.1.0
bleach             3.0.2
colorama           0.4.0
decorator          4.3.0
defusedxml         0.5.0
entrypoints        0.2.3
ipykernel          5.1.0
ipython            7.1.1
ipython-genutils   0.2.0
ipywidgets         7.4.2
jedi               0.13.1
Jinja2             2.10
jsonschema         2.6.0
jupyter            1.0.0
jupyter-client     5.2.3
jupyter-console    6.0.0
jupyter-core       4.4.0
MarkupSafe         1.0
mistune            0.8.4
nbconvert          5.4.0
nbformat           4.4.0
notebook           5.7.0
pandocfilters      1.4.2
parso              0.3.1
pickleshare        0.7.5
pip                18.1
prometheus-client  0.4.2
prompt-toolkit     2.0.7
Pygments           2.2.0
python-dateutil    2.7.5
pywinpty           0.5.4
pyzmq              17.1.2
qtconsole          4.4.2
Send2Trash         1.5.0
setuptools         40.5.0
six                1.11.0
terminado          0.8.1
testpath           0.4.2
tornado            5.1.1
traitlets          4.3.2
virtualenv         16.0.0
wcwidth            0.1.7
webencodings       0.5.1
widgetsnbextension 3.4.2
```

The first thing to do in order to work with NLTK is to install it. Detailed instructions are available on the [Installing NLTK](http://www.nltk.org/install.html) page. In this section, I will detail what I installed on my Windows system. Should I ever install it on another system, I will integrate it.


### Install Numpy
[NumPy](http://www.numpy.org/) is the fundamental package for scientific computing with Python. Install it on your system with the following command

```
C:\notebooks>pip install numpy
Collecting numpy
  Downloading https://files.pythonhosted.org/packages/42/5a/eaf3de1cd47a5a6baca4
1215fba0528ee277259604a50229190abf0a6dd2/numpy-1.15.4-cp37-none-win32.whl (9.9MB
)
    100% |████████████████████████████████| 9.9MB 2.1MB/s
Installing collected packages: numpy
Successfully installed numpy-1.15.4
```

### Install NLTK
In order to install NLTK libraries, run the following command:

```
(nltk) C:\GitHub\nltk>pip install nltk
Collecting nltk
Collecting six (from nltk)
  Using cached https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bf
a78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
Installing collected packages: six, nltk
Successfully installed nltk-3.3 six-1.11.0
```

### Install Matplotlib
```
C:\GitHub>pip install matplotlib
Collecting matplotlib
  Downloading https://files.pythonhosted.org/packages/01/57/ea829da613b3eb1d1b18
d85ba3be8d41b2bdd61997960c30824a1059a663/matplotlib-3.0.1-cp37-cp37m-win32.whl (8.7MB)
    100% |████████████████████████████████| 8.7MB 3.3MB/s
Collecting kiwisolver>=1.0.1 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/63/95/6e03c1e40776851eda7
af2e9b014bcf510e3205033c33b604c2ee36687a1/kiwisolver-1.0.1-cp37-none-win32.whl
Requirement already satisfied: numpy>=1.10.0 in c:\users\mary\appdata\local\prog
rams\python\python37-32\lib\site-packages (from matplotlib) (1.15.4)
Collecting cycler>=0.10 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af69644
0ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/71/e8/6777f6624681c8b9701a
8a0a5654f3eb56919a01a78e12bf3c73f5a3c714/pyparsing-2.3.0-py2.py3-none-any.whl (5
9kB)
    100% |████████████████████████████████| 61kB 3.9MB/s
Requirement already satisfied: python-dateutil>=2.1 in c:\users\mary\appdata\loc
al\programs\python\python37-32\lib\site-packages (from matplotlib) (2.7.5)
Requirement already satisfied: setuptools in c:\users\mary\appdata\local\program
s\python\python37-32\lib\site-packages (from kiwisolver>=1.0.1->matplotlib) (40.
5.0)
Requirement already satisfied: six in c:\users\mary\appdata\local\programs\pytho
n\python37-32\lib\site-packages (from cycler>=0.10->matplotlib) (1.11.0)
Installing collected packages: kiwisolver, cycler, pyparsing, matplotlib
Successfully installed cycler-0.10.0 kiwisolver-1.0.1 matplotlib-3.0.1 pyparsing
-2.3.0
```

With this, we are ready to start working with NLTK.

### Load the data
Now let's download and install the data that we will use


```python
import nltk
nltk.download('book')
```

    [nltk_data] Downloading collection 'book'
    [nltk_data]    |
    [nltk_data]    | Downloading package abc to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\abc.zip.
    [nltk_data]    | Downloading package brown to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\brown.zip.
    [nltk_data]    | Downloading package chat80 to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\chat80.zip.
    [nltk_data]    | Downloading package cmudict to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\cmudict.zip.
    [nltk_data]    | Downloading package conll2000 to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\conll2000.zip.
    [nltk_data]    | Downloading package conll2002 to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\conll2002.zip.
    [nltk_data]    | Downloading package dependency_treebank to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\dependency_treebank.zip.
    [nltk_data]    | Downloading package genesis to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\genesis.zip.
    [nltk_data]    | Downloading package gutenberg to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\gutenberg.zip.
    [nltk_data]    | Downloading package ieer to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\ieer.zip.
    [nltk_data]    | Downloading package inaugural to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\inaugural.zip.
    [nltk_data]    | Downloading package movie_reviews to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\movie_reviews.zip.
    [nltk_data]    | Downloading package nps_chat to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\nps_chat.zip.
    [nltk_data]    | Downloading package names to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\names.zip.
    [nltk_data]    | Downloading package ppattach to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\ppattach.zip.
    [nltk_data]    | Downloading package reuters to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    | Downloading package senseval to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\senseval.zip.
    [nltk_data]    | Downloading package state_union to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\state_union.zip.
    [nltk_data]    | Downloading package stopwords to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\stopwords.zip.
    [nltk_data]    | Downloading package swadesh to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\swadesh.zip.
    [nltk_data]    | Downloading package timit to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\timit.zip.
    [nltk_data]    | Downloading package treebank to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\treebank.zip.
    [nltk_data]    | Downloading package toolbox to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\toolbox.zip.
    [nltk_data]    | Downloading package udhr to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\udhr.zip.
    [nltk_data]    | Downloading package udhr2 to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\udhr2.zip.
    [nltk_data]    | Downloading package unicode_samples to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\unicode_samples.zip.
    [nltk_data]    | Downloading package webtext to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\webtext.zip.
    [nltk_data]    | Downloading package wordnet to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\wordnet.zip.
    [nltk_data]    | Downloading package wordnet_ic to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\wordnet_ic.zip.
    [nltk_data]    | Downloading package words to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\words.zip.
    [nltk_data]    | Downloading package maxent_treebank_pos_tagger to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping taggers\maxent_treebank_pos_tagger.zip.
    [nltk_data]    | Downloading package maxent_ne_chunker to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping chunkers\maxent_ne_chunker.zip.
    [nltk_data]    | Downloading package universal_tagset to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping taggers\universal_tagset.zip.
    [nltk_data]    | Downloading package punkt to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping tokenizers\punkt.zip.
    [nltk_data]    | Downloading package book_grammars to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping grammars\book_grammars.zip.
    [nltk_data]    | Downloading package city_database to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping corpora\city_database.zip.
    [nltk_data]    | Downloading package tagsets to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping help\tagsets.zip.
    [nltk_data]    | Downloading package panlex_swadesh to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    | Downloading package averaged_perceptron_tagger to
    [nltk_data]    |     C:\Users\ai239\AppData\Roaming\nltk_data...
    [nltk_data]    |   Unzipping taggers\averaged_perceptron_tagger.zip.
    [nltk_data]    |
    [nltk_data]  Done downloading collection book





    True



---
## NLTK Corpora

In this section you can find some details about all the corpora used in the book.

### Book Corpus
This is a collection of nine books and other corpora that is used in the first chapter of the book.


```python
from nltk.book import *
```

    *** Introductory Examples for the NLTK Book ***
    Loading text1, ..., text9 and sent1, ..., sent9
    Type the name of the text or sentence to view it.
    Type: 'texts()' or 'sents()' to list the materials.
    text1: Moby Dick by Herman Melville 1851
    text2: Sense and Sensibility by Jane Austen 1811
    text3: The Book of Genesis
    text4: Inaugural Address Corpus
    text5: Chat Corpus
    text6: Monty Python and the Holy Grail
    text7: Wall Street Journal
    text8: Personals Corpus
    text9: The Man Who Was Thursday by G . K . Chesterton 1908



```python
help(nltk.book)


    Help on module nltk.book in nltk:

    NAME
        nltk.book

    DESCRIPTION
        # Natural Language Toolkit: Some texts for exploration in chapter 1 of the book
        #
        # Copyright (C) 2001-2019 NLTK Project
        # Author: Steven Bird <stevenbird1@gmail.com>
        #
        # URL: <http://nltk.org/>
        # For license information, see LICENSE.TXT

    FUNCTIONS
        sents()

        texts()

    DATA
        genesis = <PlaintextCorpusReader in 'C:\\Users\\ai239\\AppData\\Roamin...
        gutenberg = <PlaintextCorpusReader in 'C:\\Users\\ai239\\AppData\\Roam...
        inaugural = <PlaintextCorpusReader in 'C:\\Users\\ai239\\AppData\\Roam...
        nps_chat = <NPSChatCorpusReader in 'C:\\Users\\ai239\\AppData\\Roaming...
        print_function = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0)...
        sent1 = ['Call', 'me', 'Ishmael', '.']
        sent2 = ['The', 'family', 'of', 'Dashwood', 'had', 'long', 'been', 'se...
        sent3 = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', ...
        sent4 = ['Fellow', '-', 'Citizens', 'of', 'the', 'Senate', 'and', 'of'...
        sent5 = ['I', 'have', 'a', 'problem', 'with', 'people', 'PMing', 'me',...
        sent6 = ['SCENE', '1', ':', '[', 'wind', ']', '[', 'clop', 'clop', 'cl...
        sent7 = ['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', '...
        sent8 = ['25', 'SEXY', 'MALE', ',', 'seeks', 'attrac', 'older', 'singl...
        sent9 = ['THE', 'suburb', 'of', 'Saffron', 'Park', 'lay', 'on', 'the',...
        text1 = <Text: Moby Dick by Herman Melville 1851>
        text2 = <Text: Sense and Sensibility by Jane Austen 1811>
        text3 = <Text: The Book of Genesis>
        text4 = <Text: Inaugural Address Corpus>
        text5 = <Text: Chat Corpus>
        text6 = <Text: Monty Python and the Holy Grail>
        text7 = <Text: Wall Street Journal>
        text8 = <Text: Personals Corpus>
        text9 = <Text: The Man Who Was Thursday by G . K . Chesterton 1908>
        treebank = <BracketParseCorpusReader in 'C:\\Users\\ai239\\...Roaming\...
        webtext = <PlaintextCorpusReader in 'C:\\Users\\ai239\\AppData\\Roamin...
        wordnet = <WordNetCorpusReader in '.../corpora/wordnet' (not loaded ye...

    FILE
        c:\programming\languages\python\python37-32\lib\site-packages\nltk\book.py
```    




```python
texts()
```

    text1: Moby Dick by Herman Melville 1851
    text2: Sense and Sensibility by Jane Austen 1811
    text3: The Book of Genesis
    text4: Inaugural Address Corpus
    text5: Chat Corpus
    text6: Monty Python and the Holy Grail
    text7: Wall Street Journal
    text8: Personals Corpus
    text9: The Man Who Was Thursday by G . K . Chesterton 1908



```python
sents()
```

    sent1: Call me Ishmael .
    sent2: The family of Dashwood had long been settled in Sussex .
    sent3: In the beginning God created the heaven and the earth .
    sent4: Fellow - Citizens of the Senate and of the House of Representatives :
    sent5: I have a problem with people PMing me to lol JOIN
    sent6: SCENE 1 : [ wind ] [ clop clop clop ] KING ARTHUR : Whoa there !
    sent7: Pierre Vinken , 61 years old , will join the board as a nonexecutive director Nov. 29 .
    sent8: 25 SEXY MALE , seeks attrac older single lady , for discreet encounters .
    sent9: THE suburb of Saffron Park lay on the sunset side of London , as red and ragged as a cloud of sunset .


----
## Glossary

| Term | Definition |
|---|---|
| **token** | The technical name for a sequence of characters (such as *hairy*, *his*, or *:*) that we want to treat as a group |
| **word type** | The form or spelling of the word independently of its specific occurences in a text - that is, the word considered as a unique item of vocabulary. |
| **hapaxes** | Words that occur once only in a text |

-------------------------------------------------------------------------------------------------------------------------------
## NL Concepts

### Concordance
A `concordance` view shows us every occurence of a given word, together with some context. It permits us to see how the words are used by different authors.

Ref: http://www.nltk.org/api/nltk.html#nltk.text.Text.concordance

For example, let's check the `concordance` of the word `monstrous` in Moby Dick.


```python
text1.concordance("monstrous")
```

    Displaying 11 of 11 matches:
    ong the former , one was of a most monstrous size . ... This came towards us ,
    ON OF THE PSALMS . " Touching that monstrous bulk of the whale or ork we have r
    ll over with a heathenish array of monstrous clubs and spears . Some were thick
    d as you gazed , and wondered what monstrous cannibal and savage could ever hav
    that has survived the flood ; most monstrous and most mountainous ! That Himmal
    they might scout at Moby Dick as a monstrous fable , or still worse and more de
    th of Radney .'" CHAPTER 55 Of the Monstrous Pictures of Whales . I shall ere l
    ing Scenes . In connexion with the monstrous pictures of whales , I am strongly
    ere to enter upon those still more monstrous stories of them which are to be fo
    ght have been rummaged out of this monstrous cabinet there is no telling . But
    of Whale - Bones ; for Whales of a monstrous size are oftentimes cast up dead u


Here the contexts of `monstrous` are `most ___ size`, `that ___ bulk`, `of ___ clubs`, etc.

### Distributional Similarity
The `distributional similarity` find other words which appear in the same contexts of the specified word, listing the most similar words first.

Ref: http://www.nltk.org/api/nltk.html#nltk.text.Text.similar

With reference to the word *monstrous* used to illustrate the `concordance` concept, we can find its `distributional similarity` by executing:


```python
text1.similar("monstrous")
```

    true contemptible christian abundant few part mean careful puzzled
    mystifying passing curious loving wise doleful gamesome singular
    delightfully perilous fearless


### Common Contexts
The term `common context` allows us to examine just the contexts that are shared by two or more words.

Ref: http://www.nltk.org/api/nltk.html#nltk.text.Text.common_contexts

So, for the example used in `distributional similarity`, we know that *monstrous* and *true* are used in similar context. Which ones exactly? We can find it out by running:


```python
text1.common_contexts(["monstrous", "true"])
```

    the_pictures


### Dispersion Plot
A `dispersion plot` produce a plot showing the distribution of words through the text, by plotting the location of a word in the text, i.e. how many words from the beginning it appears. This can be useful when we investigate changes in language use over time.

Ref: http://www.nltk.org/api/nltk.html#nltk.text.Text.dispersion_plot


```python
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
```


    <IPython.core.display.Javascript object>



<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAAAgAElEQVR4Xu2dBZQcx9WFr2SKDLJjJjlmdiwzMztmdszMMTNJppgxZmY7MSWO2THF8JsZEjPHLFkmmfY/t/uUtnc0szM7NTu1u/PVOTqSdvt1V311u9+dgp5+bW1tbaJAAAIQgAAEIAABCLQMgX4YwJbpaxoKAQhAAAIQgAAEMgIYQIQAAQhAAAIQgAAEWowABrDFOpzmQgACEIAABCAAAQwgGoAABCAAAQhAAAItRgAD2GIdTnMhAAEIQAACEIAABhANQAACEIAABCAAgRYjgAFssQ6nuRCAAAQgAAEIQAADiAYgAAEIQAACEIBAixHAALZYh9NcCEAAAhCAAAQggAFEAxCAAAQgAAEIQKDFCGAAW6zDaS4EIAABCEAAAhDAAKIBCEAAAhCAAAQg0GIEMIAt1uE0FwIQgAAEIAABCGAA0QAEIAABCEAAAhBoMQIYwBbrcJoLAQhAAAIQgAAEMIBoAAIQgAAEIAABCLQYAQxgi3U4zYUABCAAAQhAAAIYQDQAAQhAAAIQgAAEWowABrDFOpzmQgACEIAABCAAAQwgGoAABCAAAQhAAAItRgAD2GIdTnMhAAEIQAACEIAABhANQAACEIAABCAAgRYjgAFssQ6nuRCAAAQgAAEIQAADiAYgAAEIQAACEIBAixHAALZYh9NcCEAAAhCAAAQggAFEAxCAAAQgAAEIQKDFCGAAW6zDaS4EIAABCEAAAhDAAKIBCEAAAhCAAAQg0GIEMIAt1uE0FwIQgAAEIAABCGAA0QAEIAABCEAAAhBoMQIYwBbrcJoLAQhAAAIQgAAEMIBoAAIQgAAEIAABCLQYAQxgi3U4zYUABCAAAQhAAAIYQDQAAQhAAAIQgAAEWowABrDFOpzmQgACEIAABCAAAQwgGoAABCAAAQhAAAItRgAD2GIdTnN7L4HLLrtM22yzjZ588kktuOCCTWtIv379dOSRR2rIkCHdcs3pp59eyy67rNy+zoqPe/fdd7NDXKcJJphAU089tRZaaCFtvvnmWnnllUcL7+66dwuQMidN1Y6guVClMcYYQ1NOOaVWWmklHXPMMZpmmmmyXz3wwANabrnldP/992d92ZXy6KOP6u6779Zee+2liSaaqCuhHAsBCEQQwABGwCMUAs0kkMoA/t///Z+mnXba7E93lK4YQNfh5JNPzqrxzTff6D//+Y+uu+46Pfzww1p//fV17bXXaqyxxhpVze6ue3fwKHfOVO0Imrv00ks1++yz6/vvv9dDDz2kP//5z5n5fvHFFzXeeONFGUD35/7776+3335b1gIFAhBoDgEMYHM4cxUIRBNIZQCjK17lBF0xgHPPPbf++c9/jnZGj04OHTpUBxxwgE444YTurnJDzv/dd99p3HHHbci5uusklTR3xBFH6Oijj9ZVV12lzTbbDAPYXR3AeSHQjQQwgN0Il1NDoJEEajWAX3/9tY466ijdeOON+vDDDzXZZJNpww031LHHHpuN1rh41GzTTTfVWWedpd13331UNT3V66m9O++8M5vmcyk3/ejz2nDdcccd+uSTTzTppJNq8cUX19lnn60ppphCP/zwgw499FD961//ykZ2PHU422yz6aCDDtLaa6/dAUsjDKBPaHPoa33xxRf6zW9+U7buNl02L2bz8ccfZwZsxhln1L777pvxcNl66611ww036PHHH9ef/vQnefTNx2288cY68cQTO5i2trY2nXvuubrggguy0Uhfd4UVVsiO83lD8bTo559/rnPOOSdj8Nxzz2mttdbK+uG+++7L+sujaa6f+8vT2ldeeeWoa5Xrg5deeilj7BE5j8x5hG7vvffWVlttNeq6YWr2mmuukY/3SJ5HThdeeOGsr9wnnZVKmrv99tv1hz/8IdPUIYccUtEA/uMf/8hGC59//vlMA4suumjW1sUWWyy7bDDupXWoZyq5kfca54JAKxDAALZCL9PGPkGgFgNoA7HEEkvogw8+yBLz73//e7388suZ6VlggQV07733ZobOZZdddtEll1yiRx55JFtTaCNi0+c4j+6EUmo+bP5sUH766adR17Dpuuuuu7KpPBuR4cOHZ2u6bIa8TuzHH3/Mrn3qqadmJmTLLbccdf5GGcCDDz5Yxx9/vP79739rySWXLGsAd95558xY2eTON998+vbbbzNjZGMcjLANoKeSvdZtp512ytrqdWqOWXXVVXXrrbeOqvuOO+6YrV20UTS7L7/8MjM4X331VWZ6bIZdbADDdKlHKW1W+/fvr+mmm05zzDGHllpqKe22227ZGjjztQE/88wzR62JK+0Dm03Xa/LJJ8/WZ04yySTZaJzr7RFQX8MlGEAzti7++Mc/yh8QDjzw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gEASAuRvDGCU8BBQFD6CIQABCEAAAkkIkL8xgFHCQ0BR+AiGAAQgAAEIJCFA/sYARgkPAUXhIxgCEIAABCCQhAD5GwMYJTwEFIWPYAhAAAIQgEASAuRvDGCU8BBQFD6CIQABCEAAAkkIkL8xgFHCQ0BR+AiGAAQgAAEIJCFA/sYARgkPAUXhIxgCEIAABCCQhAD5GwMYJTwEFIWPYAhAAAIQgEASAuRvDGCU8BBQFD6CIQABCEAAAkkIkL8xgFHCQ0BR+AiGAAQgAAEIJCFA/sYARgkPAUXhIxgCEIAABCCQhAD5GwMYJTwEFIWPYAhAAAIQgEASAuRvDGCU8BBQFD6CIQABCEAAAkkIkL8xgFHCQ0BR+AiGAAQgAAEIJCFA/sYARgkPAUXhIxgCEIAABCCQhAD5GwMYJTwEFIWPYAhAAAIQgEASAuRvDGCU8BBQFD6CIQABCEAAAkkIkL8xgFHCQ0BR+AiGAAQgAAEIJCFA/sYARgkPAUXhIxgCEIAABCCQhAD5GwMYJTwEFIWPYAhAAAIQgEASAuRvDGCU8BBQFD6CIQABCEAAAkkIkL8xgFHCQ0BR+AiGAAQgAAEIJCFA/sYARgkPAUXhIxgCEIAABCCQhAD5GwMYJTwEFIWPYAhAAAIQgEASAuRvDGCU8BBQFD6CIQABCEAAAkkIkL8xgFHCQ0BR+AiGAAQgAAEIJCFA/sYARgkPAUXhIxgCEIAABCCQhAD5GwMYJTwEFIWPYAhAAAIQgEASAuRvDGCU8BBQFD6CIQABCEAAAkkIkL8xgFHCQ0BR+AiGAAQgAAEIJCFA/sYARgkPAUXhIxgCEIAABCCQhAD5GwMYJTwEFIWPYAhAAAIQgEASAuRvDGCU8BBQFD6CIQABCEAAAkkIkL8xgFHCQ0BR+AiGAAQgAAEIJCFA/sYARgkPAUXhIxgCEIAABCCQhAD5GwMYJTwEFIWPYAhAAAIQgEASAuRvDGCU8BBQFD6CIQABCEAAAkkIkL8xgFHCQ0BR+AiGAAQgAAEIJCFA/sYARgkPAUXhIxgCEIAABCCQhAD5GwMYJTwEFIWPYAhAAAIQgEASAuRvDGCU8BBQFD6CIQABCEAAAkkIkL8xgFHCQ0BR+AiGAAQgAAEIJCFA/sYARgkPAUXhIxgCEIAABCCQhAD5GwMYJTwEFIWPYAhAAAIQgEASAuRvDGCU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3eIGMFaCCCiWIPEQgAAEIACB5hMgf2MAo1SHgKLwEQwBCEAAAhBIQoD8jQGMEh4CisJHMAQgAAEIQCAJAfI3BjBKeAgoCh/BEIAABCAAgSQEyN8YwCjhIaAofARDAAIQgAAEkhAgf2MAo4SHgKLwEQwBCEAAAhBIQoD8jQGMEh4CisJHMAQgAAEIQCAJAfI3BjBKeAgoCh/BEIAABCAAgSQEyN8YwCjhIaAofARDAAIQgAAEkhAgf2MAo4SHgKLwEQwBCEAAAhBIQoD8jQGMEh4CisJHMAQgAAEIQCAJAfI3BjBKeAgoCh/BEIAABCAAgSQEyN8YwCjhIaAofARDAAIQgAAEkhAgf2MAo4SHgKLwEQwBCEAAAhBIQoD8jQGMEh4CisJHMAQgAAEIQCAJAfI3BjBKeAgoCh/BEIAABCAAgSQEyN8YwCjhIaAofARDAAIQgAAEkhAgf2MAo4SHgKLwEQwBCEAAAhBIQoD8jQGMEh4CisJHMAQgAAEIQCAJAfI3BjBKeAgoCh/BEIAABCAAgSQEyN8YwCjhIaAofARDAAIQgAAEkhAgf2MAo4SHgKLwEQwBCEAAAhBIQoD8jQGMEh4CisJHMAQgAAEIQCAJAfI3BjBKeAgoCh/BEIAABCAAgSQEyN8YwCjhIaAofARDAAIQgAAEkhAgf2MAo4SHgKLwEQwBCEAAAhBIQoD8jQGMEh4CisJHMAQgAAEIQCAJAfI3BjBKeAgoCh/BEIAABCAAgSQEyN8YwCjhIaAofARDAAIQgAAEkhAgf2MAo4SHgKLwEQwBCEAAAhBIQoD8jQGMEh4CisJHMAQgAAEIQCAJAfI3BjBKeAgoCh/BEIAABCAAgSQEyN8YwCjhIaAofARDAAIQgAAEkhAgf2MAo4SHgKLwEQwBCEAAAhBIQoD8jQGMEh4CisJHMAQgAAEIQCAJAfI3BjBKeAgoCh/BEIAABCAAgSQEyN8YwCjhIaAofARDAAIQgAAEkhAgf2MAo4SHgKLwEQwBCEAAAhBIQoD8jQGMEh4CisJHMAQgAAEIQCAJAfI3BjBKeAgoCh/BEIAABCAAgSQEyN8YwCjhIaAofARDAAIQgAAEkhAgf2MAo4SHgKLwEQwBCEAAAhBIQoD8jQGMEh4CisJHMAQgAAEIQCAJAfI3BjBKeAgoCh/BEIAABCAAgSQEyN8YwCjhIaAo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gXYPb6mlBPQ3/V33Q7IXBaLz1tJ5L5KmMIA9sLd4YLTWA4P+pr974GOo4VVC5+i84aLihFEEMIBR+LonmAclD8ruUVbPOis6R+c9S5HdUxt03lo67x4Vdc9ZMYDdwzXqrCNHjtSf//xnHXzwwRpnnHGiztWbgmk3/d2b9FpvXdE5Oq9XO70prlV13pv6CAPYm3qLukIAAhCAAAQgAIEGEMAANgAip4AABCAAAQhAAAK9iQAGsDf1FnWFAAQgAAEIQAACDSCAAWwARE4BAQhAAAIQgAAEehMBDGBv6i3qCgEIQAACEIAABBpAAAPYAIiNPMU555yjk046SR9//LHmmmsunX766VpqqaUaeYmGncs7lW+66Sa99tprGjBggBZffHGdcMIJmm222UZdwzvB9ttvP1177bX6/vvvtcIKK8htLH71znvvvafddttN9913X3aeP/7xjzr55JM19thjjzrPgw8+qH322Ucvv/xy9ub2Aw44QDvvvHOHtqRiZw6HHHKI9txzz6y/XPpquz/88EMdeOCBuuOOO7L+nHXWWXXxxRdrgQUWyNrtt+sPHTpUF1xwgb766istssgiOvvsszMth+Kf/+lPf9I//vGP7EdrrbWWzjrrrOx7tUN58cUXtfvuu+uJJ57QxBNPrJ122kmHH354h2/cufHGG7Ofvfnmm5ppppl07LHHat11122YvsOJfv75Zw0ZMkRXX321/ve//2mqqabS1ltvrcMOO2zUNwj0hXY/9NBD2bPn6aefzp4/N998s9ZZZ51RPHtSG2upS61C6KzdP/30U9bPt99+u956663sO2NXXHFFHX/88dlzqNmabla7S9n5/vM9fdppp2mvvfbq1e2uVRetcBwGsAf18vXXX68tttgiM0hLLLGEzj//fF100UV65ZVXNN100/WgmuZVWXXVVbXJJptooYUWkpPkoYceKidu13e88cbLjtlll11066236rLLLtMkk0yifffdV19++WWWZMYYYwz98ssvGjx4sCabbDKdcsop+uKLL7TVVltpvfXWy0yBy9tvv625555bO+ywQ2YEHnnkEe26666ZqVx//fWzY1Kxe/LJJ7XRRhtl3+Cx3HLLjTKAfbHdNm7zzTdf1k63b/LJJ8/M1/TTT58ZMBd/ALARc3/bHB5zzDFygv3Pf/6TfWWiy2qrrSZ/j7YTisuOO+6Y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U4leO+jiZQDWd3gNjD84WE/LL798tvbOidea8Iah8BoYG05vDvISCX9Asgb9vrbueA2Mr+2F/66vp4C9IcV13nbbbbP29pV2e1e7N3K5eBOPp7i9Ccv3rTfd9KS+raUutT4vO2u3pz+949tToX6O+TkVirmEDyj+8NEMTTer3eVeO1Y6BWwOvbHdteqiFY7DAPawXvbo34knnph9+vJOWu9sdKLricWflssVj4w4abp4PZbXT9koFl8E7VGyULymxmay9EXQ3ggSinedevQhvAjaI23lXgSdil2pAeyr7XYS9OYHmzJP93uaKOwCdl+FF9XaLBVfBG0th2KTX/oi6L/85S+jvQjaU642md5B7r62ASxq7oYbbshMX5gasxn0+yMbXTzS6BdOe6Tbo9I2BV576PoEA9AX2m2jbsNXWjwa7w9wPamNtdSlVh101m6//664rKV4To8G+r53aZamm9Vu93dpKWcAe2O7a9VFKxyHAWyFXqaNEIAABCAAAQhAoEAAA4gcIAABCEAAAhCAQIsRwAC2WIfTXAhAAAIQgAAEIIABRAMQgAAEIAABCECgxQhgAFusw2kuBCAAAQhAAAIQwACiAQhAAAIQgAAEINBiBDCALdbhNBcCEIAABCAAAQhgANEABCAAAQhAAAIQaDECGMAW63CaCwEItBMofYF3LBu/ONjfj+wXRvvF0f5Gm3I/i70O8RCAAARiCWAAYwkSDwEIdJmAv7LP3xDjbwsZc8wxs3h/JZe/9cPfC1z8vmH/29+G46+Tm3XWWbt8rc4CajGA/gab448/Xtddd53eeecdTTDBBNk3QPgr8fzVcKGE70a18XMb3BZ/S4m/z7v4s+I33NTTmHLfV1vPeYiBAARamwAGsLX7n9ZDIAkBm7nZZ589+15nmyWXO+64I/uO3c8++yz7aq1xxx03+/nRRx8tG8YPP/ywrrr+9NNPGmusscrGVjOAI0eOzL6T2F9XeMopp2iRRRbRJ598kn3f8T333JN9R3Cov78mb80119Svv/466ivryv2srkYUgjCAsQSJhwAETAADiA4gAIEkBKaZZhrtscceOuigg7Lr+/udv/32W/k7Vs844wytuOKK2c9XWGEFTTXVVLrqqquy/9uMOe5f//qX+vfvr1VXXVVnnXWWpphiiuz3nnK95ZZbsu8bPuaYY7JRu19++UXfffeddtllF910003ZKN5+++2nW2+9VYMHD9bpp59elsEJJ5yQfffxs88+q3nnnXfUMTZ5NoM+50svvZSNBvpPsRx55JGj/czf5ervnj3ggAOy77W2MfUoor8r+3e/+10W7jq5DeF7r/1dvIceemg2UurvY3333XdHXcYxbh8FAhCAQFcJYAC7SozjIQCBhhDYbLPN9Pnnn+uuu+7Kzrfwwgtnxui+++7Lpk+PPfZY/fjjj5poookyg7fddtvJBmqBBRbQeOONl5m2n3/+Wbvuumtm6GysggE8+eSTteSSS2YjdWOMMYbmmWce7bbbbpm5uuSSSzTllFPqkEMOyWJ83koG0KbPx4Y6Fhtu0+Y22BzOPPPMuuGGG7TNNtvo448/zg4bf/zxR/vZpJNOKv/ZYYcdtPPOO2fte+KJJ7Tccstpuummy66z0UYb6cwzz9RSSy2lN998MxsV3XrrrWVD6dHRySefXJdeemlmfN22ySabrCH9wUkgAIHWIoABbK3+prUQ6DEELrzwQu29994aNmyYvM5u4oknzqZ5PQJoA/TII4/ooYce0jLLLJMZoRlnnDGbdl1ttdX09ttva9CgQVlbXnnllWwUzUZqoYUWykbPjjvuuOxcwRx5feEkk0yiK664QhtvvHEW52nmaaedNjNYlQzggAEDtNNOO5X9vY3f/PPPr+uvvz4zbR51XHfddTOTGkrpz3xN18PG0+0qLV7r6PZ51DEUj3zaGH/00UfZj5gC7jESpiIQ6NUEMIC9uvuoPAR6L4E33nhDs8wyix599NFsM4g3hXja83//+182Guafed3dxRdfPGra08bwtNNOywxgsXjE0NPGW265ZWYAr776ar3++uujDnn++eezqV5Pn/rcocw333yZEavHAD7zzDPZaORf//pXbbjhhjUZQF/Xo4TXXnutVlpppWya2+bRU9wuHtn09LJH9kLx9PUPP/yQTY97XSQGsPdqnppDoCcRwAD2pN6gLhBoMQIexfO6PJs9G5xzzjknIzDbbLNl076ewvW6N095utjk+Y931xZLmCbeYostRq0BfO6550Yd4n/b7HXVAHoK2GsL77777tF6pjgFbHNZywhgOIlHD++8885sSvrFF1/MRja9mcQjjl5LuN566412PY+Aes0jBrDFbhKaC4FuIoAB7CawnBYCEKhOwCN2HvELI4AeDXPxtKzX9dkQnn/++dnInktnU8BPPvmkFlxwwbIG0FPAnmL2dGq4hq/pKWCvx6s0AmgD6g0Y1TaB2JR1xQAWySy22GLZ1LVHN5dYYolsd7RHPSuVscceOxtBXH/99asD5ggIQAACFQhgAJEGBCCQjIBH9rw5w69q+eCDD0bt5PUUrkcGR4wYke36Dev9wiYQb7AobgLx/4ubQGzGiiOAbqDPd/vtt2ebQDyqZ2PnDSedbQLx1KtfFeP1d8XXwHiNYelrYGoxgJ66vuCCC7TWWmtp6qmnzt5tuOmmm2a7lV0/bwJZY401srp5Wtkjfi+88EI2SuhjXPwuRE8dH3HEEfI7BT39TYEABCDQVQIYwK4S43gIQKBhBPwKkxlmmCEb9fKLlEOxGbTpm2mmmeS1gsVS62tgSg2gRwGLr4HZd999ddttt3X6Ghhf16968UigXwTtKWSPTHrXrtd52qQFAAABM0lEQVQazj333KOqVosB9DsEvfv38ccf1xdffJGt/fNrXrzD12bPxSbwqKOOykYd/ZoYs9l+++2zkUoXTxvvs88+2etf/CodXgPTMDlyIgi0FAEMYEt1N42FAAQgAAEIQAACvAgaDUAAAhCAAAQgAIGWI8AIYMt1OQ2GAAQgAAEIQKDVCWAAW10BtB8CEIAABCAAgZYjgAFsuS6nwRCAAAQgAAEItDoBDGCrK4D2QwACEIAABCDQcgQwgC3X5TQYAhCAAAQgAIFWJ4ABbHUF0H4IQAACEIAABFqOAAaw5bqcBkMAAhCAAAQg0OoEMICtrgDaDwEIQAACEIBAyxHAALZcl9NgCEAAAhCAAARanQAGsNUVQPshAAEIQAACEGg5AhjAlutyGgwBCEAAAhCAQKsT+H/bAoaJZX87dgAAAABJRU5ErkJggg==" width="640">


### Lexical Diversity

A measure of the lexical richness of the text: is the ratio of word types to the total number of tokens in a text. It measures how many times a word is used - on average - throughout the text.

### Frequency Distribution

A **frequency distribution** tells us the frequency of each vocabulary item in the text.

Ref: http://www.nltk.org/api/nltk.html#nltk.probability.FreqDist


```python
fdist = FreqDist(text3)
print(fdist)
```

    <FreqDist with 2789 samples and 44764 outcomes>


---
## Usage Examples

### Counting Vocabulary

In this section we will see how to count the words in a text.

We can find the total number of tokens in a text by using the function `len`.


```python
total_tokens = len(text3)
print("Total tokens in the book of Genesis : ", total_tokens)
```

    Total tokens in the book of Genesis :  44764


This number includes duplicated tokens, i.e. tokens that appears more than once. If we want to known how many distinct tokens are in the text, we can use the function `set`:


```python
unique_tokens = sorted(set(text3))
total_unique_tokens = len(unique_tokens)
print("First 50 unique tokens in the book of Genesis : ", unique_tokens[:50])
print("Total Word Types : ", total_unique_tokens)
```

    First 50 unique tokens in the book of Genesis :  ['!', "'", '(', ')', ',', ',)', '.', '.)', ':', ';', ';)', '?', '?)', 'A', 'Abel', 'Abelmizraim', 'Abidah', 'Abide', 'Abimael', 'Abimelech', 'Abr', 'Abrah', 'Abraham', 'Abram', 'Accad', 'Achbor', 'Adah', 'Adam', 'Adbeel', 'Admah', 'Adullamite', 'After', 'Aholibamah', 'Ahuzzath', 'Ajah', 'Akan', 'All', 'Allonbachuth', 'Almighty', 'Almodad', 'Also', 'Alvah', 'Alvan', 'Am', 'Amal', 'Amalek', 'Amalekites', 'Ammon', 'Amorite', 'Amorites']
    Total Word Types :  2789



```python
lexical_diversity = total_unique_tokens / total_tokens
print("Lexical Diversity of the book of Genesis : ", lexical_diversity)
average_word_repetition = 1 / lexical_diversity
print("Each word is repeated an average of", average_word_repetition, "times")
```

    Lexical Diversity of the book of Genesis :  0.06230453042623537
    Each word is repeated an average of 16.050197203298673 times


Let's see how the word types are distributed inside the text, i.e. what are the words that appear more in the Book of Genesis?


```python
fdist = FreqDist(text3)
print(fdist)
print("The 50 most common words in the book of Genesis are : ", fdist.most_common(50))
fdist.plot(50, cumulative=True)
cumulative_count = 0
for word in fdist.most_common(50):
    cumulative_count = cumulative_count + word[1]
print("The 50 most common words accounts for", 100 * cumulative_count / total_tokens, "% of the total")
```

    <FreqDist with 2789 samples and 44764 outcomes>
    The 50 most common words in the book of Genesis are :  [(',', 3681), ('and', 2428), ('the', 2411), ('of', 1358), ('.', 1315), ('And', 1250), ('his', 651), ('he', 648), ('to', 611), (';', 605), ('unto', 590), ('in', 588), ('that', 509), ('I', 484), ('said', 476), ('him', 387), ('a', 342), ('my', 325), ('was', 317), ('for', 297), ('it', 290), ('with', 289), ('me', 282), ('thou', 272), ("'", 268), ('is', 267), ('thy', 267), ('s', 263), ('thee', 257), ('be', 254), ('shall', 253), ('they', 249), ('all', 245), (':', 238), ('God', 231), ('them', 230), ('not', 224), ('which', 198), ('father', 198), ('will', 195), ('land', 184), ('Jacob', 179), ('came', 177), ('her', 173), ('LORD', 166), ('were', 163), ('she', 161), ('from', 157), ('Joseph', 157), ('their', 153)]



    <IPython.core.display.Javascript object>



<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAAAgAElEQVR4Xux9B5hWxfn92Qos7FKX3ntTkCIdBRULBhWNBUUxxhr1FzWxRpQYjdEktn8UO4qCvQOWqJSlS0fpdel9qQvL7v6fuWTX/ba+zHdn7nz7nfs8PJR95865Z8687+HeO3NjcnNzc8GDDJABMkAGyAAZIANkIGoYiKEBjJqx5oWSATJABsgAGSADZMBjgAaQQiADZIAMkAEyQAbIQJQxQAMYZQPOyyUDZIAMkAEyQAbIAA0gNUAGyAAZIANkgAyQgShjgAYwygacl0sGyAAZIANkgAyQARpAaoAMkAEyQAbIABkgA1HGAA1glA04L5cMkAEyQAbIABkgAzSA1AAZIANkgAyQATJABqKMARrAKBtwXi4ZIANkgAyQATJABmgAqQEyQAbIABkgA2SADEQZAzSAUTbgvFwyQAbIABkgA2SADNAAUgNkgAyQATJABsgAGYgyBmgAo2zAeblkgAyQATJABsgAGaABpAbIABkgA2SADJABMhBlDNAARtmA83LJABkgA2SADJABMkADSA2QATJABsgAGSADZCDKGKABjLIB5+WSATJABsgAGSADZIAGkBogA2SADJABMkAGyECUMUADGGUDzsslA2SADJABMkAGyAANIDVABsgAGSADZIAMkIEoY4AGMMoGnJdLBsgAGSADZIAMkAEaQGqADJABMkAGyAAZIANRxgANYJQNOC+XDJABMkAGyAAZIAM0gNQAGSADZIAMkAEyQAaijAEawCgbcF4uGSADZIAMkAEyQAZoAKkBMkAGyAAZIANkgAxEGQM0gFE24LxcMkAGyAAZIANkgAzQAFIDZIAMkAEyQAbIABmIMgZoAKNswHm5ZIAMkAEyQAbIABmgAaQGyAAZIANkgAyQATIQZQzQAEbZgPNyyQAZIANkgAyQATJAA0gNkAEyQAbIABkgA2QgyhigAYyyAeflkgEyQAbIABkgA2SABpAaIANkgAyQATJABshAlDFAAxhlA87LJQNkgAyQATJABsgADSA1QAbIABkgA2SADJCBKGOABjDKBpyXSwbIABkgA2SADJABGkBqgAyQATJABsgAGSADUcYADWCUDTgvlwyQATJABsgAGSADNIDUABkgA2SADJABMkAGoowBGsAoG3BeLhkgA2SADJAB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42JDKmlZ/fmZA3RLuMn6rYvJdjsawDAYNykgmxPIr778nNR+YZKch7jtFiPyTb45L+1qoDDfubm5WLn9oHeHL23VTsxetweHj2UXWw1jY4BOjaqhb8ta3nt8pzZIxk+zZ1q5uyfViU4ZN1m/dfAE0caqAfz73/+OTz75BMuXL0elSpXQu3dv/OMf/0CbNm3yr/3MM8/ElClTQri44oor8N577+X/2969e3HnnXfiiy++8P5tyJAheOGFF1CtWrX8mCVLluD222/HnDlzUKNGDdx88814+OGHQ95F+Pjjj71/W7NmDVq0aIHHH38cl1xyiXgcTApIInzXYljY7SZ18k2+JTmAOqFOlE6++n4asmo0x4y1ez3jt/NAye/xtUitjH6tUr3HuurxbtVKCfl1UaI5mzHigl0o0GT91sVku51VA3jeeefhyiuvRPfu3b0VQA899BCUUfvll19QuXJl79qVAWzdujX++te/5nOhzGLVqlXz/37++edj06ZNeOWVV7x/u+mmm9C0aVN8+eWX3t/VwKpzDBgwwOtj5cqVGDFiBB555BHcc889XszMmTPRr18/PPbYY57p+/TTTzFy5EikpaWhR48eonEwKSCbE8ivvlhoWGgkWqJOqBPqxLwG1Bc31J29tFW7MHXlzlLf40tNrnDiDl/z6ojfsxa/OSu8rVkk4+tXjKhYFxNksn7rYrLdzqoBLHxxO3fuRO3atb07fv379883gJ07d8azzz5bLBfLli1D+/btMWvWrHyjpv7cq1cv786iupv40ksv4YEHHsD27dtRocKJTSWffPJJ7y6hMo7qe4LqrqISwKRJk/L7UQa1evXqGD9+vGgcTArIr8lh8zws7OaTemFh2hxfv/qiTqgTiZaok5PTSa9evbFy52FMW7UL01bt9D63diy7+A2YkxLjvJW6fVulesavdZ0qXl2UjItrMaJiTQNYLE2BGsDVq1ejVatW3l3Ajh075hvAn3/+GeodhTp16kDd7VN37pKTk72fv/HGG7j77ruxb9++kAtSj3+feeYZXH/99bj22muRkZGBzz//PD9mwYIF6NKlC9auXYtmzZqhcePGuOuuu7xfeYdqr4znhg0biiXr6NGjUL/yDmUAGzVqhN27dyMlJUVXh8W2U5Ns9uzZnskt7burLsXkJWyXMEl4JO4ThcbWuJFv8i3RG3VStk7U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9p9IBVQNqAZUA6oB1YBqQDVQrAaUABarT32aakA1oBpQDagGVAOqgdprQAlg7T+RCqgaUA2oBlQDqgHVgGqgWA0oASxWn/o01YBqQDWgGlANqAZUA7XXgBLA2n8iFVA1oBpQDagGVAOqAdVAsRpQAlisPmv9tB133NFcdtllQYLmP/3pT+YnP/lJ4gnjWndEhauNBj7//HMzceJEs/7665sllliiNnLVUZCPP/7YcPvAwgsvHIj36quvmhtuuMGss846ZujQoXUUuaVl4lu89tprZpllljELLbRQS/e1WTrHXctXXHGF+fa3v22WW265ZhG7aeVUAti0ny5b8E8++cQsuOCC8yp27do1MDrLL7+86dKli3nrrbeCya9ZC3cxcwXfiiuuWFkXkvT43nvvBbqFIKWVp556Siw7JKvR8uyzzwZGbs6cOR2abr/99qJHSUgLGHvuuefMqquuKnpmWiUuZn/kkUfMO++8Y7hqMVx23XVX8fMnTJiQWnfzzTcXPyur4iqrrGJ+8YtfmN13392svPLKidUheSzC9t133+AC+rXWWssssMACZvr06ebMM880++23X9CW38aOHWv+9a9/mcMPP9wsueSS5vHHHzfLLrtsoVhnMfjjH/94HiENC07eOGlJuvFH2j6p3ocffjgfBhp9Fxj65z//GYunTTfdNJgfn3nmGdOnT5+84ma2f+GFF8w555wTjBXmLb7/L3/5S7PmmmvO17YsDPBiSNf48eMDvP3sZz8LrjblilN0veiii86Tjd/HjBkT1Pv9738fzG+333676dmzp1l33XUz+0+Fu+++O/gXN74vvfTS4BkskNBRr169RM/USu4aUALorrvSWuJZYUJoa2sLBgekI6lgTE4++WRz4YUXmmnTppkXX3zRrLbaaua4444LBu/WW29tttxyS7PHHnuYs88+O/G6tjRju+GGGwaTALmlsgY+hiup0KfFF1+8w89ZEx8T+kknnWR++9vfGgwEhQnr0EMPNcccc0zDdzryvj/+8Y/zJuW1117b7LnnnsH1YpLCHZJvv/32fESaCXT11Vc3ECiMflLBA2RL1n2UWWQy/I6XX37Z/OAHPzBTpkwJjA3eDoq9s5pn/fvf/84kbRLS8q1vfcuMHj3abLXVVqkqyyLLN954o/n5z39uZs2aNd/92sg9Y8aMDs/HsINDyBweHPpo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" width="640">


    The 50 most common words accounts for 57.88803502814762 % of the total


What about the hapaxes in the book?


```python
hapaxes = fdist.hapaxes()
print("There are", len(hapaxes), "hapaxes in the Book of Genesis. 20 of them are:", hapaxes[:20])
```

    There are 1195 hapaxes in the Book of Genesis. 20 of them are: ['form', 'void', 'Day', 'Night', 'firmame', 'Heaven', 'appe', 'Earth', 'signs', 'seasons', 'lesser', 'nig', 'darkne', 'fly', 'whales', 'winged', 'seas', 'likene', 'subdue', 'finished']


Let's see if we can find words that can characterize a text, since neither the most common nor the hapaxes seems to help in this task. Let's search for long words that appears often in the text. What does *long* and *often* mean here? Well, for example, more than average.


```python
total_chars = 0
for w in fdist:
    total_chars = total_chars + (len(w) * fdist[w])
average_chars_per_word = total_chars / total_tokens
print("The average word length is:", average_chars_per_word)
print("Each word appears", average_word_repetition, "on average")
long_words = [w for w in fdist if len(w) > average_chars_per_word and fdist[w] > average_word_repetition]
print("There are", len(long_words), "words over the average:", long_words)
```

    The average word length is: 3.5129791796979717
    Each word appears 16.050197203298673 on average
    There are 203 words over the average: ['heaven', 'earth', 'upon', 'face', 'waters', 'said', 'there', 'that', 'good', 'from', 'called', 'morning', 'were', 'made', 'which', 'under', 'unto', 'place', 'land', 'bring', 'forth', 'seed', 'tree', 'after', 'brought', 'night', 'them', 'days', 'give', 'great', 'also', 'over', 'hath', 'life', 'every', 'their', 'blessed', 'saying', 'multiply', 'cattle', 'thing', 'beast', 'make', 'have', 'Behold', 'given', 'shall', 'behold', 'very', 'because', 'These', 'when', 'they', 'LORD', 'field', 'before', 'ground', 'went', 'into', 'whom', 'sight', 'food', 'water', 'thence', 'name', 'where', 'same', 'toward', 'took', 'commanded', 'thou', 'shalt', 'should', 'will', 'Adam', 'what', 'gave', 'found', 'flesh', 'taken', 'woman', 'This', 'father', 'mother', 'wife', 'both', 'more', 'know', 'then', 'your', 'eyes', 'with', 'knew', 'heard', 'voice', 'told', 'thee', 'What', 'this', 'hast', 'done', 'between', 'children', 'bread', 'hand', 'take', 'sent', 'conceived', 'bare', 'again', 'brother', 'sheep', 'time', 'came', 'pass', 'well', 'rose', 'against', 'come', 'dwelt', 'city', 'born', 'begat', 'wives', 'dwell', 'sister', 'lived', 'hundred', 'thirty', 'years', 'sons', 'daughters', 'died', 'five', 'seven', 'three', 'Noah', 'hands', 'even', 'covenant', 'according', 'house', 'returned', 'until', 'spake', 'Canaan', 'tent', 'brethren', 'servant', 'servants', 'these', 'nations', 'Sodom', 'down', 'people', 'left', 'Abram', 'Sarai', 'daughter', 'bless', 'famine', 'Egypt', 'near', 'pray', 'Pharaoh', 'camels', 'tell', 'therefore', 'away', 'flocks', 'Then', 'thine', 'king', 'himself', 'Ishmael', 'Abraham', 'among', 'money', 'Sarah', 'Isaac', 'stood', 'little', 'lord', 'answered', 'firstborn', 'drink', 'Abimelech', 'dream', 'Rebekah', 'master', 'Laban', 'words', 'Esau', 'Jacob', 'corn', 'Rachel', 'Leah', 'Judah', 'Joseph', 'Israel', 'Shechem', 'Benjamin', 'duke']


To Read - Chapter 1 : section 3.3
