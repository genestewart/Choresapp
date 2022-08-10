from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window


Window.size = (300, 500)


screen_helper = """
ScreenManager:
    StartScreen:
    UserLoginScreen:
    MainScreen:


<StartScreen>:
    name: 'Start'
    MDFillRoundFlatButton:
        text: 'User'
        font_size: 15
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'UserLogin'
    
<UserLoginScreen>:
    name: 'UserLogin'
    MDCard:
        size_hint: None, None
        size: 300, 450
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 65
        spacing: 35
        orientation: 'vertical'
        MDIcon:
            icon: 'account'
            icon_color: 204/255.0, 102/255.0, 0/255.0, 255/255.0
            halign: 'center'
            font_size: 180
        MDTextFieldRound:
            id: user
            icon_left: "account-check"
            hint_text: "Username"
            foreground_color: 0, 0, 0, 1
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
        MDTextFieldRound:
            id: password
            icon_left: "key-variant"
            hint_text: "Password"
            foreground_color: 0, 0, 0, 1
            size_hint_x: None
            width: 220
            font_size: 20            
            pos_hint: {"center_x": 0.5}
            password: True    
        MDFillRoundFlatButton:
            text: "LOG IN"
            font_size: 15
            pos_hint: {"center_x": 0.5}
            on_press: root.manager.current = 'Main'

<MainScreen>:
    name: 'Main'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Chores'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                            elevation: 10
                        Widget:
            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    MDLabel:
                        text: 'User'
                        font_style: 'Subtitle1'
                    MDLabel:
                        text: 'email@email.com'
                        font_style: 'Caption'
                    ScrollView:

"""


class StartScreen(Screen):
    pass


class UserLoginScreen(Screen):
    pass


class MainScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(StartScreen(name='Start'))
sm.add_widget(UserLoginScreen(name='UserLogin'))
sm.add_widget(MainScreen(name='Main'))


class ChoreApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


ChoreApp().run()
