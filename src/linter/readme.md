# Awesome YouTubers linter

The awesome-youtubers linter is a workflow that checks the layout of the pull requests opened. This helps the contributors show if
something in the layout is not formatted correctly so it can be fixed. This linter was created in order to keep the format of the
list without breaking the layouts (images, new lines, etc.)

## Rules

| File containing                                            | Rules followed                                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [YouTuber's name and link](rules/youtubers_names.py) line. | - Trailing `\`<br/>- Spaces between badges                                   |
| [Content about](rules/content_about.py) line.              | - Trailing `\`<br/>- Spaces between words (including `,`)                    |
| [Featured playlists](rules/featured_playlists.py) line.    | - Trailing `\`<br/>- Spaces between words (including `,`) and a trailing `.` |
| [Links formatted](rules/link_format.py)                    | - Well-formatted links (`[text](link)`)                                      |
