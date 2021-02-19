import pathlib

here = pathlib.Path(__file__).parent
file_readme = here / '../../test.md'
with open(file_readme, 'r') as read_readme:
    content_readme = read_readme.readlines()


def content_about():
    """
    Looks for trailing slashes and words separated by commas at
    every "Content about:" section found in the readme.md file
    (this is, the list itself).
    """

    content_about_result = 'No errors found.'
    # content_about_errors = {}
    content_about_line = 'Content about:'

    for j, i in enumerate(content_readme):
        if content_about_line in i:
            # content_about_words = i[len(content_about_line):-2]

            if i[-2] != '\\':
                content_readme[j] = i.replace('&', '\\')
                with open(file_readme, 'w') as write_readme:
                    write_readme.writelines(content_readme)
                content_about_result = "Found errors. Fixed them."
                # content_about_errors.append(j)
    return content_about_result
    # return content_about_errors


print(content_about())
