import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget

class player_init(GridLayout):
  def __init__(self, **kwargs):
    super(player_init, self).__init__(**kwargs)
    
    self.cols = 1
    self.top_grid = GridLayout(cols = 1, 
                               size_hint_y = None, 
                               height = 230
                               )
    
    self.top_grid.add_widget(Label(text = "Number of players: ", 
                                   font_size = 75, 
                                   size_hint_y = None, 
                                   height = 200
                                   ))
    
    self.number = TextInput(multiline = False, 
                            input_filter = 'int', 
                            size_hint = (None, None), 
                            size = (200, 30)
                            )
    self.top_grid.add_widget(self.number)
    self.add_widget(self.top_grid)
    
    self.numpad = GridLayout(cols = 3, 
                             rows = 4, 
                             size_hint = (None, None), 
                             size = (200, 260), 
                             spacing = 0, 
                             padding = 5
                             )
    
    self.buttons = {}
    for digit in range(1, 10):
      btn = Button(text = str(digit), 
                   font_size = 32, 
                   size_hint = (None, None), 
                   size = (60, 60)
                   )
      btn.bind(on_press = self.press)
      self.buttons[digit] = btn
      self.numpad.add_widget(btn)
    
    btn0 = Button(text = "0", 
                  font_size = 32, 
                  size_hint = (None, None), 
                  size = (60, 60)
                  )
    btn0.bind(on_press = self.press)
    self.buttons[0] = btn0
    self.numpad.add_widget(btn0)
    
    self.numpad.add_widget(Widget(size_hint = (None, None), size = (60, 60)))
    
    self.submit = Button(text = "Enter", 
                         font_size = 32, 
                         size_hint = (None, None), 
                         size = (60, 60)
                         )
    self.submit.bind(on_press = self.press)
    self.numpad.add_widget(self.submit)
    
    self.add_widget(self.numpad)
  
  def press(self, instance):
    for digit, btn in self.buttons.items():
      if instance == btn:
        self.number.text += str(digit)
        return
    
    if instance == self.submit:
      self.number.text = ""

class main(App):
  def build(self):
    root = AnchorLayout()
    player_widget = player_init(size_hint = (None, None))
    player_widget.width = 220
    player_widget.height = 400
    root.add_widget(player_widget)
    return root

if __name__ == '__main__':
  main().run()