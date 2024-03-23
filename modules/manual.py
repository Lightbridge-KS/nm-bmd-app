# man_app={
#     "change": f"""- Input current value as number (e.g. 2)
# - Input previous value as number (e.g. 1)
# - % change = (current - previous) * 100 / previous""",
#     "spine_ht_loss": f"""- Input height in centimeter (e.g. 10)
# - Comma-separated value to calculate mean (e.g. 10, 12)"""
# }

def read_man(man_name):
    """Read Markdown from `man/`"""
    # Technique from this https://py-pkgs.org/04-package-structure#including-non-code-files-in-a-package
    from importlib import resources 
    with resources.path("modules.man", man_name) as file_path:
        markdown_content = read_markdown_file(file_path)
    return markdown_content


def read_markdown_file(file_path):
    from pathlib import Path
    file_path = Path(file_path)
    try:
        # Open the markdown file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire file content into a string
            markdown_content = file.read()
            return markdown_content
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


