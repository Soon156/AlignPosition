import math
import os
from concurrent.futures import ThreadPoolExecutor
from tensorflow.keras.callbacks import EarlyStopping
from mediapipe import tasks, Image
import numpy as np
import tensorflow as tf
from PostureRecognize.ExtractLandmark import extract_landmark
from sklearn.model_selection import train_test_split
from sklearn.utils import compute_class_weight


def preprocess_img(epoch=100, batch_size=12):
    labels = ['good', 'bad']
    file_counts = []
    counts = 0

    for label in labels:
        # List all files in the folder
        files = os.listdir(label)
        # Count the files
        file_count = len([f for f in files])
        file_counts.append(file_count)
        counts += file_count
        print(f"Number of files in the {label} folder: {file_count}")
    print(f"Total files: {counts}")
    with ThreadPoolExecutor() as executor:
        good = executor.submit(process_img, "good")
        bad = executor.submit(process_img, "bad")
        good_result = good.result()
        bad_result = bad.result()

    n_batches = counts / batch_size
    n_batches = math.ceil(n_batches)

    train_model(good_result, bad_result, n_batches, epoch)


def process_img(folder_path):
    base_options = tasks.BaseOptions(model_asset_path='pose_landmarker_heavy.task')
    options = tasks.vision.PoseLandmarkerOptions(base_options=base_options)
    detector = tasks.vision.PoseLandmarker.create_from_options(options)
    landmark_vectors = []
    pose_landmarks_list = None

    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate through each file in the folder
    for file_name in file_list:
        # Check if the file is an image (you can add more file extensions if needed)
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Construct the full path to the image file
            image_path = os.path.join(folder_path, file_name)
            mp_image = Image.create_from_file(image_path)
            if mp_image is not None:
                detection_result = detector.detect(mp_image)
                pose_landmarks_list = extract_landmark(detection_result)

            # Append the list of pose landmarks for this detection to the landmark_vectors list
            landmark_vectors.append(pose_landmarks_list)
    return np.array(landmark_vectors)


def train_model(good_landmark, bad_landmark, batch_size, epoch=60, num_landmarks=33,
                num_features_per_landmark=5):
    # Reshape the array to have the shape (number_of_samples, number_of_landmarks * number_of_features_per_landmark)
    landmarks_good = good_landmark.reshape(-1, num_landmarks * num_features_per_landmark)
    landmarks_bad = bad_landmark.reshape(-1, num_landmarks * num_features_per_landmark)
    features = np.concatenate((landmarks_good, landmarks_bad), axis=0)
    labels = np.concatenate((np.zeros(len(landmarks_good)), np.ones(len(landmarks_bad))), axis=0)

    # Calculate class weights
    class_weights = compute_class_weight('balanced', classes=np.unique(labels), y=labels)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2,
                                                        random_state=42)

    # Define your TensorFlow model
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(num_landmarks * num_features_per_landmark,)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    # model.summary()

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    early_stopping = EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True)

    weights = dict(enumerate(class_weights))

    print(f"Class weights [good, bad]: {class_weights}")
    print(f"Batch size: {batch_size}")

    # Train the model
    model.fit(X_train, y_train, epochs=epoch, batch_size=batch_size,
              validation_data=(X_test, y_test), class_weight=weights, callbacks=[early_stopping])

    # Evaluate the model
    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    print(f"Test Accuracy: {test_accuracy}")

    model.save("..\posture_detection_model.keras")


preprocess_img(epoch=999, batch_size=10)
