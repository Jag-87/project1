import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Rectangle



class LoginScreen(FloatLayout):

	def callback(instance,value):
		print('pressed')

	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Image(
			source='nini.gif',
			size=(.1, .1)))
		self.add_widget(Label(
			text='[size=20][b][color=3333ff]User Name[/color][/b][/size]',
			markup=True,
			size_hint=(.2, .2),
			pos_hint={'center_x': .4,'center_y': .6}))
		self.username = TextInput(
			multiline=False,
			size_hint=(.2, .1),
			pos_hint={'center_x': .6, 'center_y': .6})
		self.add_widget(self.username)
		self.add_widget(Label(
			text='[size=20][b][color=3333ff]Password[/color][/b][/size]',
			markup=True,
			size_hint=(.2, .2),
			pos_hint={'center_x': .4, 'center_y': .4}))
		self.password = TextInput(
			password=True,
			multiline=False,
			size_hint=(.2, .1),
			pos_hint={'center_x': .6, 'center_y': .4})
		self.add_widget(self.password)
		self.button = Button(
			text='Login',
			size_hint=(.2, .1),
			pos_hint={'center_x': .6, 'center_y': .2})
		self.add_widget(self.button)
		self.button.bind(on_press=self.callback)



class MyApp(App):
	def build(self):
		self.root = root = LoginScreen()
		return root


if __name__ == '__main__':
	MyApp().run()
