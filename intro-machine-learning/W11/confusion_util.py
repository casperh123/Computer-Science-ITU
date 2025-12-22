import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

def make_dataset(weights, seed, n_samples=2000):
    X, y = make_classification(
        n_samples=n_samples, n_features=10,
        n_informative=6, n_redundant=0,
        weights=weights, random_state=seed
    )
    return train_test_split(X, y, test_size=0.3, random_state=seed)



def compute_metrics(cm):
    tn, fp, fn, tp = cm.ravel()

    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0
    specificity = tn / (tn + fp) if (tn + fp) else 0
    mcc_den = np.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
    mcc = ((tp * tn) - (fp * fn)) / mcc_den if mcc_den != 0 else 0

    print(f"Accuracy:     {accuracy:.3f}")
    print(f"Precision:    {precision:.3f}")
    print(f"Recall:       {recall:.3f}")
    print(f"F1-Score:     {f1:.3f}")
    print(f"Specificity:  {specificity:.3f}")
    print(f"MCC:          {mcc:.3f}")
    print("-" * 40)


def plot_confusion_matrix_sns(cm, title, x_label, y_label):
    plt.figure(figsize=(5,4))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=[x_label, y_label],
        yticklabels=[x_label, y_label]
    )
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show()



def make_model1():
    X_train, X_test, y_train, y_test = make_dataset(weights=[0.5, 0.5], seed=1)
    clf = SVC(kernel="linear")
    clf.fit(X_train, y_train)
    cm = confusion_matrix(y_test, clf.predict(X_test))

    print("=== Diagnosis Model Metrics ===")
    compute_metrics(cm)
    plot_confusion_matrix_sns(cm, "Diagnosis", "Sick", "Healthy")



def make_model2():
    X_train, X_test, y_train, y_test = make_dataset(weights=[0.99, 0.01], seed=2, n_samples=10000)
    clf = SVC(kernel="rbf")
    clf.fit(X_train, y_train)
    cm = confusion_matrix(y_test, clf.predict(X_test))

    print("=== Fraud Detection Model Metrics ===")
    compute_metrics(cm)
    plot_confusion_matrix_sns(cm, "Fraud Detection", "Legit", "Fraud")



def make_model3():
    X_train, X_test, y_train, y_test = make_dataset(weights=[0.8, 0.2], seed=3)
    clf = SVC(kernel="rbf")
    clf.fit(X_train, y_train)
    cm = confusion_matrix(y_test, clf.predict(X_test))

    print("=== Spam Detection Model Metrics ===")
    compute_metrics(cm)
    plot_confusion_matrix_sns(cm, "Spam Detection", "Spam", "Legit")



def make_model4():
    X_train, X_test, y_train, y_test = make_dataset(weights=[0.5, 0.5], seed=4)
    clf = SVC(kernel="linear")
    clf.fit(X_train, y_train)
    cm = confusion_matrix(y_test, clf.predict(X_test))

    print("=== Churn Prediction Model Metrics ===")
    compute_metrics(cm)
    plot_confusion_matrix_sns(cm, "Customer Churn Prediction", "Churn", "Loyal")

