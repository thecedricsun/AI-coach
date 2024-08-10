# imports
from ultralytics import YOLO
import matplotlib.pyplot as plt
import numpy as np
import pickle
from typing import List
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# model = YOLO("yolov8n-pose.pt")

# Serialize the model to a file
# with open('yolov8n_model.pkl', 'wb') as file:
#     pickle.dump(model, file)
# video = "Videos/squatAlexParfait4.mp4"
# video = "Videos/squatAlexParfai5t.mp4"
video = "Videos/squatAlexFail.mp4"
current_exercice = "squat"
# current_exercice = "pullUp"
# current_exercice = "pushUp"

# convertisseur video en HD, 30 fps

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

# set once, then get keypoints
results_keypoint_solo = set_keypoints(video)
def get_keypoints():
    return results_keypoint_solo

def angle_between_points(point1, point2, point3):
    vector1 = point1 - point2
    vector2 = point3 - point2
    dot_product = np.dot(vector1, vector2)
    cross_product = np.cross(vector1, vector2)
    angle_radians = np.arctan2(np.linalg.norm(cross_product), dot_product)
    angle_degrees = np.degrees(angle_radians)
    return angle_degrees

# smoother function
def smooth(scalars: List[float], weight: float) -> List[float]:  # Weight between 0 and 1
    last = scalars[0]  # First value in the plot (first timestep)
    smoothed = list()
    for point in scalars:
        smoothed_val = last * weight + (1 - weight) * point  # Calculate smoothed value
        smoothed.append(smoothed_val)                        # Save it
        last = smoothed_val                                  # Anchor the last smoothed value
    return smoothed

# angles that are interesting
'''
leftKnee = (15, 13, 11)
rightKnee = (16, 14, 12)

leftHip = (13, 11, 5)
rightHip = (14, 12, 6)

leftElbow = (5, 7, 9)
rightElbow = (6, 8, 10)

leftArmpit = (7, 5, 11)
rightArmpit = (8, 6, 12)

leftShoulder = (7, 5, 6)
rightShoulder = (8, 6, 5)
'''
# which gives using the function angle_between_points :
'''
leftKnee = [angle_between_points(results_keypoint_solo[i][15],results_keypoint_solo[i][13],results_keypoint_solo[i][11]) for i in range(len(results_keypoint_solo))]
rightKnee = [angle_between_points(results_keypoint_solo[i][16],results_keypoint_solo[i][14],results_keypoint_solo[i][12]) for i in range(len(results_keypoint_solo))]

leftHip = [angle_between_points(results_keypoint_solo[i][13],results_keypoint_solo[i][11],results_keypoint_solo[i][5]) for i in range(len(results_keypoint_solo))]
rightHip = [angle_between_points(results_keypoint_solo[i][14],results_keypoint_solo[i][12],results_keypoint_solo[i][6]) for i in range(len(results_keypoint_solo))]

leftElbow = [angle_between_points(results_keypoint_solo[i][5],results_keypoint_solo[i][7],results_keypoint_solo[i][9]) for i in range(len(results_keypoint_solo))]
rightElbow = [angle_between_points(results_keypoint_solo[i][6],results_keypoint_solo[i][8],results_keypoint_solo[i][10]) for i in range(len(results_keypoint_solo))]

leftArmpit = [angle_between_points(results_keypoint_solo[i][7],results_keypoint_solo[i][5],results_keypoint_solo[i][11]) for i in range(len(results_keypoint_solo))]
rightArmpit = [angle_between_points(results_keypoint_solo[i][8],results_keypoint_solo[i][6],results_keypoint_solo[i][12]) for i in range(len(results_keypoint_solo))]

leftShoulder = [angle_between_points(results_keypoint_solo[i][7],results_keypoint_solo[i][5],results_keypoint_solo[i][6]) for i in range(len(results_keypoint_solo))]
rightShoulder = [angle_between_points(results_keypoint_solo[i][8],results_keypoint_solo[i][6],results_keypoint_solo[i][5]) for i in range(len(results_keypoint_solo))]
'''

