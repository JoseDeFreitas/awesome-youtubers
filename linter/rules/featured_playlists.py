import pathlib

here = pathlib.Path(__file__).parent
file_readme = here / '../../test.md'
with open(file_readme, 'r') as read_readme:
    content = read_readme.readlines()


class FeaturedPlaylists():
    """
    Contains methods for the detection of various
    rules asigned to the "Featured playlists:" sections.
    These methods edit the readme.md file (the awe-
    some list) in-place if any of the rules isn't
    met.

    Attributes:
    checker (str): matches the "Featured playlists:" string.
    length (int): minimum length of the line to break line.
    result (str): result of the operation.
    """

    checker = "Featured playlists:"
    length = 124

    def __init__(self):
        self.result = "🟢 0: perfect."

    def trailing_slash(self):
        """
        Looks for backslash and the end of all the matching
        lines ("Featured playlists:" lines) and a line
        break tag "<br>" at the next line.
        """

        for line, value in enumerate(content):
            if self.checker in value:
                last = value[-2]
                if len(value) < self.length:
                    if last != "\\" and "<br>" not in content[line+1]:
                        if last == " ":
                            content[line] = f"{value[:-1]}\\\n<br>\n"
                        else:
                            content[line] = f"{value[:-1]} \\\n<br>\n"

                        with open(file_readme, 'w') as write_readme:
                            write_readme.writelines(content)

                        self.result = f"🔴 {line}: backslash | line break.\nFixed."
                    elif last != "\\" and "<br>" in content[line+1]:
                        if last == " ":
                            content[line] = f"{value[:-1]}\\\n"
                        else:
                            content[line] = f"{value[:-1]} \\\n"

                        with open(file_readme, 'w') as write_readme:
                            write_readme.writelines(content)

                        self.result = f"🔴 {line}: backslash.\nFixed."
                    elif last == "\\" and "<br>" not in content[line+1]:
                        content[line+1] = "<br>\n\n"

                        with open(file_readme, 'w') as write_readme:
                            write_readme.writelines(content)

                        self.result = f"🔴 {line}: line break.\nFixed."

        return self.result

    def closed_backsticks(self):
        """
        Looks that all backsticks of every word are co-
        rrectly opened and subsequent closed.
        """

        return self.result


featured_playlists = FeaturedPlaylists()
print(featured_playlists.trailing_slash())
