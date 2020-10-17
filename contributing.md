# Contribution guidelines

Please follow the [code of conduct](https://github.com/JoseDeFreitas/awesome-youtubers/blob/master/code-of-conduct.md).
Note that "YouTube channel", "channel" and "YouTuber" mean the same thing in [this repository](https://github.com/JoseDeFreitas/awesome-youtubers).
- [Channel rules](#channel-rules)
- [Add a youtuber](#add-a-youtuber)
  - [Youtuber template](#youtuber-template)
  - [Pull request template](#pull-request-template)
- [Open issues](#open-issues)

Only add youtubers that are **awesome**! *"After all, it's a curation, not a collection"*. [What is awesome?](https://github.com/sindresorhus/awesome/blob/main/awesome.md#only-awesome-is-awesome)
It doesn't matter if the youtuber isn't active anymore; if the youtuber has videos/playlists uploaded but no new videos, it still counts. Follow the channel rules below when deciding on what youtuber to add.
**Look up into this issue -> [#32](https://github.com/JoseDeFreitas/awesome-youtubers/issues/32) for more information and a discussion.**

## Channel rules

- The channel is focused on the technology and the youtuber also teaches about tech-related content. Examples of acceptable topics: JavaScript tutorials, web design, command-line cmdlets. Examples of not acceptable topics: freelancing as an illustrator, laws in the technology industry, personal finance tips, makeup, jokes. 
- It must be an entire YouTube channel (a youtuber). You can't add only one video or playlist.
- The channel should be made up of content created by the YouTuber. Do not add channels that create playlists and add videos from other youtubers.
- The channel must follow the [YouTube terms](https://www.youtube.com/t/terms) and any other rules provided by YouTube.
- The channel must be primarily English. 

**_For awesome YouTubers in other languages:_** Please contribute to the corresponding language list located in the [other-languages folder](https://github.com/JoseDeFreitas/awesome-youtubers/tree/master/other-languages/readme-non_en.md). Rules still apply to non-english channels as well.)

## Add a youtuber

To add a youtuber, you will need to create a pull request from a forked repository. 

- On the upper right, click on the fork button 
- In the fork you've created, create a new branch (If you're using command line, do: `git checkout -b NAME_OF_BRANCH`.)
- Edit the readme.md file in the branch you've just created. 
- Using the YouTuber template down below, add the youtuber(s) to the appropriate section **at the bottom of the section**  or create another section if you need to (a section holds several YouTube channels, please use discretion). 

*Jump to the [Pull request template](#pull-request-template) to know how to open a pull request*.

How to use the YouTuber template: 
- Do not use link shorteners
- Do not change any layout or attributes in the template
- Fill out the template with YouTuber information replacing items in ALL_CAPS and the featured playlist section
- The link to the channel must redirect only to the youtuber's channel main page (it **shouldn't** redirect to one of their videos specific channel section, or subscribe button) (eg. https://www.youtube.com/user/github or https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ). 
- To get the avatar of the channel, go to the main channel's page, right-click the avatar and select "copy image adress". Paste the image address to replace the LINK_TO_THE_AVATAR_OF_THE_YOUTUBE_CHANNEL in the template. (Do not modify the image or change the width and/or height attributes on the `<img>` tag.)
- If the channel meets any badge requirements, add accordingly (refer to [badges.md](https://github.com/JoseDeFreitas/awesome-youtubers/blob/master/badges.md)). If the channel doesn't meet badge(s) requirements, delete that badge and keep the order with the other ones. Channels do not need to meet any badge requirement.
- The "Content about" section **should not** be more than **1** line.
- The "Featured playlists" section **should not** be more than **2** lines. 
  - If the youtuber doesn't have any playlist, you can consider a series of videos as a playlist or type "`None`".

### YouTuber template: 

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

**The "Featured playlists" section could lead to some layout problems**. If the "Featured playlists" section is only 1 line, the youtuber below will have a broken layout. To solve this, add a line break `<br/>`  below the "Featured playlists" line. REMEMBER to also add `\` after the "Featured playlists" section (in the same line). 

Example:

[<img align="left" height="94px" width="94px" alt="GitHub channel's avatar" src="https://yt3.ggpht.com/a/AATXAJzVBGU-QyENevFp8etYX1iEak8Y7KEjUPsucWAvAA=s100-c-k-c0xffffffff-no-rj-mo"/>](https://www.youtube.com/user/github)

[**GitHub**](https://www.youtube.com/user/github) [<img height="16px" width="16px" alt="Badge for youtubers that upload videos weekly" src="media/badge-weekly.svg" title="Uploads videos weekly"/>](badges.md#weekly-video-upload) \
Content about: Open Source, Security, App development \
Featured playlists: `Open Source Friday`, `GitHub Satellite 2020 - Work`, `Public Roadmap`, `GitHub Artic Code Vault`.

<br/>

### Pull request template

When you finished adding the youtube channel(s) on the forked repository, open a pull request. 

To open a pull request:
- Go to the [Pull request section in this repository](https://github.com/JoseDeFreitas/awesome-youtubers/pulls)
- Click on "New pull request" 
- Click on "compare across forks". 
- Change the two options on the right-hand side of the arrow "<-" icon to be the fork you've created (it should be `your_github_username/awesome-youtubers`) and the branch you've created in your fork. **Don't change the two options on the left (whose should be "base repository: JoseDeFreitas/awesome-youtubers" and "base: main".)** 
- Click on "Create pull request"
- You should see the [pull request template](https://github.com/JoseDeFreitas/awesome-youtubers/blob/main/.github/pull_request_template.md) automatically. Fill it with the proper information.
- Click on "Create pull request" and you're all set!

You can add any number of youtubers at a time in just one pull request. *The label "new youtuber" will get automatically added when you open the pull request*. To keep the order, please follow this pull request syntax (copy and paste):

Follow this template ([pull request template](https://github.com/JoseDeFreitas/awesome-youtubers/blob/main/.github/pull_request_template.md). It should be automatically typed when you open the pull request):

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
