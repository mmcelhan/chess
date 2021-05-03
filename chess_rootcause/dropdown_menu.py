from kivy.app import App
import kivy.uix.dropdown
import kivy.uix.button
import kivy.uix.boxlayout
import kivy.uix.label
import kivy.uix.popup
import kivy.base
import os
import json


class PrimaryRootCauseDropdownApp(App):
    def build(self):

        input_file_path = os.path.join('inputs', 'inputs.json')

        with open(input_file_path) as json_file:
            input_json = json.load(json_file)

        box = kivy.uix.boxlayout.BoxLayout(orientation='vertical')
        label = kivy.uix.label.Label(text='Primary Root Cause')
        button = kivy.uix.button.Button(text='Selection', font_size=30, size_hint_y=0.15, on_release=self.close_list)
        box.add_widget(label)
        box.add_widget(button)

        self.dropdown = kivy.uix.dropdown.DropDown()  # Create the dropdown once and keep a reference to it
        self.dropdown.bind(on_select=lambda instance, x: setattr(button, 'text', x))

        for value in input_json['primary_root_causes']:  # create the buttons once
            #btn = kivy.uix.button.Button(text='%s' % value, size_hint_y=None, height=44,
            #             on_release=lambda btn: print(btn.text))  # bind every btn to a print statement
            btn = kivy.uix.button.Button(text='%s' % value, size_hint_y=None, height=44,
                         on_release=self._on_release)  # bind every btn to a print statement

            btn.text = '%s' % value
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        return box

    def close_list(self, button):
        self.dropdown.open(button)  # you need this to open the dropdown

    def _on_release(self, entry):
        self.primary_root_cause = entry.text
        return None
