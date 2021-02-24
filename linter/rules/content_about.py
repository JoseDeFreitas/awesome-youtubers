import pathlib

here = pathlib.Path(__file__).parent
file_readme = here / '../../test.md'
with open(file_readme, 'r') as read_readme:
    content = read_readme.readlines()


class ContentAbout():
    """
    Contains methods for the detection of various
    rules asigned to the "Content about:" sections.
    These methods edit the readme.md file (the awe-
    some list) in-place if any of the rules isn't
    met.

    Attributes:
    checker (str): matches the "Content about:" string.
    result (str): result of the operation.
    """

    checker = "Content about:"

    def __init__(self):
        self.result = "🟢 0: perfect."

    def trailing_slash(self) -> str:
        """
        Looks for backslash and the end of all the matching
        lines ("Content about:" lines).
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

                    self.result = "🔴 -1: line break.\nFixed."

        return self.result

    def comma_separated(self) -> str:
        """
        Looks through all words in the section to check
        if they're separated by a comma and a space
        ", ".
        """

        # for line, value in enumerate(content):
        #     if self.checker in value:

        return self.result


content_about = ContentAbout()
print(content_about.trailing_slash())
