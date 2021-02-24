import pathlib

here = pathlib.Path(__file__).parent
file_readme = here / '../../test.md'
with open(file_readme, 'r') as read_readme:
    content = read_readme.readlines()


class YoutubersNames():
    """
    Contains methods for the detection of various
    rules asigned to the YouTubers names lines.
    These methods edit the readme.md file (the awe-
    some list) in-place if any of the rules isn't
    met.

    Attributes:
    checker (str): matches the YouTuber names
    "[**" string.
    result (str): result of the operation.
    """

    checker = "[**"

    def __init__(self):
        self.result = "🟢 0: perfect."

    def trailing_slash(self):
        """
        Looks for backslash and the end of all the matching
        lines (YouTubers names lines).
        """

        for line, value in enumerate(content):
            if self.checker in value:
                last = value[-2]
                if last != "\\":
                    if last == " ":
                        content[line] = f"{value[:-1]}\\\n"
                    else:
                        content[line] = f"{value[:-1]} \\\n"

                    with open(file_readme, 'w') as write_readme:
                        write_readme.writelines(content)

                    self.result = "🔴 -1: backslash.\nFixed."

        return self.result

    def youtube_link(self):
        """
        Checks whether the link typed is from youtube.com.
        """

        link = "youtube.com"
        for line, value in enumerate(content):
            if self.checker in value:
                if link not in value:
                    self.result = "🔴 -1: YouTube link."

        return self.result


youtubers_names = YoutubersNames()
print(youtubers_names)
