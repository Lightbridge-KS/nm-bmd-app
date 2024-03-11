import flet as ft
from flet import (
    Container,
    Column
)
import nm
from utils import parse_str_to_num_or_list, read_markdown_file

# Spine Ht Loss App
class AppSpineHtLoss(ft.UserControl):
    def __init__(self):
        super().__init__()
        ## Normal Height (cm)
        self.input_ht_normal = ft.TextField(
            label="Normal height (cm)", hint_text="Normal height in cm"
        )
        ## Collapsed Height (cm)
        self.input_ht_bad = ft.TextField(
            label="Collapsed height (cm)", hint_text="Collapsed height in cm"
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
                 self.input_ht_normal,
                 self.input_ht_bad,
                 self.btn,
                 self.output_text_field,
                 ft.Text("How to use", theme_style=ft.TextThemeStyle.TITLE_MEDIUM), 
                 ft.Markdown(read_markdown_file("man/spine_ht_loss_man.md"), selectable=True)
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
        print(f"Normal: {self.input_ht_normal.value}")
        print(f"Bad: {self.input_ht_bad.value}")
        print(self.calc())
        
    def calc(self):
        normal_cm = parse_str_to_num_or_list(self.input_ht_normal.value)
        bad_cm = parse_str_to_num_or_list(self.input_ht_bad.value)
        ht_loss_str = nm.spine_ht_loss(normal_cm=normal_cm, bad_cm=bad_cm)
        return ht_loss_str