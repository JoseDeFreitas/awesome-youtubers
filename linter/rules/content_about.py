import pathlib

here = pathlib.Path(__file__).parent
file_readme = here / './../readme.md'
with open(file_readme, 'r') as read_readme:
    content_readme = read_readme.readlines()

def content_about():
    content_about_errors_nums = []
    content_about_line = 'Content about:'
        
    for j, i in enumerate(content_readme):
        if content_about_line in i:
            if i[-2] != '\\':
                content_about_errors_nums.append(j)
    return content_about_errors_nums

content_about_errors_nums = content_about()
