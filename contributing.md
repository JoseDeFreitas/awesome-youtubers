# Contribution guidelines

Please follow the [code of conduct](https://github.com/JoseDeFreitas/awesome-youtubers/blob/master/code-of-conduct.md).
Note that "YouTube channel", "channel" and "youtuber" mean the same thing in [this repository](https://github.com/JoseDeFreitas/awesome-youtubers).

- [Add a youtuber](#add-a-youtuber)
  - [Pull request template](#pull-request-template)
- [Update information](#update-information)

## Add a youtuber

Please, only add youtubers that are actually **awesome**! *"After all, it's a curation, not a collection"*. [What is awesome?](https://github.com/sindresorhus/awesome/blob/main/awesome.md#only-awesome-is-awesome)

To add a youtuber, fork this repository, then edit the readme.md file and add the youtuber to the existing section you consider it fits well or you can also create another section if you need to (if you will, please keep in mind that a section holds several YouTube channels and is intended to work as it).

For a channel to be added, you need to follow these rules:
- The channel is tech-related and the youtuber also teaches about teach stuff. It doesn't has to be mainly tech-related, but the content of the channel should at least be able to be used in technology. To explain me better, I'll give you these examples: a channel about JavaScript tutorials, a channel about web design, a channel about command-line cmdlets - these are mainly tech-related. A channel about freelancing as an illustrator, a channel about laws in the technology, a channel about how to keep track and save your money could not be mainly tech-related, but can be used and applied to tech. A channel about makeup or a channel about compilations of every-day jokes don't apply to this list.
- It must be an entire YouTube channel (a youtuber). You can't add only one video or playlist.
- The channel must be mainly English. There're good youtubers whose content isn't in English, that's why you can still add them but they need to be added into the markdown file, in the [other-languages folder](https://github.com/JoseDeFreitas/awesome-youtubers/tree/master/other-languages), corresponding to the language the channel is in (the [code of conduct](https://github.com/JoseDeFreitas/awesome-youtubers/blob/master/code-of-conduct.md) and these rules apply **the same** to non-english channels).
- The link to the channel must redirect only to the youtuber's channel main page (it **shouldn't** redirect to one of their videos or to a specific channel section) (eg. https://www.youtube.com/user/github or https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ). Please **do not use any link shortener** and ensure that the link doesn't have any youtube parameter (eg. like the parameter that redirects the user to the subscribe button).
- To get the avatar of the channel, go to the main channel's page, right-click the avatar and select "copy image adress". Use that link in the layout (please don't modify the image as any means. Also, don't change the width and/or height attributes on the <img> tag).
- Please add the badges accordingly to the channel (only add the badges if the channel meets the badges requirements) (refer to [badges.md](https://github.com/JoseDeFreitas/awesome-youtubers/blob/master/badges.md)). **Do not** change any badge layout and please follow the order in badges.md (as "verified channel" appears at first, do so when adding the channel. If the channel doesn't meet the first badge, keep the order with the other ones. If it doesn't meet any requirement just don't add any). Please only use the links to the badges in the [media folder](https://github.com/JoseDeFreitas/awesome-youtubers/tree/master/media).
- The channel must follow the [YouTube terms](https://www.youtube.com/t/terms) and any other rules provided by YouTube.
- You should follow the layout style and positioning, which is this:

```html
[<img align="left" height="94px" width="94px" alt="NAME_OF_THE_YOUTUBE_CHANNEL channel's avatar" src="LINK_TO_THE_AVATAR_OF_THE_YOUTUBE_CHANNEL"/>](LINK_TO_THE_CHANNEL)

[**NAME_OF_THE_CHANNEL**](LINK_TO_THE_CHANNEL) [<img height="16px" width="16px" alt="Badge for verified YouTube channels" src="media/badge-verified.svg"/>](badges.md#verified-youtube-channel) [<img height="16px" width="16px" alt="Badge for youtubers that upload videos weekly" src="media/badge-weekly.svg"/>](badges.md#weekly-video-upload) \
Featured videos/playlists: `#most-important-channel-1`, `#most-important-channel-2`, `#most-important-channel-3`, `#most-important-channel-4`, `#most-important-channel-5`, `#least-important-channel`
```

### Pull request template
