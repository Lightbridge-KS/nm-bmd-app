import flet as ft
import pyperclip
from flet import (
    Container,
    Column,
    Row,
    ResponsiveRow,
    Page
)
import nm
from utils import parse_str_to_num_or_list

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
                 ft.Markdown("- Input height in centimeter (e.g. 10)\n - Comma-separated value to calculate mean (e.g. 10, 12)", selectable=True)
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


def main(page: ft.Page):
    
    # Change Tab
    def change_tab(e):
        my_index = e.control.selected_index
        if my_index == 0:
            tab_app_spine_ht_loss.visible = True 
            page.appbar.middle=ft.Text("Spine Height Loss Calculator", weight=ft.FontWeight.BOLD)

        page.update()
    
    page.title = "BMD Helper"
    page.window_min_width = 450
    page.window_width = 450
    page.window_min_height = 565
    page.window_height = 575
    
    # App Bar
    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        bgcolor=ft.colors.SURFACE_VARIANT,
        middle=ft.Text("Spine Height Loss Calculator", weight=ft.FontWeight.BOLD),
        # trailing=ft.IconButton(icon=ft.icons.BRIGHTNESS_2_OUTLINED,
        #                        tooltip="Toggle theme",
        #                        on_click=theme_changed)
    )
    # Nav Bar
    page.navigation_bar = ft.NavigationBar(
        selected_index = 0,
        on_change= change_tab,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HEIGHT, label="Height Loss"),
            # ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
        ]
    )
   
    tab_app_spine_ht_loss = AppSpineHtLoss()
    lv = ft.ListView(controls=[tab_app_spine_ht_loss], 
                     expand=1, spacing=5, padding=10, auto_scroll=False)
    page.add(lv)

if __name__ == "__main__":
    ft.app(target=main)
