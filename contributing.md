# Contribution guidelines

Please follow the [code of conduct](https://github.com/JoseDeFreitas/awesome-youtubers/blob/master/code-of-conduct.md).
Note that "YouTube channel", "channel" and "youtuber" mean the same thing in [this repository](https://github.com/JoseDeFreitas/awesome-youtubers).

- [Add a youtuber](#add-a-youtuber)
  - [Pull request template](#pull-request-template)
- [Open issues](#open-issues)

## Add a youtuber

Please, only add youtubers that are actually **awesome**! *"After all, it's a curation, not a collection"*. [What is awesome?](https://github.com/sindresorhus/awesome/blob/main/awesome.md#only-awesome-is-awesome)
It doesn't matter if the youtuber isn't active anymore; if the youtuber has videos/playlists uploaded but no new videos, it still counts.

To add a youtuber, fork this repository, then (in the fork you've created) create a new branch (to do this, in your fork main page, click on the "main" brach. You'll see an input. In there, type the name of the branch you want (please keep the name accordingly to the repository) and click on "create branch: NAME_OF_BRANCH from 'main'". If you're using the cli, do: `git checkout -b NAME_OF_BRANCH`.) After that, edit the readme.md file (make sure you're in the branch you've just created) and add the youtuber to the existing section you consider it fits well or you can also create another section if you need to (if you will, please keep in mind that a section holds several YouTube channels and is intended to work as it). **Add the youtuber at the bottom of the category**. *Jump to the [Pull request template](#pull-request-template) to know how to open a pull request*.

For a channel to be added, you need to follow these rules:
- The channel is tech-related and the youtuber also teaches about teach stuff. It doesn't has to be mainly tech-related, but the content of the channel should at least be able to be used in technology. To explain me better, I'll give you these examples: a channel about JavaScript tutorials, a channel about web design, a channel about command-line cmdlets - these are mainly tech-related. A channel about freelancing as an illustrator, a channel about laws in the technology, a channel about how to keep track and save your money could not be mainly tech-related, but can be used and applied to tech. A channel about makeup or a channel about compilations of every-day jokes don't apply to this list.
- It must be an entire YouTube channel (a youtuber). You can't add only one video or playlist.
- Make sure the videos/playlists are actually from the YouTube channel you're submitting! A YouTube channel can create playlists and add videos from other youtubers; to keep the content concise and corresponding to the submission, make sure the videos on the playlists are made and uploaded by the youtuber you're submitting.
- The channel must be mainly English. There're good youtubers whose content isn't in English, that's why you can still add them but they need to be added into the markdown file, in the [other-languages folder](https://github.com/JoseDeFreitas/awesome-youtubers/tree/master/other-languages/readme-non_en.md), corresponding to the language the channel is in (the [code of conduct](https://github.com/JoseDeFreitas/awesome-youtubers/blob/master/code-of-conduct.md) and these rules apply **the same** to non-english channels.)
- The link to the channel must redirect only to the youtuber's channel main page (it **shouldn't** redirect to one of their videos or to a specific channel section) (eg. https://www.youtube.com/user/github or https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ). Please **do not use any link shortener** and ensure that the link doesn't have any youtube parameter (eg. like the parameter that redirects the user to the subscribe button.)
- To get the avatar of the channel, go to the main channel's page, right-click the avatar and select "copy image adress". Use that link in the layout (please don't modify the image as any means. Also, don't change the width and/or height attributes on the `<img>` tag.)
- Please add the badges accordingly to the channel (only add the badges if the channel meets the badges requirements) (refer to [badges.md](https://github.com/JoseDeFreitas/awesome-youtubers/blob/master/badges.md)). **Do not** change any badge layout and please follow the order in badges.md (as "verified channel" appears at first, do so when adding the channel. If the channel doesn't meet the first badge, keep the order with the other ones. If it doesn't meet any requirement just don't add any). Please only use the links to the badges in the [media folder](https://github.com/JoseDeFreitas/awesome-youtubers/tree/master/media).
- The channel must follow the [YouTube terms](https://www.youtube.com/t/terms) and any other rules provided by YouTube.
- You should follow the layout style and positioning, which is this:

```html
[<img align="left" height="94px" width="94px" alt="NAME_OF_THE_YOUTUBE_CHANNEL channel's avatar" src="LINK_TO_THE_AVATAR_OF_THE_YOUTUBE_CHANNEL"/>](LINK_TO_THE_CHANNEL)

[**NAME_OF_THE_CHANNEL**](LINK_TO_THE_CHANNEL) [<img height="16px" width="16px" alt="Badge for verified YouTube channels" src="media/badge-verified.svg" title="Is a verified YouTube channel"/>](badges.md#verified-youtube-channel) [<img height="16px" width="16px" alt="Badge for youtubers that upload videos weekly" src="media/badge-weekly.svg" title="Uploads videos weekly"/>](badges.md#weekly-video-upload) \
Content about: EXAMPLE, EXAMPLE, EXAMPLE \
Featured playlists: `playlist-1`, `playlist-2`, `playlist-3`, `playlist-4`.
```

When adding a youtuber below other one, you should add another line. Example:

```html
...
Featured playlists: `playlist-1`, `playlist-2`, `playlist-3`, `playlist-4`.

[<img align="left" height="94px" width="94px" alt="NAME_OF_THE_YOUTUBE_CHANNEL channel's avatar" src="LINK_TO_THE_AVATAR_OF_THE_YOUTUBE_CHANNEL"/>](LINK_TO_THE_CHANNEL)
...
```

*The "Content about" section **should not** be more than **1** line. In this section, describe the main content of the channel.*
*The "Featured playlists" section **should not** be more than **2** lines. In this section, put the best playlists of the youtuber. This is because as the youtuber should at least teach (maybe not explicitly) something according to its channel content. It doesn't have to be a literal YouTube playlist though; this is preferable, but if the youtuber doesn't have any playlist, you can consider as a playlist a series of videos. If still you consider the youtuber doesn't have any playlists, you can type "`None`".*

**The "Featured playlists" section could lead to some layout problems**. If the "Featured playlists" section is 2 lines, there won't be any problem with the layout. But, if the "Featured playlists" section is just 1 line, the youtuber below it will broke the layout. To solve this, add a line break `<br/>` just below the "Featured playlists" line. REMEMBER to also add `\` after the "Featured playlists" section (in the same line). In the example above there should be a `<br/>` below the "Featured playlists" section, but I didn't put it to prevent confuse.

Example:

[<img align="left" height="94px" width="94px" alt="GitHub channel's avatar" src="https://yt3.ggpht.com/a/AATXAJzVBGU-QyENevFp8etYX1iEak8Y7KEjUPsucWAvAA=s100-c-k-c0xffffffff-no-rj-mo"/>](https://www.youtube.com/user/github)

[**GitHub**](https://www.youtube.com/user/github) [<img height="16px" width="16px" alt="Badge for youtubers that upload videos weekly" src="media/badge-weekly.svg" title="Uploads videos weekly"/>](badges.md#weekly-video-upload) \
Content about: Open Source, Security, App development \
Featured playlists: `Open Source Friday`, `GitHub Satellite 2020 - Work`, `Public Roadmap`, `GitHub Artic Code Vault`.

<br/>

### Pull request template

When you finished adding the youtuber(s), open a pull request. To open a pull request, go to the [Pull request section in this repository](https://github.com/JoseDeFreitas/awesome-youtubers/pulls), then click on "New pull request" and therefore click on "compare across forks". After that, select the fork you've created (it should be `your_github_username/awesome-youtubers`) and the branch you've created in your fork. **You need to select these two options in the right-hand side of the arrow "<-" icon. Don't change the two options on the left (whose should be "base repository: JoseDeFreitas/awesome-youtubers" and "base: main".)** Click on "Create pull request", select a title and copy & fill the pull request template you can find below. Then click on "Create pull request" and you're ready!

You can add any number of youtubers at a time in just one pull request. *The label "new youtuber" will get automatically added when you open the pull request*. To keep the order, please follow this pull request syntax (copy and paste):

Follow this template:

```
- **Name of the youtuber:**
- **What the channel is about (eg. web development, design, ...)**:
- **Which section is the channel in? (if you created a section, please specify why)**:
- **Why do you consider the youtuber deserves a place in this list? *What does make it awesome?***:
```

Example:

- **Name of the youtuber**: GitHub
- **What the channel is about (eg. web development, design, ...)**: Software Development Platform for storing repositories.
- **Which section is the channel in? (if you created a section, please specify why)**: Open Source
- **Why do you consider the youtuber deserves a place in this list? *What does make it awesome?***: The youtuber uploads videos every day with general-tech tutorials. These tutorials include securing your organization, finding vulnerabilities, using GitHub actions and more. It also has pretty useful playlists where you can find talks from professionals that teach you diverse topics.

**Use this template for every youtuber you add.**

## Open issues

If you find a layout issue, a typo or an outdated information about a youtuber, please open an issue explaining what it is about.
If you have an idea of a possible feature, please also open an issue explaining your idea.
The issue labels are asigned accordingly to every issue - follow them to know more about the issue.
