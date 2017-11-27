import docx
from AutoGrade_Train import get_attributes, write_to_csv
import os
import sys
from weka.classifiers import Classifier
from weka.core.converters import Loader
import weka.core.jvm as jvm
from weka.filters import Filter


def get_topic_essay(filename):
    document = docx.Document(filename)
    paragraphs = []
    essay = ""
    for paragraph in document.paragraphs:
        if paragraph.text:
            paragraphs.append(paragraph.text)
    if len(paragraphs) < 2:
        print(
            "Error: Only one paragraph is in the document. Document must contain at least 2 paragraphs where the first one is the topic.")
        jvm.stop()
        exit(1)
    topic = paragraphs[0]
    del paragraphs[0]
    for paragraph in paragraphs:
        essay += paragraph
    return topic, essay


def discretize_data(input_data):
    discretize = Filter(classname="weka.filters.unsupervised.attribute.Discretize", options=["-B", "10"])
    discretize.inputformat(input_data)
    filtered_data = discretize.filter(input_data)
    return filtered_data


def get_essay_data(topic, essay, word_limit):
    attributes_with_values = get_attributes(topic, essay, word_limit)
    print()
    for attr_with_val in attributes_with_values:
        print(str(attr_with_val[0]) + " : " + str(attr_with_val[1]))
    attributes_with_values.append(["Score", 0])
    with open("temp.csv", 'wb') as csvfile:
        print()
    csvfile.close()
    write_to_csv(attributes_with_values, "temp.csv")
    global loader
    essay_data = loader.load_file("temp.csv")
    essay_data.class_is_last()
    return essay_data


def get_essay_score(essay_data, classifier):
    score = 0
    for index, inst in enumerate(essay_data):
        score = classifier.classify_instance(inst)
        score = int(score)
    return score


def get_docs(dir_path):
    docs = []
    if os.path.isdir(dir_path):
        docs = os.listdir(dir_path)
        for i in range(len(docs)):
            docs[i] = dir_path + docs[i]
    elif os.path.isfile(dir_path):
        docs.append(dir_path)
    docs = [d for d in docs if d.endswith(".docx") and "~$" not in d]
    print()
    print("---------------------------------------------------------")
    print("Grading the following documents:")
    print(docs)
    return docs


jvm.start()
loader = Loader(classname="weka.core.converters.CSVLoader")
data = loader.load_file("data_train.csv")
data.class_is_last()

knn_classifier = Classifier(classname="weka.classifiers.lazy.IBk", options=["-K", "3"])
lin_classifier = Classifier(classname="weka.classifiers.functions.LinearRegression", options=["-S", "0"])
svm_classifier = Classifier(classname="weka.classifiers.functions.SMOreg", options=["-C", "1.0"])

knn_classifier.build_classifier(data)
lin_classifier.build_classifier(data)
svm_classifier.build_classifier(data)

classifiers = [knn_classifier, lin_classifier, svm_classifier]

print("###################### Classifiers ######################")
for classifier in classifiers:
    print("~~~~~~~~~~~~~~~~~~~")
    print(classifier)

classifier_names = ["KNN Classifier", "LinearRegression Classifier", "SVM Classifier"]

documents = get_docs(sys.argv[1])
essay_word_limit = int(sys.argv[2])

for doc in documents:
    print("-------------------------- " + "Document: " + doc + " -------------------------------")
    essay_topic, essay_content = get_topic_essay(doc)
    essay_data = get_essay_data(essay_topic, essay_content, essay_word_limit)
    predicted_scores = []
    for classifier in classifiers:
        essay_score = get_essay_score(essay_data, classifier)
        predicted_scores.append(essay_score)
    print("=========== Predicted Scores ===========")
    for i in range(len(classifier_names)):
        print(classifier_names[i] + " : " + str(predicted_scores[i]))

jvm.stop()
