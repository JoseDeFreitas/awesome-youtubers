# Last "as" keyword is in the form ab_cd, where "a" and
# "b" are the first letters of the two words of the module
# and "c" and "d" are the first letters of the two words
# of the function of the module.

from rules.content_about import trailing_slash as ca_ts
from rules.featured_playlists import trailing_slash as fp_ts
from rules.youtubers_names import trailing_slash as yn_ts


def main() -> None:
    """
    Main function. Used specifically to call print results
    by calling functions into rules/.

    Functions:
    content_about: trailing_slash, comma_separated
    featured_playlists: trailing_slash, closed_backsticks
    youtubers_names: trailing_slash, youtube_link
    """

    # "youtubers_names"
    print("YouTubers names:")
    print(yn_ts())
    # "content_about"
    print("Content about:")
    print(ca_ts())
    # "featured_playlists"
    print("Featured playlists:")
    print(fp_ts())


if __name__ == '__main__':
    main()
