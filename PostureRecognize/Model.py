import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import os
import glob
import joblib
import logging as log
from Funtionality.Config import temp_folder, model_file


def load_landmarks(folder):
    # TODO check if the landmark file is > 30 or is not empty
    landmarks_files = glob.glob(folder + '/*.npy')
    landmarks = []
    for file in landmarks_files:
        file_landmarks = np.load(file)
        landmarks.append(file_landmarks)

    return np.concatenate(landmarks, axis=0)


def train_model():
    good_folder = os.path.join(temp_folder, 'good')
    bad_folder = os.path.join(temp_folder, 'bad')

    landmarks_good = load_landmarks(good_folder)
    landmarks_bad = load_landmarks(bad_folder)

    # Prepare your training data with the existing classes
    features = np.concatenate((landmarks_good, landmarks_bad), axis=0)
    labels = np.concatenate((np.zeros(len(landmarks_good)), np.ones(len(landmarks_bad))), axis=0)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Append multiple new classes
    temp_folder_contents = os.listdir(temp_folder)
    new_classes_folders = [folder for folder in temp_folder_contents if folder.startswith('append_')]

    for idx, new_folder in enumerate(new_classes_folders):
        folder_path = os.path.join(temp_folder, new_folder)
        landmarks_new = load_landmarks(folder_path)
        new_labels = np.full(len(landmarks_new), idx + 2)  # Assign unique labels to the new classes

        X_train = np.concatenate((X_train, landmarks_new), axis=0)
        y_train = np.concatenate((y_train, new_labels), axis=0)

    # Step 4: Choose and train your classifier
    classifier = SVC()
    classifier.fit(X_train, y_train)

    # Step 5: Evaluate the trained classifier
    accuracy = classifier.score(X_test, y_test)
    log.info(f"Model Accuracy: {accuracy}")  # TODO add handler if accuracy < 0.6

    # Step 6: Save the trained classifier
    joblib.dump(classifier, model_file)
    log.info(f"Trained model saved as {model_file}")
