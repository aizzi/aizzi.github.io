---
title: "Notes on learning NLTK"
description: "In this tutorial I collected a bunch of notes I used during the study of the book *Natural Language Processing with Python*"
last_update: "2018-10-01"
---
# Notes on Learning NLTK
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

This is a collection of notes I took while studying the [Natural Language Processing with Python](http://www.nltk.org/book/) book.

1. [Glossary](#glossary)
2. [Language Processing and Python](#language-processing-and-python)
3. [Accessing Text Corpora and Lexical Resources](#accessing-text-corpora-and-lexical-resources)
4. [Further Readings and resources](#further-readings-and-resources)

## Glossary

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

## Language Processing and Python

### Simple text statistics

1. Get a frequency distribution using `FreqDist(text)`
2. Get the x most common types by using `fdist1.most_common(x)`
3. Get the infrequent words by using `fdist1.hapaxes()`
4. Search for long words used more often in order to characterize a text

### Functions define for Frequency distribution

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

### Some Word Comparison Operators

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

## Accessing Text Corpora and Lexical resources


## Further Readings and resources
1. Indurkhya, Nitin and Fred Damerau (eds, 2010) *Handbook of Natural Language Processing (Second Edition)* Chapman & Hall/CRC. 2010.
2. Jurafsky, Daniel and James Martin (2008) *Speech and Language Processing (Second Edition)*
3. Mitkov, Ruslan (ed, 2003) *The Oxford Handbook of Computational Linguistics*. Oxford University Press. (second edition expected in 2010)
4. [he Association for Computational Linguistics](http://www.aclweb.org/)
