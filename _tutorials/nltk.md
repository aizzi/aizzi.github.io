---
title: "Notes on learning NLTK"
description: "In this tutorial I collected a bunch of notes I used during the study of the book *Natural Language Processing with Python*"
last_update: "2018-10-01"
published: false
---
# Notes on Learning NLTK
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

This is a collection of notes I took while studying the [Natural Language Processing with Python](http://www.nltk.org/book/) book.

1. [Glossary](#glossary)
2. [Language Processing and Python](#language-processing-and-python)
3. [Accessing Text Corpora and Lexical Resources](#accessing-text-corpora-and-lexical-resources)
4. [Further Readings and resources](#further-readings-and-resources)

## 1 - Glossary

| Term | Description | Example |
| === | === | === |
| Concordance | Shows every occurence of a given word, together with some context | `text1.concordance("monstrous")` |
| Similarity | Shows us what other words appear in a similar range of context of a given word | `text1.similar("monstrous")` |
| Common Context | Examine just the contexts that are shared by two or more words | text1.common_contexts(["monstrous", "very"]) |
| token | A sequence of characters that we want to treat as a group | len(text3) |
| type | The form or spelling of the word independently of its specific occurence in the text | set(text3) |
| lexical diversity | Shows the number of unique words used in a text with regards to the length of the text itself. The higher it is, more words are used. | len(set(text)) / len(text) |
| frequency distribution | the frequency of each vocabulary item in the text | FreqDist(text1) |
| hapaxes | words that occurs only once in the text | fdist1.hapaxes() |
| collocation | a sequence of words that occur together unusually often. They are bigrams that occurs more often than we would expect based on the frequency of the individual words | text.collocations() |
| bigrams | a list of word pairs | bigrams(['a',  'b', 'c']) |
| Word Sense Disambiguation | work out which sense of a word was intended in a given context |
| anaphora resolution | identifying what a pronoun or noun phrase refers to |
| semantic role labeling | identifying how a noun phrase relates to the verb (as agent, patient, instrument, and so on) |
| Conditional Frequency Distributions | A collection of frequency distributions, each of one for a different "condition" |
| Lexicon | A lexicon (or lexical resource), is a collection of words and/or phrases along with associated information such as part of speech and sense definitions. |

## 2 - Language Processing and Python

### 2.1 - Simple text statistics

1. Get a frequency distribution using `FreqDist(text)`
2. Get the x most common types by using `fdist1.most_common(x)`
3. Get the infrequent words by using `fdist1.hapaxes()`
4. Search for long words used more often in order to characterize a text

### 2.2 - Functions define for Frequency distribution

| Example | Description |
| === | === |
| fdist = FreqDist(samples) | create a frequency distribution containing the given samples |
| fdist[sample] += 1 | increment the count for this sample |
| fdist['token'] | count of the number of times a given sample occurred |
| fdist.N() | total number of samples |
| fdist.most_common(n) | the n most common samples and their frequencies |
| for sample in fdist | iterate over the samples |
| fdist.max() | sample with the greatest count |
| fdist.tabulate() | tabulate the frequency distribution |
| fdist.plot() | graphical plot of the frequency distribution |
| fdist.plot(cumulative=True) | cumulative plot of the frequency distribution |
| fdist1 \|= fdist2 | update fdist1 with counts from fdist2 |
| fdist1 < fdist2 | test if samples in fdist1 occur less frequently than in fdist2 |

### 2.3 - Some Word Comparison Operators

| Function | Meaning |
| === | === |
| s.startswith(t) | test if s starts with t |
| s.endswith(t) | test if s ends with t |
| t in s | test if t is a substring of s |
| s.islower() | test if s contains case characters and all are lowercase |
| s.isupper() | test if s contains cased characters and all are uppercase |
| s.isalpha() | test if s is non-empty and all characters in s are alphabetic |
| s.isalnum() | test if s is non-empty and all characters in s are alphanumerics |
| s.isdigit() | test if s is non-empty and all characters in s are digits |
| s.istitle() | test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals) |

## 3 - Accessing Text Corpora and Lexical resources

### Accessing Text Corpora
Corpora available in NTLK are described in the table below

| Corpus | Description | Example |
| === | === | === |
| gutenberg | Small selection of texts from [Project Gutenberg](http://www.gutenberg.org) | from nltk.corpus import gutenberg |
| Web and Chat Text | Content from a Firefox discussion forum, conversations overheard in New York, the movie script of *Pirates of the Carribean*, personal advertisements, and wine review | from nltk.corpus import webtext |
| NPS Chat | Instant messagin chat sessions, collected by the Naval Postgraduate School for research on automatic detection of Internet predators | from nltk.corpus import nps_chat |
| Brown Corpus | The first million-word electronic corpus of English, created in 1961 at Brown University (http://icame.uib.no/brown/bcm-los.html) | from nltk.corpus import brown |
| Routers | contains 10.788 news documents totaling 1.3 million words, classified into 90 topics and grouped into two sets (*training* and *test*) | from nltk.corpus import reuters |
| Inaugural Address Corpus | A collection of 55 texts, one for each presidential address | from nltk.corpus import inaugural |
| Annotated Text Corpora | Many text corpora containing linguist annotations | see http://nltk.org/data |

In the following table some functions than can be used with these corpora:

| Command | Description | Example |
| === | === | === |
| from nltk.corpus import gutenberg | Import the corpora as a `gutenberg` object | |
| gutenberg.fileids() | return a list of all the file identifiers in the corpus | |
| gutenberg.words(<file_id>) | return the corpus associated with the specific fileid | emma = gutenberg.words('austen-emma.txt') |
| gutenberg.raw(fileid) | return the "raw" text of the book, not split up into tokens. | gutenberg.raw('austen-emma.txt') |
| gutenbers.sents(fileid) | divides the text up into its sentences, where each sentence is a list of words | gutenberg.sents('austen-emma.txt') |

On these corpora we can of course use all the functions we explored in the chapter 1 (e.g. `concordance`, `similarity`, `common_context`, etc.).

### Conditional Frequency distributions
Commonly-used methods and idioms for defining, accessing and visualizing a conditional distribution of counters:

| Example | Description |
| === | === |
| cfdist = ConditionalFreqDist(pairs) | create a conditional frequency distribution from a list of pairs |
| cfdist.conditions() | the conditions |
| cfdist[condition] | the frequency distribution for this condition |
| cfdist[condition][sample] | frequency for the given sample for this condition |
| cfdist.tabulate() | tabulate the conditional frequency distribution |
| cfdist.tabulate(samples, conditions) | tabulation limited to the specified samples and conditions |
| cfdist.plot() | graphical plot of the conditional frequency distribution |
| cfdist.plot(samples, conditions) | graphical plot limited to the specified samples and conditions |
| cfdist1 < cfdist2 | test if samples in cfdist1 occur less frequently than in cfdist2 |

## 4 - Further Readings and resources
1. Indurkhya, Nitin and Fred Damerau (eds, 2010) *Handbook of Natural Language Processing (Second Edition)* Chapman & Hall/CRC. 2010.
2. Jurafsky, Daniel and James Martin (2008) *Speech and Language Processing (Second Edition)*
3. Mitkov, Ruslan (ed, 2003) *The Oxford Handbook of Computational Linguistics*. Oxford University Press. (second edition expected in 2010)
4. [The Association for Computational Linguistics](http://www.aclweb.org/)
5. Edward Finegan *Language: Its Structure and Use*
6. William O'Grady, John Archibald, Mark Aronoff, and Janie Rees-Miller. *Contemporary Linguistics: An Introduction*. St. Martin's Press, 5 edition, 2004.
