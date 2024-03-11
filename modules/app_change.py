import flet as ft
from flet import (
    Container,
    Column
)
import nm
from utils import attempt_float, read_markdown_file


# Change App
class AppChange(ft.UserControl):
    def __init__(self):
        super().__init__()
        ## Current Value
        self.input_now = ft.TextField(
            label="Current value", hint_text="Current value"
        )
        ## Previous Value
        self.input_prev = ft.TextField(
            label="Previous value", hint_text="Previous value"
        )
        # Button
        self.btn = ft.ElevatedButton(text="Generate", on_click=self.button_gen_clicked)
        
        # Output text
        txt_size = 14 # 14
        self.output_text_field = ft.TextField(value="", multiline=True, read_only=False, text_size=txt_size) 

    def build(self):
        return Container(
            content=Column(
                [
                 self.input_now,
                 self.input_prev,
                 self.btn,
                 self.output_text_field,
                 ft.Text("How to use", theme_style=ft.TextThemeStyle.TITLE_MEDIUM), 
                 ft.Markdown(read_markdown_file("man/change_app_man.md"), selectable=True)
                 ]
            )
        )
    def button_gen_clicked(self, e):
        self._log()
        self.output_text_field.value = self.calc()
        self.output_text_field.focus()
        self.output_text_field.update()
        
    def _log(self):
        print("Btn clicked")
        print(f"Now: {self.input_now.value}")
        print(f"Prev: {self.input_prev.value}")
        print(self.calc())
        
    def calc(self):
        now = attempt_float(self.input_now.value)
        prev = attempt_float(self.input_prev.value)
        ch_str = nm.change(now=now, prev=prev)
        return ch_str
