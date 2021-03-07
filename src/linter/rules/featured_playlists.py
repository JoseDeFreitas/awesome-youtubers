import pathlib

here = pathlib.Path(__file__).parent
file_readme = here / '../../../readme.md'
with open(file_readme, 'r') as read_readme:
    content = read_readme.readlines()

CHECKER = "Featured playlists:"
LENGTH = 124


def trailing_slash() -> str:
    """
    Looks for backslash and the end of all the matching
    lines ("Featured playlists:" lines) and a line
    break tag "<br>" at the next line.
    """

    result = ["🟢 0: perfect."]

    for line, value in enumerate(content):
        if CHECKER in value:
            last = value[-2]
            if len(value) < LENGTH:
                if last != "\\" and "<br>" not in content[line+1]:
                    if last == " ":
                        content[line] = f"{value[:-1]}\\\n<br>\n"
                    else:
                        content[line] = f"{value[:-1]} \\\n<br>\n"

                    with open(file_readme, 'w') as write_readme:
                        write_readme.writelines(content)

                    result.append(f"🔴 {line}: backslash | line break. Fixed.")
                elif last != "\\" and "<br>" in content[line+1]:
                    if last == " ":
                        content[line] = f"{value[:-1]}\\\n"
                    else:
                        content[line] = f"{value[:-1]} \\\n"

                    with open(file_readme, 'w') as write_readme:
                        write_readme.writelines(content)

                    result.append(f"🔴 {line}: backslash. Fixed.")
                elif last == "\\" and "<br>" not in content[line+1]:
                    content[line+1] = "<br>\n\n"

                    with open(file_readme, 'w') as write_readme:
                        write_readme.writelines(content)

                    result.append(f"🔴 {line}: line break. Fixed.")

    if len(result) > 1:
        return '\n'.join(result[1:])
    else:
        return ''.join(result)
