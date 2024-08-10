import numpy as np
from mathfunctions import angle_between_points, smooth
from rep_sep import set_keypoints, get_exercice, rep_separator, get_all_peaks

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
        return abs(np.mean(self.rightKnee_Angles[:5]) - np.mean(self.rightKnee_Angles[-5:])) < 15
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
