from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.clearcolor = (0.1 ,0.1 ,0.1 ,1)
class MyApp(App):
    def build(self):
        layout = FloatLayout()
        #img
        img_black=Image(source='black.jpg', pos_hint={'center_x':0.5, 'center_y':0.85}, size_hint=(None, 9), width=908)
        img_black1=Image(source='black.jpg', pos_hint={'center_x':0.2, 'center_y':0.85}, size_hint=(None, 9), width=908)
        img_black2=Image(source='black.jpg', pos_hint={'center_x':0.6, 'center_y':0.85}, size_hint=(None, 9), width=908)
        img_black3=Image(source='black.jpg', pos_hint={'center_x':0.5, 'center_y':0.71}, size_hint=(None, 9), width=908)
        img_black4=Image(source='black.jpg', pos_hint={'center_x':0.2, 'center_y':0.71}, size_hint=(None, 9), width=908)
        img_black5=Image(source='black.jpg', pos_hint={'center_x':0.6, 'center_y':0.71}, size_hint=(None, 9), width=908)
        #text
        text=Label(text='Calculator', pos_hint={'center_x':0.2, 'center_y':0.95}, color=(0,1,1,1), font_size=35)
        text2=Label(text='___________', pos_hint={'center_x':0.2, 'center_y':0.94}, color=(0,1,1,1), font_size=30)
        #text_input
        self.text_input=TextInput(text='  ', size_hint=(None, 0.3), width=628, pos_hint={'center_x':0.5, 'center_y':0.7}, readonly=True, font_size=75, background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1))
        #button123
        button_0 = Button(text='0', size_hint=(None, None), width=100, pos_hint={'center_x': 0.2, 'center_y': 0.1}, on_press=self.on_press_button_0, background_color=(1,1,1,1), font_size=65, background_normal='background.jpg')
        button_00 = Button(text='00', size_hint=(None, None), width=100, pos_hint={'center_x': 0.4, 'center_y': 0.1}, on_press=self.on_press_button_00, font_size=65, background_normal='background.jpg')
        button_dot = Button(text='.', size_hint=(None, None), width=100, pos_hint={'center_x': 0.6, 'center_y': 0.1}, on_press=self.on_press_button_dot, font_size=65, background_normal='background.jpg')
        button_1 = Button(text='1', size_hint=(None, None), width=100, pos_hint={'center_x': 0.2, 'center_y': 0.2}, on_press=self.on_press_button_1, background_color=(1,1,1,1), font_size=65, background_normal='background.jpg')
        button_2 = Button(text='2', size_hint=(None, None), width=100, pos_hint={'center_x': 0.4, 'center_y': 0.2}, on_press=self.on_press_button_2, font_size=65, background_normal='background.jpg')
        button_3 = Button(text='3', size_hint=(None, None), width=100, pos_hint={'center_x': 0.6, 'center_y': 0.2}, on_press=self.on_press_button_3, font_size=65, background_normal='background.jpg')
        button_4 = Button(text='4', size_hint=(None, None), width=100, pos_hint={'center_x': 0.2, 'center_y': 0.3}, on_press=self.on_press_button_4, font_size=65, background_normal='background.jpg')
        button_5 = Button(text='5', size_hint=(None, None), width=100, pos_hint={'center_x': 0.4, 'center_y': 0.3}, on_press=self.on_press_button_5, font_size=65, background_normal='background.jpg')
        button_6 = Button(text='6', size_hint=(None, None), width=100, pos_hint={'center_x': 0.6, 'center_y': 0.3}, on_press=self.on_press_button_6, font_size=65, background_normal='background.jpg')
        button_7 = Button(text='7', size_hint=(None, None), width=100, pos_hint={'center_x': 0.2, 'center_y': 0.4}, on_press=self.on_press_button_7, font_size=65, background_normal='background.jpg')
        button_8 = Button(text='8', size_hint=(None, None), width=100, pos_hint={'center_x': 0.4, 'center_y': 0.4}, on_press=self.on_press_button_8, font_size=65, background_normal='background.jpg')
        button_9 = Button(text='9', size_hint=(None, None), width=100, pos_hint={'center_x': 0.6, 'center_y': 0.4}, on_press=self.on_press_button_9, font_size=65, background_normal='background.jpg')
        #+-*%%
        button_add = Button(text='+', size_hint=(None, None), width=100, pos_hint={'center_x': 0.9, 'center_y': 0.2}, on_press=self.on_press_button_add, font_size=90, background_normal='background.jpg', color='cyan')
        button_minus = Button(text='-', size_hint=(None, None), width=100, pos_hint={'center_x': 0.9, 'center_y': 0.3}, on_press=self.on_press_button_minus, font_size=120, background_normal='background.jpg', color='cyan')
        button_times = Button(text='x', size_hint=(None, None), width=100, pos_hint={'center_x': 0.9, 'center_y': 0.4}, on_press=self.on_press_button_times, font_size=80, background_normal='background.jpg', color='cyan')
        button_share = Button(text='', size_hint=(None, None), width=110, pos_hint={'center_x': 0.9, 'center_y': 0.5}, on_press=self.on_press_button_share, font_size=80, background_normal='share.png', color='cyan')
        button_back = Button(text='', size_hint=(None, 0.055), width=110, pos_hint={'center_x': 0.6, 'center_y': 0.5}, on_press=self.on_press_button_back, font_size=80, background_normal='back.png', color='cyan')
        button_div100 = Button(text='%', size_hint=(None, None), width=100, pos_hint={'center_x': 0.4, 'center_y': 0.5}, on_press=self.on_press_button_div100, font_size=65, background_normal='background.jpg', color='cyan')
        button_C = Button(text='C', size_hint=(None, None), width=100, pos_hint={'center_x': 0.2, 'center_y': 0.5}, on_press=self.on_press_button_C, font_size=65, background_normal='background.jpg', color='cyan')
        button_soman = Button(text='=', size_hint=(None, None), width=100, pos_hint={'center_x': 0.9, 'center_y': 0.1}, on_press=self.on_press_button_soman, font_size=100, background_normal='background.jpg', color='cyan')
        #layout.add
        #img add layout
        layout.add_widget(img_black)
        layout.add_widget(img_black1)
        layout.add_widget(img_black2)
        layout.add_widget(img_black3)
        layout.add_widget(img_black4)
        layout.add_widget(img_black5)
        #text add layout
        layout.add_widget(text)
        layout.add_widget(text2)
        #text add button
        layout.add_widget(button_0)
        layout.add_widget(button_00)
        layout.add_widget(button_dot)
        layout.add_widget(button_1)
        layout.add_widget(button_2)
        layout.add_widget(button_3)
        layout.add_widget(button_4)
        layout.add_widget(button_5)
        layout.add_widget(button_6)
        layout.add_widget(button_7)
        layout.add_widget(button_8)
        layout.add_widget(button_9)
        layout.add_widget(button_add)
        layout.add_widget(button_soman)
        layout.add_widget(button_minus)
        layout.add_widget(button_times)
        layout.add_widget(button_share)
        layout.add_widget(button_back)
        layout.add_widget(button_div100)
        layout.add_widget(button_C)
        layout.add_widget(self.text_input)
        return layout
#button clcik
    def on_press_button_00(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_dot(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_1(self, instance):
        self.text_input.text += instance.text
    def on_press_button_2(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_3(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_4(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_5(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_6(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_0(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_minus(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_7(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_8(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_9(self, instance):
    	self.text_input.text += instance.text
    def on_press_button_times(self, instance):
    	self.text_input.text += 'x'
    def on_press_button_share(self, instance):
    	self.text_input.text += '/'
    def on_press_button_back(self, instance):
    	self.text_input.text = self.text_input.text[:-1]
    def on_press_button_C(self, instance):
    	self.text_input.text = ''
    def on_press_button_div100(self, instance):
    	self.text_input.text += '%'  
    #button work end
    def on_press_button_soman(self, instance):
	    try:
	        if 'x' in self.text_input.text:
                    self.text_input.text = self.text_input.text.replace('x', '*')
	        elif '%' in self.text_input.text:
                    self.text_input.text = self.text_input.text.replace('%', '/100')
	        result = eval(self.text_input.text)
	        self.text_input.text = str(result)  	    
	    except:
	        self.text_input.text = 'Math Error'
    def on_press_button_add(self, instance):
    	self.text_input.text += instance.text	 

MyApp().run()
