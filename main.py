from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import AsyncImage
from kivymd.uix.list import OneLineListItem


###############################
#        size_hint: None, None
#        size: dp(500), dp(500)
##############################

KV="""
<DrawerClickableItem@MDNavigationDrawerItem>
<DrawerLabelItem@MDNavigationDrawerItem>
ScreenManager:
    FirstScreen:
    SecoundScreen:
<FirstScreen>:
    name:"First"
    AsyncImage:
        source:'kali.pn'
    ScrollView:
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            padding: dp(10)
            spacing: dp(10)
            MDBoxLayout:
                ad$ pkgive_height: True
                Label:
                    text: 'Item 1'
                    halign: 'center'
                    valign: 'center'
                    size_hint_y: None
                    height: dp(56)
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    canvas.before:
                        Color:
                            rgba: 0, 1, 0, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
            MDBoxLayout:
                ad$ pkgive_height: True
                OneLineListItem:
                    text: '                     Termux Setup'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bg_color: 0, 1, 0, 1
                    on_press:root.manager.current="Secound"
            MDBoxLayout:
                ad$ pkgive_height: True
                OneLineListItem:
                    text: '                    Storm-Breaker'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bg_color: 0, 1, 0, 1
                    on_press:root.manager.current="Secound"
            MDBoxLayout:
                ad$ pkgive_height: True
                OneLineListItem:
                    text: '                    CCTV HAck'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bg_color: 0, 1, 0, 1
                    on_press:root.manager.current="Secound"
            MDBoxLayout:
                ad$ pkgive_height: True
                OneLineListItem:
                    text: '                    I-Tracker'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bg_color: 0, 1, 0, 1
                    on_press:root.manager.current="Secound"
            MDBoxLayout:
                ad$ pkgive_height: True
                OneLineListItem:
                    text: '                    DDos_WEB'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bg_color: 0, 1, 0, 1
                    on_press:root.manager.current="Secound"
            MDBoxLayout:
                ad$ pkgive_height: True
                OneLineListItem:
                    text: '                    CamHacker'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bg_color: 0, 1, 0, 1
                    on_press:root.manager.current="Secound"
            MDBoxLayout:
                ad$ pkgive_height: True
                OneLineListItem:
                    text: '                    seeker'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bg_color: 0, 1, 0, 1
                    on_press:root.manager.current="Secound"
            MDBoxLayout:
                ad$ pkgive_height: True
                OneLineListItem:
                    text: '                    PyPhisher'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bg_color: 0, 1, 0, 1
                    on_press:root.manager.current="Secound"
            MDBoxLayout:
                ad$ pkgive_height: True
                OneLineListItem:
                    text: '                    Zphisher'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bg_color: 0, 1, 0, 1
                    on_press:root.manager.current="Secound"
            MDBoxLayout:
                ad$ pkgive_height: True
                OneLineListItem:
                    text: '                    Toll-X'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bg_color: 0, 1, 0, 1
                    on_press:root.manager.current="Secound"
            MDBoxLayout:
                ad$ pkgive_height: True
                OneLineListItem:
                    text: '                    Facebook-Brute'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bg_color: 0, 1, 0, 1
                    on_press:root.manager.current="Secound"

    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                MDScreen:
                    MDTopAppBar:
                        title:"Hacker Tool"
                        elivation:4
                        pos_hint:{"top":1}
                        left_action_items:[["menu", lambda x:nav_drawer.set_state("open")]]
            MDNavigationDrawer:
                id:nav_drawer

                MDNavigationDrawerMenu:
                    MDNavigationDrawerHeader:
                        title:"Hacker Tool"
                        text:"By RAzahamed"
                        spacing:"4dp"
                        padding:"1dp",0,0,"3dp"
                    MDNavigationDrawerLabel:
                        text:"MENU"  
                    DrawerClickableItem:
                        icon:"email"
                        text:"Email"
                    DrawerClickableItem:
                        icon:"youtube"
                        text:"Youtube"
                    DrawerClickableItem:
                        icon:"facebook"
                        text:"Facebook"
                    DrawerClickableItem:
                        icon:"github"
                        text:"Github"
                    DrawerClickableItem:
                        icon:"share-variant"
                        text:"Share App"
                        on_press:"https://kivymd.readthedocs.io/en/0.104.1/components/image-list/index.html"
                    DrawerClickableItem:
                        icon:"more"
                        text:"More App"
                    MDNavigationDrawerLabel:
                        text:"All"
<SecoundScreen>:
    name:"Secound"
    MDLabel:
        text:"Setup Termux"
        pos_hint: {"x": 0.4, "y": 0.4}
    MDIconButton:
        icon: "backburger"
        size_hint: None, None
        size: dp(5000), dp(5)       
        pos_hint:{"center_x":0.1, "center_y":0.9}
        on_press:root.manager.current="First"
"""
class FirstScreen(Screen):
    pass
class SecoundScreen(Screen):
    pass
class ScreenmangerApp(MDApp):
    def build(self):
        blder=Builder.load_string(KV)
        return blder
    
ScreenmangerApp().run()