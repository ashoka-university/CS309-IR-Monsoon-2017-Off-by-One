# AutoGrade

Automated Essay Scoring (AES) is an area which falls at the intersection of computing and linguistics.
AES systems conduct a linguistic analysis of a given essay or prose and then estimates the writing skill or the essay quality in the form a numeric score or a letter grade. 
AES systems are useful for the school, university and testing company community for efficiently and effectively scaling the task of grading a large number of essays.

## Getting Started

The following instructions will get a copy of the project up and running on your local machine for development and testing purposes.
The project was developed on Python 3.

### Prerequisites

Following are the packages you will need to install.

* [language_check](https://pypi.python.org/pypi/language-check)
* [enchant](https://pythonhosted.org/pyenchant/)
* [spacy](https://pypi.python.org/pypi/spacy)
* [nltk](https://pypi.python.org/pypi/nltk)
* [textstat](https://github.com/shivam5992/textstat)
* [python-weka-wrapper3](https://github.com/fracpete/python-weka-wrapper3)

Run the following python commands only once on your system to download all the required nltk packages:

```
  import nltk
  
  nltk.download('wordnet')  
  nltk.download('punkt')
  nltk.download('averaged_perceptron_tagger')
  nltk.download('stopwords')
```

### Data

We used publically available Hewlett Foundation’s Automated Student Assessment Prize (ASAP) dataset for experimental evaluation.
Out of 8 available essay sets, we used 3 essay sets (Set 1, Set 7 and Set 8). We selected the essay sets which have highest grade range for experimental evaluation.

All the data that we used, processed, obtained is present in the 'Data' folder of the project.

(1) Essays used for training the models:
```
training_set_rel3_set1.xlsx
training_set_rel3_set7.xlsx
training_set_rel3_set8.xlsx
```
(2) Data obtained from processing the training sets above is stored in:
```
data_train_set1.csv
data_train_set7.csv
data_train_set8.csv
```
(3) Essays used for testing the models:
```
valid_set_set1.xlsx
valid_set_set7.xlsx
valid_set_set8.xlsx
```
(4) Data obtained from processing the test sets above is stored in:
```
data_test_set1.csv
data_test_set7.csv
data_test_set8.csv
```
(5) For k-cross validation, we combined the training data and testing data. The complete data for the set is stored in:
```
full_set1.csv
full_set7.csv
full_set8.csv
```

## How does it work

Each attribute calculated for an essay is developed as a tool. Code for a particular tool can be found in the Tools folder. Each tool is imported in a python file and used accordingly.

Main python files: AutoGrade.py, AutoGrade_Test.py and AutoGrade_Train.py, Evaluation.py (in Evaluation Folder)

### AutoGrade_Train.py

This python program is used to process the essays in the (1) and (3).
Change the 'file_path', 'ws', 'essay_set', 'topic', 'word_limit', 'write_to_file' variables in the train_data() function according to your dataset (file).

Topic and word limit of the essays can be found in the description of the data that is available on Kaggle.

For example, if you are processing the file that contains test essays of set 8, the variables must be set to:
```
file_path = "Data/valid_set_set8.xlsx"
ws = wb['valid_set']

if essay_set == 8:
  topic = "If you want a place in the sun, you will have to expect some blisters."

word_limit = 800

write_to_file = "data_test_set8.csv"
```
This program has to be run on all the .xlsx files (that contain raw essays) present in the data folder to obtain the processed data that is required to train the test the models.

### AutoGrade_Test.py

This program builds models using the weka packaged, takes training data and test data, and predicts score for all the essays in the test data. The predicted scores are then written to a csv. 

Change the 'train_csv', 'test_csv' and 'result_csv' according to the set you are working on. 
For example, if you want to predict the scores of all essays of set1, the variables must be set to:
```
train_csv = "Data/data_train_set1.csv"
test_csv = "Data/data_test_set1.csv"
result_csv = "Data/test_result_set1.csv"
```
The 'result_csv' file will contain the scores predicted by all 3 models: kNN, Linear Regression and SVM and also the actual score of the essay.
It can then be used for evaluation.

### AutoGrade.py

AutoGrade.py is written keeping in mind a non-technical user. AutoGrade.py is useful for users who want to grade essays present in the word documents in a folder. 

The first paragraph of the document has to be the topic of the essay.

AutoGrade.py takes 2 command line aruments:
Argument 1: path of the document or folder that contains the documents.
Argument 2: word limit of the essay(s).

Eg command: python3 AutoGrade.py essays/AshokaUniversity/PoliticalScience 1000

The above command predicts the scores of all the essays present in the 'PoliticalScience' folder.

### Evaluation.py

The 'result_csv' files that are obtained from AutoGrade_Test.py program can be used to evaluate our models. 
After running AutoGrade_Test.py on all the sets, we have gotten:
* 'test_result_set1.csv'
* 'test_result_set2.csv'
* 'test_result_set3.csv'

Each of the above csv files contains scores predicted by KNN, Linear Regression, SVM and the Acutal Score of the essay.
Using a software like MS Excel (or any other csv editor), create separate csv files for each classifier - knn.csv, lin_reg.csv, svm.csv. These csv files must contain the score predicted by the classifier, actual score and their difference.

Input to the program: csv file - either knn.csv, line_reg.csv or svm.csv.
Change the variables such as 'filepath' and row names in line 11,12,13 of the program according to the csv file. 

Evaluation.py will calculate all the necessary evaluation metrics such as precision, recall, f_measure etc. 