# if squat, we need right knee angles, which is angle_between_points(16, 14, 12)
# if pullUp, we need right armpit angles, which is angle_between_points(8, 6, 12)
# if pushUp, we need right elbow angles, which is angle_between_points(6, 8, 10)
def get_exercice(current_exercice):
    results_keypoint_solo = get_keypoints()
    # only calculate the angles we need, to separate the reps
    if current_exercice == "squat": # right knee angle
        return [angle_between_points(results_keypoint_solo[i][16],results_keypoint_solo[i][14],results_keypoint_solo[i][12]) for i in range(len(results_keypoint_solo))]
    elif current_exercice == "pullUp": # right armpit angle
        return [angle_between_points(results_keypoint_solo[i][8],results_keypoint_solo[i][6],results_keypoint_solo[i][12]) for i in range(len(results_keypoint_solo))]
    elif current_exercice == "pushUp": # right elbow angle
        return [angle_between_points(results_keypoint_solo[i][6],results_keypoint_solo[i][8],results_keypoint_solo[i][10]) for i in range(len(results_keypoint_solo))]

def get_all_peaks():
    # Smooth the angles
    smoothed_angles = np.array(smooth(get_exercice(current_exercice), 0.8))
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

def rep_separator():
    temp = get_all_peaks()
    smoothed_angles = temp[0]
    peaks = temp[1]
    valleys = temp[2]
    all_points = [(0, 'peak')] + [(p, 'peak') for p in peaks] + [(v, 'valley') for v in valleys]
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

# # test plot all reps colored differently
# offset = 0
# reps = rep_separator()
# for rep in reps:
#     plt.plot(range(offset, offset + len(rep)), rep, label="Rep at frame : "+str(offset))
#     offset += len(rep)
# # plt.axhline(y=150, color='r', linestyle='-', label="Threshold 150")
# plt.title('Repetitions')
# plt.legend()
# plt.show()

# class ExerciseRep, for herited classes
class ExerciseRep:
    def __init__(self, duration, rep_number, start_frame, end_frame, frames):
        self.duration = duration
        self.rep_number = rep_number
        self.start_frame = start_frame
        self.end_frame = end_frame
        # frames = keypoint_solo[start_frame:end_frame]
        self.frames = frames
        # frames = keypoint_solo délimité par start_frame et end_frame
    def __str__(self):
        return f"Rep {self.rep_number} : duration = {self.duration}"

# class squat
class SquatRep(ExerciseRep):
    def __init__(self, duration, rep_number, start_frame, end_frame, frames):
        super().__init__(duration, rep_number, start_frame, end_frame, frames)
        self.squat_depth = self.set_squat_depth()
        self.rightKnee_Angles = self.set_rightKnee_Angles()
        self.amplitude = self.set_amplitude()
        self.integrity = self.set_integrity()
    def set_squat_depth(self):
        hip_heights = smooth([self.frames[i][12][1] for i in range(len(self.frames))], 0.8)  # hip is at index 12
        knee_heights = smooth([self.frames[i][14][1] for i in range(len(self.frames))], 0.8)  # knee is at index 14
        # hip_heights_flipped = flip_curve_to_valley_with_same_min_max(hip_heights)
        # knee_heights_flipped = flip_curve_to_valley_with_same_min_max(knee_heights)
        # H1 is max hip height, which is first frame
        H1 = hip_heights[0]
        # H2 is current hip height
        # G1 is max knee height, which is first frame
        G1 = knee_heights[0]
        # G2 is current knee height
        # return ((H2 - G2) * 100) / (H1 - G1)
        # for test, return H2 and G2
        # return [(H2, G2) for H2, G2 in zip(hip_heights, knee_heights)]
        # this returns plots that are flipped, to get a more logical 0 to 80% depth reached.
        return [100 - (abs(H2 - G2) * 100) / abs(H1 - G1) for H2, G2 in zip(hip_heights, knee_heights)]
        # this returns the regular plots, but the % are filpped, so at squat lowest point, there is 20% left
        return [(abs(H2 - G2) * 100) / abs(H1 - G1) for H2, G2 in zip(hip_heights, knee_heights)]
    def set_amplitude(self):
        # create angles for right knee, using function angle_between_points
        # using max - min to get the amplitude
        return max(self.rightKnee_Angles) - min(self.rightKnee_Angles)
    def set_rightKnee_Angles(self):
        raw_angles = [angle_between_points(self.frames[i][16],self.frames[i][14],self.frames[i][12]) for i in range(len(self.frames))]
        # smooth before return
        return smooth(raw_angles, 0.8)
    def set_integrity(self):
        # this funciton will return a bool that will indicate :
        # if the angle right knee at first few frames is equal to the angle at the last few frames
        # difference of mean has to be smaller than 10% betwee nthe first 5 frames and the last 5 frames
        return abs(np.mean(self.rightKnee_Angles[:5]) - np.mean(self.rightKnee_Angles[-5:])) < 10
    def __str__(self):
        return super().__str__() + f", squat depth = {self.squat_depth}, amplitude = {self.amplitude}, right knee angles = {self.rightKnee_Angles}"

