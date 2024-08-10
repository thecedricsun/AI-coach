<VideoScreen>:
    name: 'video'
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

            VideoPlayer:
                id: video_player
                source: ''
                state: 'stop'
                size_hint: 1, 0.5
                pos_hint: {'x': 0, 'top': 1}
                opacity: 1  # Make it visible once a video is selected

            Image:
                id: logo_image
                source: 'assets/coach.png'  # Replace with the actual image path
                size_hint: 0.2, 0.2
                size: dp(100), dp(100)
                pos_hint: {'x': 0.05, 'center_y': 0.25}

            Label:
                id: side_box_label
                text: "Les conseils du coach"
                font_size: '18sp'
                color: 0, 0, 0, 1  # Black text
                size_hint: 0.6, 0.1
                pos_hint: {'right': 0.9, 'top': 0.48}
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0  # Transparent background, only outline is visible

            Widget:
                id: side_box
                size_hint: 0.6, 0.4
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1  # Grey color for the frame
                    Line:
                        rectangle: (self.x, self.y, self.width, self.height)
                        width: 1.5
                pos_hint: {'right': 0.9, 'center_y': 0.25}

        Image:
            id: plot_image
            source: 'assets/plot.png'  # Path to the plot image
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
            
        MDIconButton:
            icon: "arrow-left"
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {'center_x': 0.5, 'y': 0.01}
            on_release: app.root.current = 'exercice'
