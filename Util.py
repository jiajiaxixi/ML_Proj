from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def preprocess(raw_data, feature_abstract_method):
    X_raw = raw_data.iloc[:, 1:]
    y_raw = raw_data['label']
    X_train, X_test, y_train, y_test = train_test_split(X_raw, y_raw, test_size=0.2)
    if (feature_abstract_method == 'LBP'):
        return LBP()
    elif (feature_abstract_method == 'PCA'):
        return PCA()
    elif(feature_abstract_method == 'skeleton'):
        return skeleton()
    return X_train, X_test, y_train, y_test

def score(y_true, y_predict):
    print(classification_report(y_true, y_predict))
    print("Detailed confusion matrix:")
    print(confusion_matrix(y_true, y_predict))
    print("Accuracy Score: \n")
    print(accuracy_score(y_true, y_predict))