# class pushup
class PushupRep(ExerciseRep):
    def __init__(self, duration, rep_number, start_frame, end_frame, frames, pushup_depth):
        super().__init__(duration, rep_number, start_frame, end_frame, frames)
        self.pushup_depth = pushup_depth
    def __str__(self):
        return super().__str__() + f", pushup depth = {self.pushup_depth}"

# class pullup
class PullupRep(ExerciseRep):
    def __init__(self, duration, rep_number, start_frame, end_frame, frames, pullup_depth):
        super().__init__(duration, rep_number, start_frame, end_frame, frames)
        self.pullup_depth = pullup_depth
    def __str__(self):
        return super().__str__() + f", pullup depth = {self.pullup_depth}"

def all_Rep_Indexes(reps):
    all_Rep_Indexes = [0]
    for rep in reps:
        all_Rep_Indexes.append(all_Rep_Indexes[-1] + len(rep))
    return all_Rep_Indexes

reps = rep_separator()
if current_exercice == "squat":
    squatReps = [SquatRep(len(rep), i, all_Rep_Indexes(reps)[i], all_Rep_Indexes(reps)[i+1], results_keypoint_solo[all_Rep_Indexes(reps)[i]:all_Rep_Indexes(reps)[i+1]]) for i, rep in enumerate(reps)]
elif current_exercice == "pushUp":
    pushupReps = [PushupRep(len(rep), i, all_Rep_Indexes(reps)[i], all_Rep_Indexes(reps)[i+1], results_keypoint_solo[all_Rep_Indexes(reps)[i]:all_Rep_Indexes(reps)[i+1]], 0) for i, rep in enumerate(reps)]
elif current_exercice == "pullUp":
    pullupReps = [PullupRep(len(rep), i, all_Rep_Indexes(reps)[i], all_Rep_Indexes(reps)[i+1], results_keypoint_solo[all_Rep_Indexes(reps)[i]:all_Rep_Indexes(reps)[i+1]], 0) for i, rep in enumerate(reps)]

# plot each squat rep frames
# for rep in squatReps:
#     plt.plot(rep.rightKnee_Angles, label="Rep " + str(rep.rep_number))
# plt.legend()
# plt.show()

def individual_rep_stats(rep, current_exercice):
    if current_exercice == "squat":
        rep_duration = rep.duration/30
        max_squat_depth = max(rep.squat_depth)
        good_rep = ((max_squat_depth > 75) and rep.integrity)
        return (rep.rep_number, max_squat_depth, rep_duration, good_rep)
    elif current_exercice == "pushUp":
        pass
    elif current_exercice == "pullUp":
        pass

# new functipon to attribut a score to, not the rep, but the whole set, based on the individual rep stats, using coefs, and means
# we want to return a tuple with the score, and the number of good reps
# we want to return the number of good reps, the number of bad reps, the score, and the total number of reps
def set_score(reps, exercise_type):
    good_reps = 0
    bad_reps = 0
    total_reps = len(reps)
    score = 0
    reps = [individual_rep_stats(rep, exercise_type) for rep in reps]
    for rep in reps:
        if rep[3]:
            good_reps += 1
        else:
            bad_reps += 1
        score += rep[1]
    # calculate variance on
    variance = np.var([rep[2] for rep in reps])
    # print(variance * 100)
    # score kept as int
    average_score = (score / total_reps) * 10
    score = int(average_score - (variance * 100))
    # Deduct 15 percent of the score for each bad rep
    score -= int((15 / 100) * score * bad_reps)
    if score < 10:
        # random int bewteen 0 and 10
        score = np.random.randint(0, 10)
    if score > 1000:
        score = 1000
    return (good_reps, bad_reps, total_reps, score)

# make a quick sentence, to give a feedback to the user
def feedback():
    temp = set_score(squatReps, "squat")
    print(f"Good reps : {temp[0]}, Bad reps : {temp[1]}, Total reps : {temp[2]}, Score : {temp[3]}")
feedback()