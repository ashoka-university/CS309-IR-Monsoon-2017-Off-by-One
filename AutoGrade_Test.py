from weka.classifiers import Classifier
from weka.core.converters import Loader
import weka.core.jvm as jvm
from AutoGrade_Train import write_to_csv
import csv

train_csv = "Data/data_train_set8.csv"
test_csv = "Data/data_test_set8.csv"
result_csv = "Data/test_result_set8_k5s2c10.csv"

jvm.start()
loader = Loader(classname="weka.core.converters.CSVLoader")

data_train = loader.load_file(train_csv)
data_train.class_is_last()

knn_classifier = Classifier(classname="weka.classifiers.lazy.IBk", options=["-K", "5"])
lin_classifier = Classifier(classname="weka.classifiers.functions.LinearRegression", options=["-S", "2"])
svm_classifier = Classifier(classname="weka.classifiers.functions.SMOreg", options=["-C", "10.0"])

knn_classifier.build_classifier(data_train)
lin_classifier.build_classifier(data_train)
svm_classifier.build_classifier(data_train)

classifiers = [knn_classifier, lin_classifier, svm_classifier]

print("###################### Classifiers ######################")
for classifier in classifiers:
    print("~~~~~~~~~~~~~~~~~~~")
    print(classifier)

data_test = loader.load_file(test_csv)
data_test.class_is_last()

actual_scores = []
with open(test_csv) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        actual_scores.append(row['Score'])

with open(result_csv, 'wb') as csvfile:
    print()
csvfile.close()

print(data_test)

for index, inst in enumerate(data_test):
    print(index)
    knn_score = int(knn_classifier.classify_instance(inst))
    lin_score = int(lin_classifier.classify_instance(inst))
    svm_score = int(svm_classifier.classify_instance(inst))
    classifiers_scores = [["KNN", knn_score], ["Linear Regression", lin_score], ["SVM", svm_score],
                          ["Actual Score", actual_scores[index]]]
    write_to_csv(classifiers_scores, result_csv)

jvm.stop()
