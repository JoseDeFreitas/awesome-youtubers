file_readme = './../readme.md'
with open(file_readme, 'r') as read_readme:
    content_readme = read_readme.readlines()

def featured_playlists():
    featured_playlists_errors_nums = []
    featured_playlists_line = 'Featured playlists:'
    featured_playlists_dlen = 124
        
    for j, i in enumerate(content_readme):
        if featured_playlists_line in i:
            if len(i) < featured_playlists_dlen and i[-2] != '\\':
                featured_playlists_errors_nums.append(j)
    return featured_playlists_errors_nums

featured_playlists_errors_nums = featured_playlists()
