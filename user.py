import pickle as pkl

class User():
    def __init__(self, username, password, score=[]):
        self.username = username
        self.password = password
        # Initialize the score list with 0s
        self.score = score if score else [0]*4
    
    def update_score(self, exercise_index, new_score):
        if new_score > self.score[exercise_index]:
            self.score[exercise_index] = new_score

def save_users(users, filename):
    with open(filename, 'wb') as file:
        pkl.dump(users, file)

def load_users(filename):
    try:
        with open(filename, 'rb') as file:
            return pkl.load(file)
    except FileNotFoundError:
        return []
