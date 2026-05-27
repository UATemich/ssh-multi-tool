from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel


class SSHTool(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"

        screen = MDScreen()

        label = MDLabel(
            text="SSH Multi-Tool",
            halign="center"
        )

        screen.add_widget(label)

        return screen


SSHTool().run()
