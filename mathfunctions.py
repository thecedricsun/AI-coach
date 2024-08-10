import numpy as np
from typing import List

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

def all_Rep_Indexes(reps):
    all_Rep_Indexes = [0]
    for rep in reps:
        all_Rep_Indexes.append(all_Rep_Indexes[-1] + len(rep))
    return all_Rep_Indexes

def individual_rep_stats(rep, current_exercice):
    if current_exercice == "squat":
        rep_duration = rep.duration/30
        max_squat_depth = max(rep.squat_depth)
        good_rep = ((max_squat_depth > 75) and rep.integrity)
        print(rep.integrity)
        print(max_squat_depth)
        return (rep.rep_number, max_squat_depth, rep_duration, good_rep)
    elif current_exercice == "pushUp":
        pass
    elif current_exercice == "pullUp":
        pass

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
