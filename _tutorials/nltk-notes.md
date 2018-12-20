---
title: "Notes on learning NLTK"
description: "In this tutorial I collected a bunch of notes I used during the study of the book *Natural Language Processing with Python*"
last_update: "2018-11-04"
published: false
---
# Notes on learning NLTK
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

This notebook is a collection of notes and codes developed during my studies of the NLTK library.

In this notebook I will follow the [Natural Language Processing with Python](http://www.nltk.org/book/) book, focusing exclusively on the NLTK argument, skipping all the Python related parts of the book. **This is NOT a replacement for reading the book and walk the path yourself!**

## Index
* [Setting Up The Environment](#Setting-Up-The-Environment)
* [NLTK Corpora](#NLTK-Corpora)
    * [Book Corpus](#Book-Corpus)
* [NL Concepts](#NL-Concepts)
    * [Concordance](#Concordance)
    * [Distributional Similarity](#Distributional-Similarity)
    * [Common Contexts](#Common-Contexts)
    * [Dispersion Plot](#Dispersion-Plot)

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
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package abc is already up-to-date!
    [nltk_data]    | Downloading package brown to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package brown is already up-to-date!
    [nltk_data]    | Downloading package chat80 to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package chat80 is already up-to-date!
    [nltk_data]    | Downloading package cmudict to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package cmudict is already up-to-date!
    [nltk_data]    | Downloading package conll2000 to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package conll2000 is already up-to-date!
    [nltk_data]    | Downloading package conll2002 to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package conll2002 is already up-to-date!
    [nltk_data]    | Downloading package dependency_treebank to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package dependency_treebank is already up-to-date!
    [nltk_data]    | Downloading package genesis to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package genesis is already up-to-date!
    [nltk_data]    | Downloading package gutenberg to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package gutenberg is already up-to-date!
    [nltk_data]    | Downloading package ieer to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package ieer is already up-to-date!
    [nltk_data]    | Downloading package inaugural to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package inaugural is already up-to-date!
    [nltk_data]    | Downloading package movie_reviews to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package movie_reviews is already up-to-date!
    [nltk_data]    | Downloading package nps_chat to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package nps_chat is already up-to-date!
    [nltk_data]    | Downloading package names to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package names is already up-to-date!
    [nltk_data]    | Downloading package ppattach to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package ppattach is already up-to-date!
    [nltk_data]    | Downloading package reuters to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package reuters is already up-to-date!
    [nltk_data]    | Downloading package senseval to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package senseval is already up-to-date!
    [nltk_data]    | Downloading package state_union to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package state_union is already up-to-date!
    [nltk_data]    | Downloading package stopwords to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package stopwords is already up-to-date!
    [nltk_data]    | Downloading package swadesh to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package swadesh is already up-to-date!
    [nltk_data]    | Downloading package timit to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package timit is already up-to-date!
    [nltk_data]    | Downloading package treebank to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package treebank is already up-to-date!
    [nltk_data]    | Downloading package toolbox to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package toolbox is already up-to-date!
    [nltk_data]    | Downloading package udhr to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package udhr is already up-to-date!
    [nltk_data]    | Downloading package udhr2 to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package udhr2 is already up-to-date!
    [nltk_data]    | Downloading package unicode_samples to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package unicode_samples is already up-to-date!
    [nltk_data]    | Downloading package webtext to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package webtext is already up-to-date!
    [nltk_data]    | Downloading package wordnet to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package wordnet is already up-to-date!
    [nltk_data]    | Downloading package wordnet_ic to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package wordnet_ic is already up-to-date!
    [nltk_data]    | Downloading package words to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package words is already up-to-date!
    [nltk_data]    | Downloading package maxent_treebank_pos_tagger to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package maxent_treebank_pos_tagger is already up-
    [nltk_data]    |       to-date!
    [nltk_data]    | Downloading package maxent_ne_chunker to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package maxent_ne_chunker is already up-to-date!
    [nltk_data]    | Downloading package universal_tagset to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package universal_tagset is already up-to-date!
    [nltk_data]    | Downloading package punkt to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package punkt is already up-to-date!
    [nltk_data]    | Downloading package book_grammars to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package book_grammars is already up-to-date!
    [nltk_data]    | Downloading package city_database to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package city_database is already up-to-date!
    [nltk_data]    | Downloading package tagsets to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package tagsets is already up-to-date!
    [nltk_data]    | Downloading package panlex_swadesh to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package panlex_swadesh is already up-to-date!
    [nltk_data]    | Downloading package averaged_perceptron_tagger to
    [nltk_data]    |     C:\Users\mary\AppData\Roaming\nltk_data...
    [nltk_data]    |   Package averaged_perceptron_tagger is already up-
    [nltk_data]    |       to-date!
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
```

    Help on module nltk.book in nltk:

    NAME
        nltk.book

    DESCRIPTION
        # Natural Language Toolkit: Some texts for exploration in chapter 1 of the book
        #
        # Copyright (C) 2001-2018 NLTK Project
        # Author: Steven Bird <stevenbird1@gmail.com>
        #
        # URL: <http://nltk.org/>
        # For license information, see LICENSE.TXT

    FUNCTIONS
        sents()

        texts()

    DATA
        genesis = <PlaintextCorpusReader in 'C:\\Users\\mary\\AppData\\Roaming...
        gutenberg = <PlaintextCorpusReader in 'C:\\Users\\mary\\AppData\\Roami...
        inaugural = <PlaintextCorpusReader in 'C:\\Users\\mary\\AppData\\Roami...
        nps_chat = <NPSChatCorpusReader in 'C:\\Users\\mary\\AppData\\Roaming\...
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
        treebank = <BracketParseCorpusReader in 'C:\\Users\\mary\\A...Roaming\...
        webtext = <PlaintextCorpusReader in 'C:\\Users\\mary\\AppData\\Roaming...
        wordnet = <WordNetCorpusReader in '.../corpora/wordnet' (not loaded ye...

    FILE
        c:\users\mary\appdata\local\programs\python\python37-32\lib\site-packages\nltk\book.py





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



<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAsAAAAIQCAYAAACPEdjAAAAgAElEQVR4Xu2dB5QcxdWFr0DkaECAQAKJjEGYKHKQycnknHM20WSDZHLOYIwxOecMBkyOIphgMDkIEDbBIDII9J/b/fdu72hmp2d3Zt+s9qtzOMBOd73qr1/13L7zurrXmDFjxogGAQhAAAIQgAAEIACBHkKgFwK4h5xpDhMCEIAABCAAAQhAICGAACYRIAABCEAAAhCAAAR6FAEEcI863RwsBCAAAQhAAAIQgAACmByAAAQgAAEIQAACEOhRBBDAPep0c7AQgAAEIAABCEAAAghgcgACEIAABCAAAQhAoEcRQAD3qNPNwUIAAhCAAAQgAAEIIIDJAQhAAAIQgAAEIACBHkUAAdyjTjcHCwEIQAACEIAABCCAACYHIAABCEAAAhCAAAR6FAEEcI863RwsBCAAAQhAAAIQgAACmByAAAQgAAEIQAACEOhRBBDAPep0c7AQgAAEIAABCEAAAghgcgACEIAABCAAAQhAoEcRQAD3qNPNwUIAAhCAAAQgAAEIIIDJAQhAAAIQgAAEIACBHkUAAdyjTjcHCwEIQAACEIAABCCAACYHIAABCEAAAhCAAAR6FAEEcI863RwsBCAAAQhAAAIQgAACmByAAAQgAAEIQAACEOhRBBDAPep0c7AQgAAEIAABCEAAAghgcgACEIAABCAAAQhAoEcRQAD3qNPNwUIAAhCAAAQgAAEIIIDJAQhAAAIQgAAEIACBHkUAAdyjTjcHCwEIQAACEIAABCCAACYHIAABCEAAAhCAAAR6FAEEcI863RwsBCAAAQhAAAIQgAACmByAAAQgAAEIQAACEOhRBBDAPep0c7AQgAAEIAABCEAAAghgcgACEIAABCAAAQhAoEcRQAD3qNPNwUIAAhCAAAQgAAEIIIDJAQhAAAIQgAAEIACBHkUAAdyjTjcHCwEIQAACEIAABCCAACYHIAABCEAAAhCAAAR6FAEEcI863RwsBCAAAQhAAAIQgAACmByAAAQgAAEIQAACEOhRBBDAPep0c7AQgAAEIAABCEAAAghgcgACEIAABCAAAQhAoEcRQAD3qNPNwUIAAhCAAAQgAAEIIIDJAQhAoCkI9OrVS9tss40uvvjiho5n6NChGjZsmN555x0NGDCgIbF8DNttt50eeOABrbDCCg2JEdWpj+fdd99N/ukuratyq7vwYJwQgICEACYLIAABPfjggxoyZIiOOuooHX744SFEukqk1CKAs20zIL1799aUU06pWWaZRYsttpg233zzsgIXAdz4FHK+5NuEE06omWeeWauuuqqOOOII9e3bt+XjzubWzTffrH/+859yPtAgAIFxgwACeNw4jxwFBDpFoBkE8Pfff6/xxx9fE0wwQaeOpdrOHRHAf/zjHzXXXHPpl19+0ZdffqlXXnlFFkUff/yx1l57bV155ZWafPLJW0L//PPP+umnn2RRNt5441UbUrf6/Mcff9SYMWM00UQThY7bona++ebTwQcfnIzD58WO+w033KD+/fsngnWaaaZJPuusAN522211ySWXJMdNgwAExg0CCOBx4zxyFBDoFIFmEMCdOoAadu6IAH7kkUe0zDLLtIliIbj33nvrz3/+s9ZZZ51EEHfH9s0332iyySbrdkO3qF1xxRV13333tRn7HnvsoXPPPVcnnXSSDjjgAARwtzuzDBgCXUMAAdw1nIkCgaYmUIsAtgv217/+VRdccIH+9a9/Jcf1m9/8RgceeKDWXXfdluP05zvvvHMiQixGsvbtt98m5QMfffSRnn/++ZY63EouncXnySefrMcff1yjRo3SDDPMkIhRl2vMPvvsSbd///vfddFFF+npp59O+rWLvNBCCyVjWnPNNduwr5cAdqdmsdRSS+nJJ59MxrfkkksmscqVQPzwww868cQTddVVV+m9995L3O6ZZppJSy+9dCLYMkfVdcn+54wzztAf/vAHPfHEE4mLvNJKKyUcBg4c2OZ4ip4P75QxtqNpDs8995ymnXbapB666Pgq1QA/9dRTyTkxB59jj9MlIgcddFDihGct4//aa6/p8ssvT5xVO+mzzTab7LR7nyKtkgC+/fbbE1feuXf++ee3K4CvuOIKnXnmmUkem+OgQYO0zz77aNNNN20Zgs+Fz1dpc76ZIw0CEOieBBDA3fO8MWoI1JVALQLYX/qXXnpp4npmD3jdeOONevjhh3Xeeedp1113bRnbFltskQi+W2+9VWuttVby9+233z4Rq/6pev3112/ZtpwAttDeZZdd1KdPn+ShMoukkSNH6u67706ElcfgZtFkEbXsssuqX79++uSTTxJh9frrr+u6667ThhtuOJYAK/IQXCbWyjnAWYd/+9vftMMOO+jQQw/VMcccU1EA77TTTsmNg5lkbrLHcNtttyWiceqpp072teByrfHnn3+u3/3ud1p88cWTkguLuemmm07PPvtsm/rWWs5HVjZgQWee888/v7766ivtv//+Kjq+cgLY58NjnWqqqZLz75uUO++8U3fddZdWW2013XHHHS2lIBnTJZZYIhHkG2ywQfKZbwLefPPNRPD7s2qtkgA+9dRTk+M57LDDdPTRR1cUwK4TtmBfYIEFWkS3BfnLL7+cnEefTzc7++7TOXDZZZe1DMs3Ps5HGgQg0D0JIIC753lj1BCoK4GiAviWW25JXF4Lgn333bfNGOy6WQR/8MEHmmKKKZLPvv76ay2yyCL69NNPk5pMx9l666211157Jc5bvpUK4A8//DBxeO2S2tm1+Ms31+Nm9bXlfsa3C2kX2G6wRU3W6ukAu0+7qD5GC7nrr7++ogB2ParFrEVhey1zHPM/4Xt7C/mNN944EdsW0m61no/swTE75iuvvHKbYRQdX6kAdr3zHHPMof/+978J57xDnd3sWDhuueWWSbyM/+qrry67tdk5HDFiRHK+fbPimupqzcey3HLLJTdSbv514B//+Ecifr/77rvk1wXXCLuV5tYbb7yheeaZRwsuuKAeffRRTTLJJMl2ziOL71dffTUR49kqIdQAVzsbfA6B7kcAAdz9zhkjhkDdCRQVwBYndvYsDvI/a3tAdnktzu655x6tssoqLWN84YUXElEx77zzJo6shYcdz9L9S0XK6aefnojsWn9qtojxA3X+Sds/qbtG1+IoE+X1FsBmMeeccyYlCvfee29FAWy3cPTo0Ynos+tYqVl02f21i136oNncc8+d/P2zzz5LRF2t58P7uFzFNyOlrej4SgXw8OHDNXjw4MT59S8A+fb+++9r1llnTW6abrrppjYCuJwIdwmCj/mZZ56pmuOlq0BkO/hcnHXWWclqEFkrzS3fXLg85uqrr9Ymm2zSJpZ/3fByfM4/13i7IYCrng42gEC3I4AA7nanjAFDoP4EigpgO2r+Ob69ZgGx1VZbtdnktNNO03777adJJ51UL774Ykvtbn6jUpGy++67J4LKAro9weg+vCatxa7FucVjafNP/l66zK3eArioA+xSB3PxagV2SV376xuFjTbaSBNPPHHLkC2Af/WrXyUOZmmzkLTra0fdtbu1ng8zdrxrr712rL6L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plqk2kG1wLQY9v/7p/jMAd5kk1S4ujlBLDa//lp67z1p2mnTv9sRvvBC6X//S///oouknXeWXnhB+vWvWw968cWlWWeVrr22VQDb8bXz269f63alD8G9/ro0zzzSMcdIhxxSHaKLQzzWE0+Uzj5b+uij9vcZNWqU/E/WRo4cqcGDB2vEiBHqlx9Y9dCd2oISiE7hK7szwqe+TLsrz+467vqevbF7QwAjgBHACOBGX2fq3X+nBLDF4UwzpQ8Y3HBDOrTHH09dW4vXbbdtFcAWyX5ALmtLLZWWFOQfIrDzu8suqSvrkobNNpNee016+um2h20n9qqrpHfeaRXALnfwag/5ViqA//xnabfdUnFut7hc+/77tMTiiiuk99+XfvqpdatsXJVOwtChQzVs2LCxPkYAdyxtKYHoGLfusFd3FZLdddyNzgkEMAIYAYwAbvR1pt79d0oA3323tPrqqdjNan49QJcm2Gm9995WAeySiA03bB1+Vrd7++2tf7v4Ymm77aRPPpGmmy4tUbjvvvKHnH9a1n15lQeXMrQngO38upQiL2pLe99779TRdtnDIouk5RS33CIdfXTruCqdBBzg+qYnAri+PJupt+4qJLvruBt97hHACGAEMAK40deZevffKQHsml/X5JZrdnc//FCyo+qH4DoigF024Tpel0WUa9navuXEtLfviANsR9txTzutNaJNXQvnTJgXPQnUABclVX47BHDn+DXz3t1VSHbXcTc6FxDACGAEMAK40deZevffYQHs9fdmmCFducGuab5ZKPphNotIO8MdFcB2YvfbLy2DsDCt1IoK4KwG2CUOfgCvXPOqEK47PuGE9FOXeXjlCQtxBHC906/4l0a08IiO37XkGx+tu/LsruNu9BlFABe/luW3ZB3gtus6mw3rANd3tkYZcfU9isb01mEB7AfaXKP7j3+kKy2UtsGD00XR7fx2VAD/8ENaT+znyvyA3FxzSV4WzW+c8woRFrJuRQWwt91997TEwcJ6xRXTBb5dOpGtMmHh7rILi/c+faRzzpFefTWtN0YANyYJK/WKA9y1vLsyWncVkt113I0+twhgBLAJsAwaq0A0+lpTz/47LIDXXju9U/MqD9nFLz8wC8c990zd27nn7lgJhPuz+LU49UN2XivYtcELLZQKWa85XKsA9jrAp5ySimCP3StQLL98uvSaV0/w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dx8r8sknn6yzzz5bH3/8cfK2m5NOOkkrrLBCm+2++uorHXDAAbr++uv1ww8/6Le//a3OOusszTrrrG22awa2X3/9teaZZx59+OGH8uu0F1100ZYxXnLJJTruuOP07rvvao455tCRRx6pjTbaqM0x/PTTTzriiCN08cUX68svv9Tiiy+uM844QwsssECb7cxr77331l133ZVw/93vfqfTTz9d00wzTZvt/KbBfffdV88995ymnXZa7bTTTvrjH//Y5lx1Ih0q7nrhhRfqzDPP1GuvvZascrLEEkvo1ltv7ZEsbr755uS8ey54ni+99NLJ/88999xt+I2L+fHmm2/Kc/zJJ5/Uyy+/nMwN/7u0NfOxFxlbLXOoGpNsNQvPbc+fCSaYQIsssoiOPfZYLbzwwk1xvagnk2o8StnedNNNWn/99TXffPONlUv1/q6o5/dYLTnCttUJIICrM2qqLb744gvNP//8iXCzCPnvf/+bCMPVVltNl19+eVONtdJgLGQ8/vXWW08zzDCDHnjggeTLfJ999knEq9sTTzyh5ZZbTltvvbW23HJLPfbYY4nYO//887Xjjju2dO0vxkMPPbTlwn7BBRfIYsGizWI4a2uttVYi4E455ZRETFkg+kvixRdfbLlxaBa2Bx10kPzl8J///KeNALZ4t9g9+OCDtcoqqyTHaRF/9913J/+ftT333FOXXnppcqwDBgzQiSeeqH/+85/Ja7lnnHHGZDO/HtPC+scff0zYWzQfeOCBmnnmmfXwww+rV69eyXZvv/22FlxwweSGwmLZAszbOeeOPvrohuXb0KFDddpppyU3QBbwvlHycfr8u/UkFvfdd19yfj0PttpqKzlPzcf5+69//atlCcRxlcktt9wi57TzwDeov/zyy1iipZmPvejYaplM1Zj4BmHllVfW9ttvn1xHPb99E2zT5PHHH28jgiOuF/VmUo1Hnu13332nX//61/K/p5tuurFyqZ7fFfX+HqslR9i2OgEEcHVGTbXFCSecoD/96U967733ksnrduWVV2qLLbbQK6+8onnnnbepxltuMH4veZ8+fdp8ZEF13nnnJV/uE000kVZfffVE9Dz11FMt2+288866/fbb5cXZ7VjaybWA9t8t8tx+/vnnRPja7bz66quTv7kPi+477rhDa6yxRvK3999/P3GeLSB33XXX5G/NwPbf//53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QHUCCODqjNgCAhCAAAQgAAEIQGAcIoAAHodOJocCAQhUJuA3T/ntT36T4pxzztmyod+w5jcM+q2Dfrta1r7++mtNPfXUOvLII5PXjjeiPfPMM1psscWUfwNipTh+c59fDX377bfr448/1jTTTJO8Ettv/Ztjjjna7Pb5559rhx12kN8o6Fcn33TTTVp33XWTt+n5nw8//FBrr722br755roc1sUXX5y8snrzzTevS390AgEIQKDRBBDAjSZM/xCAQFMQeOuttxKheNFFFyVCOGtbbrllIhAtRC0Ys3bfffclAvP+++9PXp3diFZUAL/22mvJK8J79+6tww47TPPOO2/yOtuTTjpJI0aM0D333KMllliiZYiHHHKIzjvvPF166aWafvrpk1dI+1Xh3u/ggw9OxO90002nueaaqy6H5bH5Fc0W5zQIQAAC3YEAArg7nCXGCAHzWRL5AAAH2UlEQVQI1IVA3759tdZaa+mCCy5o6W/gwIFaY401EmH85ZdfaoIJJkg+GzZsWOK42kGdbLLJOhz/u+++0ySTTFJ2/6IC2OL87bff1osvvqiZZ565pa9Ro0Zp0UUX1Q8//JA42xNNNFHymd1eu8APP/xwy7Z2e9dbbz35RmC22Wbr8PGU2xEBXFecdAYBCHQBAQRwF0AmBAQg0BwENthgA7366qt65ZVXkgF99NFHiaD897//rQUWWECPPPKIBg8enHy2yiqrJOL36aefbhm8P7e7+uyzz2rSSSdNhPPJJ5+sGWaYIdnGrqwFtcX0Y489phtvvFEW3S+//HLyuQX12WefLZdXuP8dd9xRa665ZrslEI653HLLJYLc5Q6lLSvtuPzyy7XFFluoV69eY22zzTbbyNvlm8fo7V36ce2117aUVVhQu6+pppoq2dwMvI1dcovq+eefX8cdd1wyfjeL34ceeqhN3y4bGTp0aHOcdEYBAQhAoAwBBDBpAQEI9BgCrn/df//99emnnyY1tNddd5322WefpCZ2ySWX1MYbb6x9991Xv/zyS1L/6zpa7+Nm0bvUUktp2WWX1d57752IQZcTuB9/NvHEE7cI4BlnnDEpM9hwww31888/a/XVV0+E71577aUDDjhAK620kv7+97/rmmuuSWK3VwN81FFHJcL3hRdeSER6abNr7bFaTNvZfvLJJ5MY3377rVzf7NanT59E5FrIZqJ89tlnT8okXEZxwgknaL755ku4eFyO6dKJH3/8UUsvvXRSPmFB65sFi+Orr75azz33nAYNGpTcTLiMxDcEvhlw69evX/IPDQIQgECzEkAAN+uZYVwQgEDdCdjNXXzxxXXbbbclpRAWux988EEihC2M33vvPV1//fWJ2FxwwQWT/7Zr7Lb++utr+PDhSQmBH/hye+KJJxJRnNUVZw6wneE77rijZfwWwbPMMotWXHHFpC43a35o7KqrrmpXAO+66646//zzEyc2c2VLwVgAW8DfddddyUc+NrvM+ZpmH8tGG22kd955RwMGDGjZzmUTN9xwQ1nWPq6dd9454fHrX/+6ZRsznHXWWRNR7UYJRN1TlQ4hAIEGE0AANxgw3UMAAs1D4KeffkrcUjuxxx9/fFLuYBFqF9gicM8995RXW8hWhvB/2811s4u66aab6qyzzmpzQBaTFrYXXnhhiwNst9crS2TNwtrb2X11HW7W/P8W2O05wEUFsIX4nXfeWZMAtrNsB/iggw5KSjEWWWQRjTfeeC3j22yzzeQH8PJlIP7Q+1m4W0wjgJsnvxkJBCBQnAACuDgrtoQABMYBAkOGDNHo0aOTlRMshh999NFECFvszjTTTHrzzTcTgffUU08l/501r8DgOlyvwpBvXn3Bdb6ukc0cYDujdluz5rIEO7SO5ZKCrLlOeJlllulUCYQfhLMznJVAuO+iDrAfnnM9r+uDPXaLfAt3H79rib0KhlfDKNfGH3/8hCMCeByYFBwCBHogAQRwDzzpHDIEejKBww8/XKeccopuueWWZLWE/MoPfoAte9jMP+t7fdusuSbWDvCZZ57ZBl85B9glFa7/zVpnHODsITjX5Xrspe2yyy7T1ltvndTm+qG2WgRwvi+L/b/97W+JIHaZxlZbbaVNNtkkeUDQ7na55gfmEMA9eTZx7BDovgQQwN333DFyCECgAwRcJ+saXf/k/9VXX7VZwcAC0o6q17P1A2V2VbPmGmAvW+Ya4GypNLvEdoBLa4BLBbBrgPv37588/FZrDbDjexk0lxu89NJLiducNdf5umzh+++/b7MMWlEHuBy+aaedVrvssouOPfbYhMF+++2XlEHYHa/UvCKEHxys5BZ34DSxCwQgAIGGEkAANxQvnUMAAs1GwI6vV24YM2ZMUvtqxzNr55xzTlIf7M+8uoFfHJG1bBUIL0mWrQLhJdFcRlG6CkSpAHYfdo69n1docGmBSzCKrALhfbMXYfjhO6/k4HHZVT7xxBOTf7svl1hkragAtgNuAb3QQgslax374UCvenHvvfcmYt0lEi7Z8E2Bx+0XZ/hhvOeffz5ZISJj5+NyGYXdaAt0i+X2BHOz5QTjgQAEeh4BBHDPO+ccMQR6PAEvJ2Y39dZbb02WK8uahd3CCy8su6CffPLJWGvq+sUS5dYBzh6Uy2qAywlgi2qXMVhk27m1wPQKCxarRV+F7P29uoTrlfOvQs6/2tnHUlQA+wE41yu/8cYbST2v3xhnoeuH37Jm8esl0PyQoOP6DXIWzLvvvnviort5KTcfy+OPP54IZNYB7vFTDAAQaHoCCOCmP0UMEAIQgAAEIAABCECgngQQwPWkSV8QgAAEIAABCEAAAk1PAAHc9KeIAUIAAhCAAAQgAAEI1JMAArieNOkLAhCAAAQgAAEIQKDpCSCAm/4UMUAIQAACEIAABCAAgXoSQADXkyZ9QQACEIAABCAAAQg0PQEEcNOfIgYIAQhAAAIQgAAEIFBPAgjgetKkLwhAAAIQgAAEIACBpieAAG76U8QAIQABCEAAAhCAAATqSQABXE+a9AUBCEAAAhCAAAQg0PQEEMBNf4oYIAQgAAEIQAACEIBAPQkggOtJk74gAAEIQAACEIAABJqeAAK46U8RA4QABCAAAQhAAAIQqCcBBHA9adIXBCAAAQhAAAIQgEDTE/g/o8RJU04HR1QAAAAASUVORK5CYII=" width="639.9999861283738">
