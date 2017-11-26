from weka.classifiers import Classifier
from weka.core.converters import Loader
import weka.core.jvm as jvm
from AutoGrade_Train import write_to_csv
import csv

jvm.start()
loader = Loader(classname="weka.core.converters.CSVLoader")
data_train = loader.load_file("data_train.csv")
data_train.class_is_last()

knn_classifier = Classifier(classname="weka.classifiers.lazy.IBk", options=["-K", "3"])
lin_classifier = Classifier(classname="weka.classifiers.functions.LinearRegression", options=["-S", "0"])
svm_classifier = Classifier(classname="weka.classifiers.functions.SMOreg", options=["-C", "1.0"])

knn_classifier.build_classifier(data_train)
lin_classifier.build_classifier(data_train)
svm_classifier.build_classifier(data_train)

classifiers = [knn_classifier, lin_classifier, svm_classifier]

print("###################### Classifiers ######################")
for classifier in classifiers:
    print("~~~~~~~~~~~~~~~~~~~")
    print(classifier)

data_test = loader.load_file("data_test.csv")
data_test.class_is_last()

actual_scores = []
with open('data_test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        actual_scores.append(row['Score'])

result_csv = "test_result.csv"
with open(result_csv, 'wb') as csvfile:
    print()
csvfile.close()

for index, inst in enumerate(data_test):
    knn_score = int(knn_classifier.classify_instance(inst))
    lin_score = int(lin_classifier.classify_instance(inst))
    svm_score = int(svm_classifier.classify_instance(inst))
    classifiers_scores = [["KNN", knn_score], ["Linear Regression", lin_score], ["SVM", svm_score],
                          ["Actual Score", actual_scores[index]]]
    write_to_csv(classifiers_scores, result_csv)

jvm.stop()
