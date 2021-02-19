import pathlib

here = pathlib.Path(__file__).parent
file_readme = here / '../../test.md'
with open(file_readme, 'r') as read_readme:
    content_readme = read_readme.readlines()


def featured_playlists():
    """
    Looks for trailing slashes and words separated by commas at
    every "Featured playlists:" section found in the readme.md file
    (this is, the list itself).

    result (str): return value of the function.
    checker (str): detector of the line corresponding the file.
    length (int): length of the corresponding line.
    """

    result = 'No errors found.'
    checker = 'Featured playlists:'
    length = 124

    for line, value in enumerate(content_readme):
        if checker in value:
            # Check for trailing slash
            if len(value) < length and value[-2] != '\\':
                if value[-2] == ' ':
                    content_readme[line] = value[:-1] + '\\' + '\n'
                    with open(file_readme, 'w') as write_readme:
                        write_readme.writelines(content_readme)
                else:
                    content_readme[line] = value[:-1] + ' \\' + '\n'
                    with open(file_readme, 'w') as write_readme:
                        write_readme.writelines(content_readme)

                result = "Trailing slash wasn't found.\nFixed."

    return result


print(featured_playlists())
