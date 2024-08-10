screen_helper = """

ScreenManager:
    MainScreen:
    LoginScreen:
    SignScreen:
    ProfileScreen:
    RankingScreen:
    RankingPompeScreen:
    LadderChooseExerciceScreen:
    VideoScreen:

<MainScreen>:
    name: 'main'
    Image:
        source: 'assets/mainscreen.png'
        size_hint: (None, None)
        size: (300, 300)
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
    BoxLayout:
        size_hint: .85, None
        height: "30dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        spacing: "5dp"
        MDRaisedButton:
            text: "Login"
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'login'
            size_hint_x: 1
        MDRectangleFlatButton:
            text: "Sign Up"
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'sign'
            size_hint_x: 1
    
<LoginScreen>:
    name: 'login'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y': .95}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'main'
        MDLabel:
            text: "S I U U U U U U U !"
            pos_hint: {'center_x': .6, 'center_y': .85}
            haligh: 'center'
            font_size: '30sp'
            color: rgba(0, 57, 119, 255)
        
        MDLabel:
            text: "Log in to continue"
            pos_hint: {'center_x': .6, 'center_y': .8}
            haligh: 'center'
            font_size: '16sp'
            color: rgba(83, 107, 133, 255)

        MDTextField:
            id: username
            hint_text: "Enter username"
            icon_right: "account"
            icon_right_color: app.theme_cls.primary_color 
            pos_hint: {'center_x': .5, 'center_y': .65}
            size_hint_x: .85
            on_text : self.text = self.text.replace(' ', '')
            write_tab: False

        MDTextField:
            id: password
            hint_text: "Enter password"
            password: True
            icon_right: "lock"
            icon_right_color: app.theme_cls.primary_color 
            pos_hint: {'center_x': .5, 'center_y': .55}
            size_hint_x: .85
            on_text : self.text = self.text.replace(' ', '')
            write_tab: False

        MDRaisedButton:
            text: "Login"
            pos_hint: {'center_x': .5, 'center_y': .35}
            size_hint_x: .85
            on_release:
                app.login(username.text, password.text)
        MDTextButton:
            text: "Forgot password?"
            pos_hint: {'center_x': .5, 'center_y': .3}
            color: rgba(83, 107, 133, 255)
            font_style: 'Caption'
        MDLabel:
            text: "or"
            pos_hint: {'center_x': .5, 'center_y': .25}
            halign: 'center'
            font_size: '14sp'
            color: rgba(0, 57, 119, 255)
        MDFloatLayout:
            md_bg_color: rgba(83, 107, 133, 255)
            size_hint: .3, .002
            pos_hint: {'center_x': .3, 'center_y': .25}
        MDFloatLayout:
            md_bg_color: rgba(83, 107, 133, 255)
            size_hint: .3, .002
            pos_hint: {'center_x': .7, 'center_y': .25}
        MDGridLayout:
            cols: 3
            pos_hint: {'center_x': .5, 'center_y': .18}
            size_hint: .5, .1
            spacing: "30dp"
            MDIconButton:
                icon: 'assets/facebook.png'
                size_hint:  .9, .9
            MDIconButton:
                icon: 'assets/apple.png'
                size_hint: .9, .9
            MDIconButton:
                icon: 'assets/google.png'
                size_hint: .9, .9

<SignScreen>:
    name: 'sign'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y': 0.95}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'main'
        MDLabel:
            text: "S I U U U U U U U !"
            pos_hint: {'center_x': 0.6, 'center_y': 0.85}
            haligh: 'center'
            font_size: '30sp'
            color: rgba(0, 57, 119, 255)
        
        MDLabel:
            text: "Sign in to continue"
            pos_hint: {'center_x': 0.6, 'center_y': 0.8}
            haligh: 'center'
            font_size: '16sp'
            color: rgba(83, 107, 133, 255)

        MDTextField:
            id: username
            hint_text: "Enter username"
            icon_right: "account"
            icon_right_color: app.theme_cls.primary_color 
            pos_hint: {'center_x': 0.5, 'center_y': 0.55}
            size_hint_x: .85
            on_text : self.text = self.text.replace(' ', '')
            write_tab: False

        MDTextField:
            id: password
            hint_text: "Enter password"
            password: True
            icon_right: "lock"
            icon_right_color: app.theme_cls.primary_color 
            pos_hint: {'center_x': 0.5, 'center_y': 0.45}
            size_hint_x: .85
            on_text : self.text = self.text.replace(' ', '')
            write_tab: False

        BoxLayout:
            size_hint: .85, None
            height: "30dp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.38}
            spacing: "5dp"
            MDCheckbox:
                id: checkbox
                size_hint: None, None
                width: "30dp"
                height: "30dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: password.password = not password.password
            MDLabel:
                text: "[ref=Show Password]Show password[/ref]"
                markup: True
                pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
                on_ref_press: 
                    password.password = not password.password
                    checkbox.active = not checkbox.active
            
        MDRaisedButton:
            text: "Sign Up"
            pos_hint: {'center_x': .5, 'center_y': .25}
            size_hint_x: .85
            on_release:
                app.sign(username.text, password.text)
                
<ProfileScreen>:
    name: 'profile'

    MDLabel:
        text: "Mon Profil"
        font_name: 'fonts/Poppins-Bold.ttf'
        theme_text_color: "Custom"
        color: rgba(0, 57, 119, 255)
        font_size: '24sp'
        pos_hint: {'x': 0.1, 'top': 1.45}

    MDIconButton:
        icon:"arrow-left"
        pos_hint: {"center_y":.95}
        user_font_size: "20sp"
        theme_text_color: "Primary"
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = 'exercice'
    
    MDIconButton:
        icon: "dots-vertical"
        pos_hint: {"center_x":.93, "center_y": .95}
        user_font_size: "20sp"
        theme_text_color: "Custom"
        text_color: rgba(71,92,119,255)
        on_release: app.open_custom_popup()

    FloatLayout:
        size_hint: None, None
        size: (200, 200)
        pos_hint: {'center_x': 0.5, 'center_y': 0.80} 

        AsyncImage:
            id : profile_image
            source: "assets/coach.png"
            size_hint: None, None
            size: (150, 150)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDLabel:
        id: username
        text: "Nom de l'utilisateur"
        font_name: 'fonts/Poppins-Bold.ttf'
        halign: "center"
        theme_text_color: "Custom"
        color: rgba(0, 57, 119, 255)
        size_hint_y:None
        size: self.texture_size
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}

    MDLabel:
        text: "Statistiques/Record Perso"
        font_name: 'fonts/Poppins-Bold.ttf'
        halign: "center"
        theme_text_color: "Custom"
        color: rgba(0, 57, 119, 255)
        size_hint_y: None
        size: self.texture_size
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}

    MDGridLayout:
        cols: 2
        rows: 4
        row_force_default: True
        row_default_height: '40dp'
        col_force_default: True
        col_default_width: '200dp'
        spacing: '20dp'
        pos_hint: {'center_x': 0.27, 'center_y': 0.35}
        size_hint: None, None
        size: (400, 200)

        MDLabel:
            text: "Pompe"
            theme_text_color: "Custom"
            color: rgba(83, 107, 133, 255)
            font_name: 'fonts/Poppins-Regular.ttf'
            halign: "center"
        MDLabel:
            id: exercice_0_score
            text: "Valeur 1"
            theme_text_color: "Custom"
            color: rgba(83, 107, 133, 255)
            font_name: 'fonts/Poppins-Regular.ttf'
            halign: "center"

        MDLabel:
            text: "Squat"
            theme_text_color: "Custom"
            color: rgba(83, 107, 133, 255)
            font_name: 'fonts/Poppins-Regular.ttf'
            halign: "center"
        MDLabel:
            id: exercice_1_score
            text: "Valeur 2"
            theme_text_color: "Custom"
            color: rgba(83, 107, 133, 255)
            font_name: 'fonts/Poppins-Regular.ttf'
            halign: "center"

        MDLabel:
            text: "Traction"
            theme_text_color: "Custom"
            color: rgba(83, 107, 133, 255)
            font_name: 'fonts/Poppins-Regular.ttf'
            halign: "center"
        MDLabel:
            id: exercice_2_score
            text: "Valeur 3"
            theme_text_color: "Custom"
            color: rgba(83, 107, 133, 255)
            font_name: 'fonts/Poppins-Regular.ttf'
            halign: "center"

        MDLabel:
            text: "???"
            theme_text_color: "Custom"
            color: rgba(83, 107, 133, 255)
            font_name: 'fonts/Poppins-Regular.ttf'
            halign: "center"
        MDLabel:
            id: exercice_3_score
            text: "Valeur 4"
            theme_text_color: "Custom"
            color: rgba(83, 107, 133, 255)
            font_name: 'fonts/Poppins-Regular.ttf'
            halign: "center"

<LadderChooseExerciceScreen>
    name: 'exercice'
    BoxLayout:
        orientation: 'vertical'
        FloatLayout:
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1  # White background
                Rectangle:
                    pos: self.pos
                    size: self.size
                Color:
                    rgba: 0, 0, 0, 1  # Black color for the line
    
            Image:
                id: logo_image
                source: 'assets/pompe.jpg'  # Replace with the actual image path
                size_hint: 0.5, 0.5
                size: dp(100), dp(100)
                pos_hint: {'x': 0.25, 'center_y': 0.85}

            Widget:
                id: side_box
                size_hint: 0.5, 0.15
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1  # Grey color for the frame
                    Line:
                        rectangle: (self.x, self.y, self.width, self.height)
                        width: 1.5
                pos_hint: {'right': 0.75, 'center_y': 0.83}
            
            Image:
                id: logo_image
                source: 'assets/squat.jpg'  # Replace with the actual image path
                size_hint: 0.35, 0.35
                size: dp(100), dp(100)
                pos_hint: {'x': 0.33, 'center_y': 0.63}

            Widget:
                id: side_box
                size_hint: 0.5, 0.15
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1  # Grey color for the frame
                    Line:
                        rectangle: (self.x, self.y, self.width, self.height)
                        width: 1.5
                pos_hint: {'right': 0.75, 'center_y': 0.63}

            Image:
                id: logo_image
                source: 'assets/traction2.jpg'  # Replace with the actual image path
                size_hint: 0.35, 0.35
                size: dp(100), dp(100)
                pos_hint: {'x': 0.33, 'center_y': 0.43}

            Widget:
                id: side_box
                size_hint: 0.5, 0.15
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1  # Grey color for the frame
                    Line:
                        rectangle: (self.x, self.y, self.width, self.height)
                        width: 1.5
                pos_hint: {'right': 0.75, 'center_y': 0.43}

            Image:
                id: logo_image
                source: 'assets/traction2.jpg'  # Replace with the actual image path
                size_hint: 0.35, 0.35
                size: dp(100), dp(100)
                pos_hint: {'x': 0.33, 'center_y': 0.23}

            Widget:
                id: side_box
                size_hint: 0.5, 0.15
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1  # Grey color for the frame
                    Line:
                        rectangle: (self.x, self.y, self.width, self.height)
                        width: 1.5
                pos_hint: {'right': 0.75, 'center_y': 0.23}

            Image:
                source: 'assets/accueil.png'
                size_hint: 0.1, 0.1
                size: dp(100), dp(100)
                pos_hint: {'x': 0.45, 'center_y': 0.95}

    MDFlatButton:
        #Bouton pompe
        text: ""  # Pas de texte, pour simuler un IconButton
        md_bg_color: 0, 0, 0, 0  # Transparent
        size_hint: None, None
        size: "225dp", "110dp"  # Taille du bouton, ajustez selon vos besoins
        pos_hint: {'center_x': 0.5, 'center_y': 0.83}
        on_release: app.show_video_popup("pushUp")
        icon: "arrow-left"  # Définissez l'icône ici si vous utilisez une version de KivyMD qui le supporte, sinon utilisez MDIcon à côté

    MDFlatButton:
        #Bouton squat
        text: ""  # Pas de texte, pour simuler un IconButton
        md_bg_color: 0, 0, 0, 0  # Transparent
        size_hint: None, None
        size: "225dp", "110dp"  # Taille du bouton, ajustez selon vos besoins
        pos_hint: {'center_x': 0.5, 'center_y': 0.63}
        on_release: app.show_video_popup("squat")
        icon: "arrow-left"  # Définissez l'icône ici si vous utilisez une version de KivyMD qui le supporte, sinon utilisez MDIcon à côté

    MDFlatButton:
        #Bouton traction
        text: ""  # Pas de texte, pour simuler un IconButton
        md_bg_color: 0, 0, 0, 0  # Transparent
        size_hint: None, None
        size: "225dp", "110dp"  # Taille du bouton, ajustez selon vos besoins
        pos_hint: {'center_x': 0.5, 'center_y': 0.43}
        on_release: app.show_video_popup("pullUp")
        icon: "arrow-left"  # Définissez l'icône ici si vous utilisez une version de KivyMD qui le supporte, sinon utilisez MDIcon à côté

    MDFlatButton:
        #Bouton squat
        text: ""  # Pas de texte, pour simuler un IconButton
        md_bg_color: 0, 0, 0, 0  # Transparent
        size_hint: None, None
        size: "225dp", "110dp"  # Taille du bouton, ajustez selon vos besoins
        pos_hint: {'center_x': 0.5, 'center_y': 0.23}
        on_release: app.show_video_popup("traction2")
        icon: "arrow-left"  # Définissez l'icône ici si vous utilisez une version de KivyMD qui le supporte, sinon utilisez MDIcon à côté

    BoxLayout:
        orientation: 'horizontal'
        adaptive_size: True
        size_hint: 1, 0.1
        height: dp(100)  # Hauteur des boutons

        MDRectangleFlatIconButton:
            icon: "assets/accueil.png"
            adaptive_size: True
            size_hint: 0.9, 0.9
            text: "  Home"
            line_color: "black"
            font_size: "24sp"
            icon_size: "36dp"
            halign: "center"
            theme_text_color: "Custom"
            color: rgba(0, 57, 119, 255)
            on_release:
                root.manager.transition.direction = 'left'  
                root.manager.current = 'exercice'

        MDRectangleFlatIconButton:
            icon: "assets/couronne.png"
            adaptive_size: True
            size_hint: 0.9, 0.9
            text: "  Ranking"
            line_color: "black"
            font_size: "24sp"
            icon_size: "36dp"
            halign: "center"
            theme_text_color: "Custom"
            color: rgba(0, 57, 119, 255)
            on_release:
                root.manager.transition.direction = 'left' 
                root.manager.current = 'ranking'

        MDRectangleFlatIconButton:
            icon: "assets/utilisateur.png"
            adaptive_size: True
            size_hint: 0.9, 0.9
            text: "  Profile"
            line_color: "black"
            font_size: "24sp"
            icon_size: "36dp"
            halign: "center"
            theme_text_color: "Custom"
            color: rgba(0, 57, 119, 255)
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'profile'
                app.on_profile_enter()

<VideoScreen>:
    name: 'video'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height

                VideoPlayer:
                    id: video_player
                    source: ''
                    state: 'stop'
                    size_hint_y: None
                    height: dp(400)
                    pos_hint: {'center_x': 0.5}
                    opacity: 1  # Make it visible once a video is selected
                
                Image:
                    id: plot_image
                    source: 'assets/plot.png'  # Path to the plot image
                    size_hint_y: None
                    size: dp(200), dp(200)
                    pos_hint: {'center_x': 0.5}   
                
                Image:
                    id: plot_integrity
                    source: 'assets/plot_integrity.png'  # Path to the plot image
                    size_hint_y: None
                    size: dp(200), dp(200)
                    pos_hint: {'center_x': 0.5}   

                MDLabel:
                    id: score_label
                    text: "S C O R E"
                    size_hint_y: None
                    font_size: '30sp'
                    haligh: 'center'
                    color: rgba(0, 57, 119, 255)
                    pos_hint: {'center_x': 0.75}

        MDIconButton:
            icon: "arrow-left"
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {'center_x': 0.5, 'y': 0.01}
            on_release: 
                app.root.current = 'exercice'
                root.manager.transition.direction = 'right'

<VideoPopup>:
    title: "Choose a video"
    size_hint: .9, .9
    BoxLayout:
        orientation: 'vertical'
        FileChooserListView:
            id: filechooser
            on_selection: app.load_video(self.selection)

        MDRaisedButton:
            text: "Close"
            size_hint: 1, None
            height: "48dp"
            on_release: root.dismiss()

<ProfilePhotoPopup>:
    title: "Choose a photo"
    size_hint: .9, .9
    BoxLayout:
        orientation: 'vertical'
        FileChooserListView:
            id: filechooser
            on_selection: app.load_image(self.selection)

        MDRaisedButton:
            text: "Close"
            size_hint: 1, None
            height: "48dp"
            on_release: root.dismiss()

<RankingScreen>
    name: 'ranking'
    BoxLayout:
        orientation: 'vertical'
        FloatLayout:
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1  # White background
                Rectangle:
                    pos: self.pos
                    size: self.size
                Color:
                    rgba: 0, 0, 0, 1  # Black color for the line

            Image:
                id: logo_image
                source: 'assets/pompe.jpg'  # Replace with the actual image path
                size_hint: 0.5, 0.5
                size: dp(100), dp(100)
                pos_hint: {'x': 0.25, 'center_y': 0.85}

            Widget:
                id: side_box
                size_hint: 0.5, 0.15
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1  # Grey color for the frame
                    Line:
                        rectangle: (self.x, self.y, self.width, self.height)
                        width: 1.5
                pos_hint: {'right': 0.75, 'center_y': 0.83}
            
            Image:
                id: logo_image
                source: 'assets/squat.jpg'  # Replace with the actual image path
                size_hint: 0.35, 0.35
                size: dp(100), dp(100)
                pos_hint: {'x': 0.33, 'center_y': 0.63}

            Widget:
                id: side_box
                size_hint: 0.5, 0.15
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1  # Grey color for the frame
                    Line:
                        rectangle: (self.x, self.y, self.width, self.height)
                        width: 1.5
                pos_hint: {'right': 0.75, 'center_y': 0.63}

            Image:
                id: logo_image
                source: 'assets/traction2.jpg'  # Replace with the actual image path
                size_hint: 0.35, 0.35
                size: dp(100), dp(100)
                pos_hint: {'x': 0.33, 'center_y': 0.43}

            Widget:
                id: side_box
                size_hint: 0.5, 0.15
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1  # Grey color for the frame
                    Line:
                        rectangle: (self.x, self.y, self.width, self.height)
                        width: 1.5
                pos_hint: {'right': 0.75, 'center_y': 0.43}

            Image:
                id: logo_image
                source: 'assets/traction2.jpg'  # Replace with the actual image path
                size_hint: 0.35, 0.35
                size: dp(100), dp(100)
                pos_hint: {'x': 0.33, 'center_y': 0.23}

            Widget:
                id: side_box
                size_hint: 0.5, 0.15
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1  # Grey color for the frame
                    Line:
                        rectangle: (self.x, self.y, self.width, self.height)
                        width: 1.5
                pos_hint: {'right': 0.75, 'center_y': 0.23}

            Image:
                source: 'assets/couronne.png'
                size_hint: 0.1, 0.1
                size: dp(100), dp(100)
                pos_hint: {'x': 0.45, 'center_y': 0.95}

    MDFlatButton:
        #Bouton pompe
        text: ""  # Pas de texte, pour simuler un IconButton
        md_bg_color: 0, 0, 0, 0  # Transparent
        size_hint: None, None
        size: "225dp", "110dp"  # Taille du bouton, ajustez selon vos besoins
        pos_hint: {'center_x': 0.5, 'center_y': 0.83}
        on_release:
            root.manager.current = 'rankingpompe'
            root.manager.transition.direction = 'up'
        icon: "arrow-left"  # Définissez l'icône ici si vous utilisez une version de KivyMD qui le supporte, sinon utilisez MDIcon à côté

    MDFlatButton:
        #Bouton squat
        text: ""  # Pas de texte, pour simuler un IconButton
        md_bg_color: 0, 0, 0, 0  # Transparent
        size_hint: None, None
        size: "225dp", "110dp"  # Taille du bouton, ajustez selon vos besoins
        pos_hint: {'center_x': 0.5, 'center_y': 0.63}
        on_release: 
            root.manager.current = 'rankingpompe'
            root.manager.transition.direction = 'up'
        icon: "arrow-left"  # Définissez l'icône ici si vous utilisez une version de KivyMD qui le supporte, sinon utilisez MDIcon à côté

    MDFlatButton:
        #Bouton squat
        text: ""  # Pas de texte, pour simuler un IconButton
        md_bg_color: 0, 0, 0, 0  # Transparent
        size_hint: None, None
        size: "225dp", "110dp"  # Taille du bouton, ajustez selon vos besoins
        pos_hint: {'center_x': 0.5, 'center_y': 0.43}
        on_release:
            root.manager.current = 'rankingpompe'
            root.manager.transition.direction = 'up'
        icon: "arrow-left"  # Définissez l'icône ici si vous utilisez une version de KivyMD qui le supporte, sinon utilisez MDIcon à côté

    MDFlatButton:
        #Bouton squat
        text: ""  # Pas de texte, pour simuler un IconButton
        md_bg_color: 0, 0, 0, 0  # Transparent
        size_hint: None, None
        size: "225dp", "110dp"  # Taille du bouton, ajustez selon vos besoins
        pos_hint: {'center_x': 0.5, 'center_y': 0.23}
        on_release:
            root.manager.current = 'rankingpompe'
            root.manager.transition.direction = 'up'
        icon: "arrow-left"  # Définissez l'icône ici si vous utilisez une version de KivyMD qui le supporte, sinon utilisez MDIcon à côté
    
    BoxLayout:
        orientation: 'horizontal'
        adaptive_size: True
        size_hint: 1, 0.1
        height: dp(100)  # Hauteur des boutons

        MDRectangleFlatIconButton:
            icon: "assets/accueil.png"
            adaptive_size: True
            size_hint: 0.9, 0.9
            text: "  Home"
            line_color: "black"
            font_size: "24sp"
            icon_size: "36dp"
            halign: "center"
            theme_text_color: "Custom"
            color: rgba(0, 57, 119, 255)
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'exercice'

        MDRectangleFlatIconButton:
            icon: "assets/couronne.png"
            adaptive_size: True
            size_hint: 0.9, 0.9
            text: "  Ranking"
            line_color: "black"
            font_size: "24sp"
            icon_size: "36dp"
            halign: "center"
            theme_text_color: "Custom"
            color: rgba(0, 57, 119, 255)
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'ranking'

        MDRectangleFlatIconButton:
            icon: "assets/utilisateur.png"
            adaptive_size: True
            size_hint: 0.9, 0.9
            text: "  Profile"
            line_color: "black"
            font_size: "24sp"
            icon_size: "36dp"
            halign: "center"
            theme_text_color: "Custom"
            color: rgba(0, 57, 119, 255)
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'profile'
                app.on_profile_enter()
            
<RankingPompeScreen>
    name: 'rankingpompe'
    BoxLayout:
        orientation: 'vertical'
        FloatLayout:
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1  # White background
                Rectangle:
                    pos: self.pos
                    size: self.size
                Color:
                    rgba: 0, 0, 0, 1  # Black color for the line

            Image:
                id: logo_image
                source: 'assets/pompe.jpg'  # Replace with the actual image path
                size_hint: 0.5, 0.5
                size: dp(100), dp(100)
                pos_hint: {'x': 0.25, 'center_y': 0.85}

            Widget:
                id: side_box
                size_hint: 0.5, 0.15
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1  # Grey color for the frame
                    Line:
                        rectangle: (self.x, self.y, self.width, self.height)
                        width: 1.5
                pos_hint: {'right': 0.75, 'center_y': 0.83}

            Label:
                id: side_box_label
                text: "Push Ups Ranking"
                font_size: '19sp'
                color: rgba(0, 57, 119, 255)
                size_hint: 0.6, 0.1
                pos_hint: {'right': 0.795, 'top': 0.77}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Label:
                id: top1_pompe_name
                text: "RyuKaSa"
                font_size: '18sp'
                color: 1, 0.8, 0, 1  # Gold text
                size_hint: 0.6, 0.1
                pos_hint: {'right': 0.6, 'top': 0.7}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Label:
                id: top1_pompe_score
                text: "928"
                font_size: '18sp'
                color: 1, 0.8, 0, 1
                size_hint: 0.6, 0.1
                pos_hint: {'right': 1, 'top': 0.7}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Label:
                id: top2_pompe_name
                text: "ruuskovito"
                font_size: '18sp'
                color: 0.75, 0.75, 0.83, 1  # Silver text
                size_hint: 0.6, 0.1
                pos_hint: {'right': 0.6, 'top': 0.6}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Label:
                id: top2_pompe_score
                text: "900"
                font_size: '18sp'
                color: 0.75, 0.75, 0.83, 1
                size_hint: 0.6, 0.1
                pos_hint: {'right': 1, 'top': 0.6}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible
   
            Label:
                id: top3_pompe_name
                text: "Atuu"
                font_size: '18sp'
                color: 0.8, 0.5, 0.2, 1  # Bronze text
                size_hint: 0.6, 0.1
                pos_hint: {'right': 0.6, 'top': 0.5}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Label:
                id: top3_pompe_score
                text: "858"
                font_size: '18sp'
                color: 0.8, 0.5, 0.2, 1  # Bronze text
                size_hint: 0.6, 0.1
                pos_hint: {'right': 1, 'top': 0.5}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Label:
                id: top4_pompe_name
                text: "nyce"
                font_size: '18sp'
                color: rgba(0, 57, 119, 255)
                size_hint: 0.6, 0.1
                pos_hint: {'right': 0.6, 'top': 0.4}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Label:
                id: top4_pompe_score
                text: "819"
                font_size: '18sp'
                color: rgba(0, 57, 119, 255)
                size_hint: 0.6, 0.1
                pos_hint: {'right': 1, 'top': 0.4}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Label:
                id: top5_pompe_name
                text: "Hyckare"
                font_size: '18sp'
                color: rgba(0, 57, 119, 255)
                size_hint: 0.6, 0.1
                pos_hint: {'right': 0.6, 'top': 0.3}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Label:
                id: top5_pompe_score
                text: "789"
                font_size: '18sp'
                color: rgba(0, 57, 119, 255)
                size_hint: 0.6, 0.1
                pos_hint: {'right': 1, 'top': 0.3}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Label:
                id: top6_pompe_name
                text: "AzRedFire"
                font_size: '18sp'
                color: rgba(0, 57, 119, 255)
                size_hint: 0.6, 0.1
                pos_hint: {'right': 0.6, 'top': 0.2}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Label:
                id: top6_pompe_score
                text: "769"
                font_size: '18sp'
                color: rgba(0, 57, 119, 255)
                size_hint: 0.6, 0.1
                pos_hint: {'right': 1, 'top': 0.2}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            MDIconButton:
                icon:"arrow-down"
                pos_hint: {"center_y":.95}
                user_font_size: "20sp"
                theme_text_color: "Primary"
                on_press:
                    root.manager.transition.direction = 'down'
                    root.manager.current = 'ranking'
"""