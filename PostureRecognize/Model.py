import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.utils import parallel_backend
import os
import glob
import joblib
import logging as log
from Funtionality.Config import app_folder, TEMP, model_file


def load_landmarks(folder):
    landmarks_files = glob.glob(folder + '/*.npy')
    landmarks = []

    for file in landmarks_files:
        file_landmarks = np.load(file)
        landmarks.append(file_landmarks)

    return np.concatenate(landmarks, axis=0)


def train_model():
    # Step 1: Load the pose landmarks from the folder
    temp_folder = os.path.join(app_folder, TEMP)
    good_folder = os.path.join(temp_folder, 'good')
    bad_folder = os.path.join(temp_folder, 'bad')

    landmarks_good = load_landmarks(good_folder)
    landmarks_bad = load_landmarks(bad_folder)

    # Step 2: Prepare your training data
    features = np.concatenate((landmarks_good, landmarks_bad), axis=0)
    labels = np.concatenate((np.zeros(len(landmarks_good)), np.ones(len(landmarks_bad))), axis=0)

    # Step 3: Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Step 4: Choose and train your classifier
    classifier = SVC()
    with parallel_backend('threading', n_jobs=-1):
        classifier.fit(X_train, y_train)

    # Step 5: Evaluate the trained classifier
    accuracy = classifier.score(X_test, y_test)
    log.info(f"Model Accuracy: {accuracy}")

    # Step 6: Save the trained classifier
    joblib.dump(classifier, model_file)
    log.info(f"Trained model saved as {model_file}")