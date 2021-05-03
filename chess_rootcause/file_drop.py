from kivy.app import App
from kivy.core.window import Window
import kivy.uix.dropdown
import kivy.uix.button
import kivy.uix.boxlayout
import kivy.uix.label
import kivy.uix.popup
import kivy.base
import os
import json
import helpers as hlp
import shutil


class WindowFileDropApp(App):

    def build(self):
        self.json_dict = {}
        Window.bind(on_dropfile=self._on_file_drop, on_request_close=self.on_request_close)
        return None

    def get_inputs(self):
        with open(os.path.join('inputs', 'inputs.json')) as f:
            input_dict = json.load(f)
        return input_dict

    def on_request_close(self, *args):
        self.textpopup(title='Exit', text='Are you sure?')
        return True

    def textpopup(self, title='', text=''):
        """Open the pop-up with the name.

        :param title: title of the pop-up to open
        :type title: str
        :param text: main text of the pop-up to open
        :type text: str
        :rtype: None
        """

        box = kivy.uix.boxlayout.BoxLayout(orientation='vertical')
        box.add_widget(kivy.uix.label.Label(text=text))
        mybutton = kivy.uix.button.Button(text='OK', size_hint=(1, 0.25))
        box.add_widget(mybutton)
        popup = kivy.uix.popup.Popup(title=title, content=box, size_hint=(None, None), size=(600, 300))
        mybutton.bind(on_release=self.stop)
        popup.open()

    def _on_file_drop(self, window, file_path):
        self.textpopup(title='loaded file', text=str(str(file_path) + 'loaded'))

        with open(file_path) as temp_file:
            pgn_dict = hlp.parse_pgn(temp_file)

        file_name = os.path.basename(file_path).decode('utf-8')
        dir_name = os.path.dirname(file_path).decode('utf-8')
        target = os.path.join(dir_name, 'coded', file_name)
        shutil.move(file_path, target)
        self.json_dict = pgn_dict
        return None


