import numpy as np
import pandas as pd

def train(train_data) :
    # label column
    labels = train_data['label']
    # image size / pixel number
    pixel_number = len(train_data.columns) - 1
    # sample number
    data_number = len(train_data.index)
    # data_number = 50
    # number of different digit
    label_counts = labels.value_counts()

    # conditional probability of different pixels with certain digit
    point_counts = np.zeros((pixel_number, 10))
    for i in range(1, pixel_number + 1):
        # print(i)
        pixel_label_counts = np.zeros((1, 10))
        # count label
        for j in range(0, data_number):
            if train_data.iloc[j, i] > 0:
                pixel_label_counts[0, labels.iloc[j]] += 1

        # calculate probability
        for n in range(0, 10):
            point_counts[i-1, n] = (pixel_label_counts[0, n] + 1) / label_counts[n]

    np.savetxt('probability.txt', point_counts)
    return 0

def predict(test_data) :
    data_number = len(test_data.index)
    # data_number = 50
    pixel_number = len(test_data.columns)
    labels_predict = np.zeros((data_number, 2))

    # load probability data from file generated by train method
    point_counts = np.loadtxt('probability.txt')

    # calculate probability for every label every sample
    for i in range(0, data_number):
        # print(i)
        labels_probability = np.zeros((1, 10))
        for n in range(0, 10):
            probability = 1
            for j in range(0, pixel_number):
                if test_data.iloc[i, j] == 0:
                    probability *= 1 - point_counts[j, n]
                else:
                    probability *= point_counts[j, n]
            labels_probability[0, n] = probability
        # save result with max probability
        labels_predict[i, 0] = i+1
        labels_predict[i, 1] = np.argmax(labels_probability)

    data_frame = pd.DataFrame(labels_predict)
    data_frame.to_csv('predict_naive_bayes2.csv', index=False)
    return 0
