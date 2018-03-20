# AutoGrade

Automated Essay Scoring (AES) is an area which falls at the intersection of computing and linguistics.
AES systems conduct a linguistic analysis of a given essay or prose and then estimates the writing skill or the essay quality in the form a numeric score or a letter grade. 
AES systems are useful for the school, university and testing company community for efficiently and effectively scaling the task of grading a large number of essays.

## Getting Started

The following instructions will get a copy of the project up and running on your local machine for development and testing purposes.
The project was developed on Python 3.

### Prerequisites

Following are the packages you will need to install.

```
language_check (https://pypi.python.org/pypi/language-check)
enchant (https://pythonhosted.org/pyenchant/)
spacy (https://pypi.python.org/pypi/spacy)
nltk (https://pypi.python.org/pypi/nltk)
textstat (https://github.com/shivam5992/textstat)

Run the following python commands only once on your system to download all the required nltk packages:

  import nltk
  
  nltk.download('wordnet')  
  nltk.download('punkt')
  nltk.download('averaged_perceptron_tagger')
  nltk.download('stopwords')

```

### How to use

Each attribute calculated for an essay is developed as a tool. Code for a particular tool can be found in the Tools folder. Each tool is imported in a python file and used accordingly.

There are three main python files: AutoGrade.py, AutoGrade_Test.py and AutoGrade_Train.py




