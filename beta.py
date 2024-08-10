from kivymd.app import MDApp

from kivy.clock import Clock

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.lang.builder import Builder
from screen_manager import screen_helper
import matplotlib.pyplot as plt

from mathfunctions import all_Rep_Indexes, set_score
from rep_sep import set_keypoints, get_exercice, rep_separator, get_all_peaks
from classes import ExerciseRep, SquatRep, PushupRep, PullupRep
from user import User, save_users, load_users

import os

Window.size = (450, 750)

class MainScreen(Screen):
    pass

class LoginScreen(Screen):
    def verify_credentials(self, username, password):
        if os.path.exists('files/users.pkl'):
            loaded = load_users('files/users.pkl')
            for user in loaded:
                if username == user.username and password == user.password:
                    return True
        return False

class SignScreen(Screen):
    def save_user(self, username, password):
        if not os.path.exists('files/users.pkl'):
            save_users([], 'files/users.pkl')
        loaded = load_users('files/users.pkl')
        user = User(username, password)
        loaded.append(user)
        save_users(loaded, 'files/users.pkl')

class ProfileScreen(Screen):
    pass

class LadderChooseExerciceScreen(Screen):
    pass

class VideoScreen(Screen):
    pass

class ProfilePhotoPopup(Popup):
    pass

class VideoPopup(Popup):
    pass

class RankingScreen(Screen):
    pass

class RankingPompeScreen(Screen):
    pass

class CustomPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Options"
        self.size_hint = (None, None)
        self.size = (500, 200)
        self.auto_dismiss = True

        # Contenu de la fenêtre contextuelle
        layout = BoxLayout(orientation='vertical')
        button1 = Button(text='Changer la photo de profile', size_hint_y=None, height=40)
        button1.bind(on_release=self.option1_pressed)
        button2 = Button(text='Sign Out', size_hint_y=None, height=40)
        button2.bind(on_release=self.option2_pressed)
        layout.add_widget(button1)
        layout.add_widget(button2)
        self.content = layout

    def option1_pressed(self, instance):
        app = MDApp.get_running_app()  # Obtenir l'instance de l'application
        app.open_image_selector()

    def option2_pressed(self, instance):
        app = MDApp.get_running_app()
        app.root.current = 'main'
        #dismiss the popup
        self.dismiss()

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(SignScreen(name='sign'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(LadderChooseExerciceScreen(name='exercice'))
sm.add_widget(VideoScreen(name='video'))
sm.add_widget(RankingScreen(name='ranking'))
sm.add_widget(RankingPompeScreen(name='rankingpompe'))

class Beta(MDApp):

    current_exercice = ""
    current_exercice_index = 0
    current_user = None

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        screen = Builder.load_string(screen_helper)
        return screen

    def load_video(self, selection):
        if selection:
            video_path = selection[0]
            if video_path:  # Check if the path is not empty
                video_screen = self.root.get_screen('video')
                video_screen.ids.video_player.source = video_path
                video_screen.ids.video_player.state = 'play'

                self.keypoints = set_keypoints(video_path)
                angles, peaks, valleys = get_all_peaks(self.current_exercice, self.keypoints)
                reps = rep_separator(angles, peaks, valleys)

                self.create_plot(reps)  # Create a plot when loading a video

                self.root.current = 'video'
                if hasattr(self, 'popup'):  # Ensure the popup reference exists
                    self.popup.dismiss()  # Dismiss the popup

    def load_image(self, selection):
        if selection:
            image_path = selection[0]
            if image_path:  
                profile_screen = self.root.get_screen('profile')
                profile_screen.ids.profile_image.source = image_path
                if hasattr(self, 'popup'):  
                    self.popup.dismiss()
    
    def open_image_selector(self):
        self.popup = ProfilePhotoPopup()
        self.popup.open()

    def open_custom_popup(self):
        popup = CustomPopup()
        popup.open()

    def show_video_popup(self, exercice):
        self.current_exercice = exercice
        self.check_exercice(exercice)
        self.popup = VideoPopup()
        self.popup.open()

    def login(self, username, password):
        login_screen = self.root.get_screen('login')
        if login_screen.verify_credentials(username, password):
            self.current_user = username
            self.root.current = 'exercice'  # Navigate to ExerciceScreen if credentials are correct
            profile_screen = self.root.get_screen('profile')
            profile_screen.ids.username.text = username
        else:
            # Handle incorrect credentials here (e.g., display an error message)
            print("Incorrect username or password")

    def sign(self, username, password):
        sign_screen = self.root.get_screen('sign')
        if username and password:
            sign_screen.save_user(username, password)
            self.root.current = 'login'

    def create_plot(self, reps):
        if self.current_exercice == "squat":
            squatReps = [SquatRep(len(rep), i, all_Rep_Indexes(reps)[i], all_Rep_Indexes(reps)[i+1], self.keypoints[all_Rep_Indexes(reps)[i]:all_Rep_Indexes(reps)[i+1]]) for i, rep in enumerate(reps)]
            for rep in squatReps:
                plt.plot(rep.rightKnee_Angles, label="Rep" + str(rep.rep_number + 1))
            plt.legend()
            plt.savefig('assets/plot_integrity.png')  # Save the plot as an image
            plt.close()
        elif self.current_exercice == "pushUp":
            pushupReps = [PushupRep(len(rep), i, all_Rep_Indexes(reps)[i], all_Rep_Indexes(reps)[i+1], self.keypoints[all_Rep_Indexes(reps)[i]:all_Rep_Indexes(reps)[i+1]], 0) for i, rep in enumerate(reps)]
        elif self.current_exercice == "pullUp":
            pullupReps = [PullupRep(len(rep), i, all_Rep_Indexes(reps)[i], all_Rep_Indexes(reps)[i+1], self.keypoints[all_Rep_Indexes(reps)[i]:all_Rep_Indexes(reps)[i+1]], 0) for i, rep in enumerate(reps)]

        self.score = set_score(squatReps, self.current_exercice)[3]
        print(self.score)

        # Create a simple plot
        offset = 0
        for rep in reps:
            plt.plot(range(offset, offset + len(rep)), rep)
            offset += len(rep)
        plt.savefig('assets/plot.png')  # Save the plot as an image
        plt.close()
        
        self.update_plot_image() # Update the plot image in the VideoScreen

        # Update the score label
        video_screen = self.root.get_screen('video')
        video_screen.ids.score_label.text = f"S C O R E : {self.score}"  # Update the label text

        # Update the profile score
        loaded = load_users('files/users.pkl')
        for user in loaded:
            if self.current_user == user.username:
                user.update_score(self.current_exercice_index, self.score)
        save_users(loaded, 'files/users.pkl')
    
    def update_plot_image(self):
        video_screen = self.root.get_screen('video')

        video_screen.ids.plot_image.source = 'assets/plot.png'  # Update the image source
        video_screen.ids.plot_image.reload()  # Force refresh the image

        video_screen.ids.plot_integrity.source = 'assets/plot_integrity.png'
        video_screen.ids.plot_integrity.reload()

    def on_profile_enter(self):
        self.update_profile_score()

    def update_profile_score(self):
        profile_screen = self.root.get_screen('profile')
        loaded = load_users('files/users.pkl')
        for user in loaded:
            if self.current_user == user.username:
                for i, score in enumerate(user.score):
                    label_id = f'exercice_{i}_score'
                    profile_screen.ids[label_id].text = str(score)

    def check_exercice(self, exercice):
        if exercice == "pushUp":
            self.current_exercice_index = 0
        elif exercice == "squat":
            self.current_exercice_index = 1
        elif exercice == "pullUp":
            self.current_exercice_index = 2

if __name__ == "__main__":
    Beta().run()