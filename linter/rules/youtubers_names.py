import pathlib

here = pathlib.Path(__file__).parent
file_readme = here / '../../test.md'
with open(file_readme, 'r') as read_readme:
    content = read_readme.readlines()

CHECKER = "[**"


def trailing_slash() -> str:
    """
    Looks for backslash and the end of all the matching
    lines (YouTubers names lines).
    """

    result = ["🟢 0: perfect."]

    for line, value in enumerate(content):
        if CHECKER in value:
            last = value[-2]
            if last != "\\":
                if last == " ":
                    content[line] = f"{value[:-1]}\\\n"
                else:
                    content[line] = f"{value[:-1]} \\\n"

                with open(file_readme, 'w') as write_readme:
                    write_readme.writelines(content)

                result.append(f"🔴 {line}: backslash. Fixed.")

    if len(result) > 1:
        return '\n'.join(result[1:])
    else:
        return ''.join(result)
