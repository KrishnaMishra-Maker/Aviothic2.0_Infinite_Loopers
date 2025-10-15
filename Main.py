from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.clearcolor = (1, 0.95, 0.8, 1)  # full background color 
#Ui Ux by Harshit
class Login(Screen):
    def __init__(self, **k):
        super().__init__(**k)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        layout.add_widget(Label(text="Lost & Found App", font_size=28, color=(0.1,0.2,0.5,1)))
        self.user_input = TextInput(hint_text="Enter Name", size_hint=(1,0.2))
        self.id_input = TextInput(hint_text="Enter AFN", size_hint=(1,0.2))
        login_btn = Button(text="Login", size_hint=(1,0.25), background_color=(0.2,0.6,1,1))
        login_btn.bind(on_press=self.login)
        for w in [self.user_input, self.id_input, login_btn]:
            layout.add_widget(w)
        self.add_widget(layout)

    def login(self, instance):
        if self.user_input.text and self.id_input.text:
            self.manager.get_screen("home").welcome_user(self.user_input.text)
            self.manager.current = "home"
# Backend By Krishna 
class Home(Screen):
    def __init__(self, **k):
        super().__init__(**k)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        self.welcome_label = Label(text="", font_size=22)
        report_btn = Button(text="Report Lost Item", background_color=(1,0.6,0.5,1))
        view_btn = Button(text="View Found Items", background_color=(0.5,1,0.6,1))
        report_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'lost'))
        view_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'found'))
        for w in [self.welcome_label, report_btn, view_btn]:
            layout.add_widget(w)
        self.add_widget(layout)

    def welcome_user(self, name):
        self.welcome_label.text = f"Welcome, {name}!"
# Frontend By Nishant
class Lost(Screen):
    def __init__(self, **k):
        super().__init__(**k)
        layout = BoxLayout(orientation='vertical', padding=30)
        layout.add_widget(Label(text="Report Lost Item", font_size=22))
        back_btn = Button(text="Back", background_color=(0.8,0.8,0.8,1))
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'home'))
        layout.add_widget(back_btn)
        self.add_widget(layout)

class Found(Screen):
    def __init__(self, **k):
        super().__init__(**k)
        layout = BoxLayout(orientation='vertical', padding=30)
        layout.add_widget(Label(text="Found Items", font_size=22))
        back_btn = Button(text="Back", background_color=(0.8,0.8,0.8,1))
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'home'))
        layout.add_widget(back_btn)
        self.add_widget(layout)

class LostFoundApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Login(name="login"))
        sm.add_widget(Home(name="home"))
        sm.add_widget(Lost(name="lost"))
        sm.add_widget(Found(name="found"))
        return sm

LostFoundApp().run()
