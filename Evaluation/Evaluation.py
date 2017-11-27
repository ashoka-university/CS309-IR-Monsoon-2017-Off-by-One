import csv
import math

filepath = "svm.csv"
classifier_scores = []
actual_scores = []
difference = []
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        classifier_scores.append(int(row['svm']))
        actual_scores.append(int(row['actual']))
        difference.append(int(row['difference']))

size = len(actual_scores)
probabilities = []
precisions = []
recalls = []
f_measures = []
mcc_scores = []
kappa_scores = []

for score in range(2, 13):
    tp = 0
    fn = 0
    fp = 0
    tn = 0
    n = 0

    for i in range(size):
        if (actual_scores[i] == score) and (difference[i] == 0):
            tp += 1
        if (actual_scores[i] == score) and (difference[i] != 0):
            fn += 1
        if (actual_scores[i]) != score and (classifier_scores[i] == score):
            fp += 1
        if (actual_scores[i] != score) and (classifier_scores[i] != score):
            fn += 1
        if actual_scores[i] == score:
            n += 1

    probability = n / (size)
    precision = 0
    if tp + fp != 0:
        precision = tp / (tp + fp)
    recall = 0
    if tp + fn != 0:
        recall = tp / (tp + fn)
    f_measure = 0
    if recall + precision != 0:
        f_measure = (2 * recall * precision) / (recall + precision)

    mcc_num = (tp * tn) + (fp * fn)
    mcc_den = math.sqrt((tp + fn) * (tp + fp) * (tn + fn) * (tn + fp))

    mcc = 0
    if mcc_den != 0:
        mcc = mcc_num / mcc_den

    po = (tp + tn) / (tp + tn + fp + fn)
    p1 = ((tp + fn) / (tp + tn + fp + fn)) * ((tp + fp) / (tp + tn + fp + fn))
    p2 = ((tn + fn) / (tp + tn + fp + fn)) * ((tn + fp) / (tp + tn + fp + fn))
    pe = p1 + p2
    kappa = (po - pe) / (1 - pe)

    probabilities.append(probability)
    precisions.append(precision)
    recalls.append(recall)
    f_measures.append(f_measure)
    mcc_scores.append(mcc)
    kappa_scores.append(kappa)

avg_precision = 0
avg_recall = 0
avg_f_measure = 0
avg_mcc = 0
avg_kappa = 0

for i in range(11):
    avg_precision += probabilities[i] * precisions[i]
    avg_recall += probabilities[i] * recalls[i]
    avg_f_measure += probabilities[i] * f_measures[i]
    avg_mcc += probabilities[i] * mcc_scores[i]
    avg_kappa += probabilities[i] * kappa_scores[i]

print(avg_precision)
print(avg_recall)
print(avg_f_measure)
print(avg_mcc)
print(avg_kappa)
