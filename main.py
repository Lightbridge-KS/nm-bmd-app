import flet as ft
import pyperclip
from app_spine_ht_loss import AppSpineHtLoss
from app_change import AppChange
from utils import parse_str_to_num_or_list, attempt_float, read_markdown_file


def main(page: ft.Page):
    
    # Change Tab
    def change_tab(e):
        my_index = e.control.selected_index
        ## Toggle Visibility
        tab_app_spine_ht_loss.visible = True if my_index == 0 else False
        tab_app_change.visible = True if my_index == 1 else False
        
        ## Toggle Appbar Text
        if my_index == 0:
            page.appbar.middle=ft.Text("Spine Height Loss Calculator", weight=ft.FontWeight.BOLD)
        if my_index == 1:
            page.appbar.middle=ft.Text("Percent Change Calculator", weight=ft.FontWeight.BOLD)

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
            ft.NavigationDestination(icon=ft.icons.PERCENT, label="Change"),
        ]
    )
   
    tab_app_spine_ht_loss = AppSpineHtLoss()
    tab_app_change = AppChange()
    
    # Default
    tab_app_spine_ht_loss.visible = True
    tab_app_change.visible = False
    
    # lv = ft.ListView(controls=[tab_app_spine_ht_loss, tab_app_change], 
    #                  expand=1, spacing=5, padding=10, auto_scroll=False)
    col = ft.Column(controls=[tab_app_spine_ht_loss, tab_app_change])
    page.add(col) 

if __name__ == "__main__":
    ft.app(target=main)
