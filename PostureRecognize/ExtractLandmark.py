def extract_landmark(detection_result):
    if detection_result is not None and detection_result.pose_landmarks:
        # Create a list to store pose landmarks for this detection
        pose_landmarks_list = []

        # Iterate through the pose landmarks for this detection
        for landmark in detection_result.pose_landmarks[0]:
            # Extract landmark values and create a vector
            landmark_vector = [
                landmark.x,
                landmark.y,
                landmark.z,
                landmark.visibility,
                landmark.presence
            ]

            # Append the landmark vector to the list for this detection
            pose_landmarks_list.append(landmark_vector)
        return pose_landmarks_list

