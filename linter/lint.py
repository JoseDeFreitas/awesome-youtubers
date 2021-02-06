from rules import (content_about, featured_playlists, youtubers_names)

file_readme = './../readme.md'
with open(file_readme, 'r') as read_readme:
    content_readme = read_readme.readlines()

def main():
    """
    Main function. Used specifically to call print results
    by calling functions into rules/.
    """
    if len(youtubers_names.youtubers_name_errors_nums) == 0:
        print("Every YouTubers names are good.", "\n")
    else:
        print("'YouTubers name' errors:\n", '\n'.join(["Error at line {}: there should be a trailing '\\'.".format(i) for i in youtubers_names.youtubers_name_errors_nums]), "\n")
    
    if len(content_about.content_about_errors_nums) == 0:
        print("Every 'Content about' sections are good.", "\n")
    else:
        print("'Content about' errors:\n", '\n'.join(["Error at line {}: there should be a trailing '\\'.".format(i) for i in content_about.content_about_errors_nums]), "\n")

    if len(featured_playlists.featured_playlists_errors_nums) == 0:
        print("Every 'Featured playlists' sections are good.", "\n")
    else:
        print("'Featured playlists' errors:\n", '\n'.join(["Error at line {}: there should be a trailing '\\'.".format(i) for i in featured_playlists.featured_playlists_errors_nums]), "\n")

if __name__ == '__main__':
    main()
