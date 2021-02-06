file_readme = './../readme.md'
with open(file_readme, 'r') as read_readme:
    content_readme = read_readme.readlines()

def youtubers_names():
    youtubers_name_errors_nums = []
    youtuber_count_char = '[**'
        
    for j, i in enumerate(content_readme):
        if youtuber_count_char in i:
            if i[-2] != '\\':
                youtubers_name_errors_nums.append(j)
    return youtubers_name_errors_nums

youtubers_name_errors_nums = youtubers_names()
