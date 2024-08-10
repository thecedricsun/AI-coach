from ultralytics import YOLO
import pickle
import numpy as np
from scipy.signal import find_peaks
from mathfunctions import angle_between_points, smooth

# model = YOLO("yolov8n-pose.pt")

# # Serialize the model to a file
# with open('yolov8n_model.pkl', 'wb') as file:
#     pickle.dump(model, file)

def set_keypoints(video):
    # load the model from pickle
    with open('yolov8n_model.pkl', 'rb') as file:
        model = pickle.load(file)
    # use the model on the imported video
    results = model(source=video, conf=0.4, save=False)
    # results_keypoint = results[0].keypoints.xyn.cpu().numpy()[0]
    results_keypoint_solo = []
    for r in results:
        results_keypoint_solo.append(r.keypoints.xyn.cpu().numpy()[0])
    return results_keypoint_solo

def get_exercice(current_exercice, results_keypoint_solo):
    # only calculate the angles we need, to separate the reps
    if current_exercice == "squat": # right knee angle
        return [angle_between_points(results_keypoint_solo[i][16],results_keypoint_solo[i][14],results_keypoint_solo[i][12]) for i in range(len(results_keypoint_solo))]
    elif current_exercice == "pullUp": # right armpit angle
        return [angle_between_points(results_keypoint_solo[i][8],results_keypoint_solo[i][6],results_keypoint_solo[i][12]) for i in range(len(results_keypoint_solo))]
    elif current_exercice == "pushUp": # right elbow angle
        return [angle_between_points(results_keypoint_solo[i][6],results_keypoint_solo[i][8],results_keypoint_solo[i][10]) for i in range(len(results_keypoint_solo))]
    

def get_all_peaks(current_exercice, keypoints):
    # Smooth the angles
    smoothed_angles = np.array(smooth(get_exercice(current_exercice, keypoints), 0.8))
    # Adjust find_peaks parameters
    peaks, _ = find_peaks(smoothed_angles, prominence=0.7, distance=40)  # Example parameters
    valleys, _ = find_peaks(-smoothed_angles, prominence=0.7, distance=50)
    # Visualization
    # plt.figure(figsize=(12, 6))
    # plt.plot(smoothed_angles, label='Smoothed Angles')
    # plt.scatter(peaks, smoothed_angles[peaks], color='red', label='Filtered Peaks')
    # plt.scatter(minima, smoothed_angles[minima], color='green', label='Filtered Valleys')
    # plt.title('Filtered Peaks and Valleys')
    # plt.legend()
    # plt.xlabel('Frame')
    # plt.ylabel('Angle')
    # plt.show()
    return smoothed_angles, peaks, valleys

def rep_separator(smoothed_angles, peaks, valleys):
    all_points = []
    # if peaks[0] < valleys[0]:
    #     peaks = peaks[1:]
    all_points += [(0, 'peak')] + [(p, 'peak') for p in peaks] + [(v, 'valley') for v in valleys]
    # Append a peak at the end, using the last index of smoothed_angles
    all_points += [(len(smoothed_angles) - 1, 'peak')]
    all_points = sorted(all_points, key=lambda x: x[0])
    # print(all_points)
    # if there are two 2 peaks in a row, we remove the peak with the lowest value
    # if there are two 2 valleys in a row, we remove the valley with the highest value
    to_remove = []
    for i in range(1, len(all_points)):
        if all_points[i][1] == all_points[i-1][1]:
            if all_points[i][1] == 'peak':
                if smoothed_angles[all_points[i][0]] < smoothed_angles[all_points[i-1][0]]:
                    to_remove.append(all_points[i][0])
                else:
                    to_remove.append(all_points[i-1][0])
            else:
                if smoothed_angles[all_points[i][0]] > smoothed_angles[all_points[i-1][0]]:
                    to_remove.append(all_points[i][0])
                else:
                    to_remove.append(all_points[i-1][0])
    # print(to_remove)
    # remove the points
    all_points = [p for p in all_points if p[0] not in to_remove]
    # print(all_points)
    '''
    We now have a list of peaks and valleys that we can use to separate the repetitions.
    we will iterate through smooth_angles and create an element per rep in the tab reps
    '''
    # complete here, we need to create the reps tab
    # in each element we will have another tab with each frame of the rep
    # rep = starts at a peak, and through a low, then finishes at the next peak.
    # the next rep starts at the peak the previous rep finished at.
    reps = []
    # Loop through all_points, stepping by 2 to jump from peak to valley to peak
    for i in range(2, len(all_points), 2):  # Start from the second peak and step by 2
        # Ensure not to exceed the list's length
        if i < len(all_points):
            # Slice from the current peak (i-2) to the next peak (i) to include the full rep
            rep = smoothed_angles[all_points[i-2][0]:all_points[i][0] + 1]
            reps.append(rep)
    return reps