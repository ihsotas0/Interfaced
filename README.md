# Interfaced

A personal creative writing project which began September 2023. Narratives and
worldbuilding cover a wide range of themes from politics to artificial
intelligence. See `drafts` for official content. Here is a snippet:

> *The Slice*, or the slice, refers to a specific program family, invented by
> teenage hackers in the 2060s, which utilize joining programs to kill a person.
> To begin the Slice, hemispherectomy software is executed along the initially
> programmed plane in the mind (between hemispheres). This also signals to
> knowledgeable recipients the coming end of their life. Then, the
> hemispherectomy software, which runs as a daemon to maintain the plane
> separating the mind, is fed bogus information, causing the bisection plane to
> rotate along numerous positions in the mind. The point, speed, and direction
> of rotation jump randomly. The severing of the mind into such small sections
> rapidly stops normal brain function causing seizures, comas, and even death.

If you enjoyed that, feel free to read more here on GitHub or more accessibly on
my website: <https://jonahspector.net/writing/interfaced> (not operational as of
last commit)

## Organization

```
archive/            <--- Old files; not organized well
content/            <--- Raw source markdown of drafts/
├── Interfaced/            <--- Capitalized for build.sh
│   ├── 001_front_matter/
│   │   ├── 001_metadata.yml
│   │   ├── 002_title.md
│   │   ├── 003_copyright.md
│   │   ├── 004_dedication.md
│   │   └── front_cover.png
│   ├── 002_chapters/            <--- Table of contents generated here
│   │   ├── 001_chapter_name/
│   │   │   ├── 001_scene_name.md
│   │   │   ├── wip_002_scene_name.md
│   │   │   └── wip_003_scene_name.md
│   │   ├── 002_chapter/
│   │   └── wip_003_chapter/
│   ├── 003_back_matter/
│   │   ├── 001_afterword.md
│   │   ├── 002_author.md
│   │   └── back_cover.png
│   ├── spine_cover.png
│   └── wip_misc.md
├── Book_Two/
└── Book_Three/
drafts/            <--- Compiled content/ files for viewing
├── sffms/
│   └── JonahSpector_Interfaced_2025-01-01.pdf
└── JonahSpector_Interfaced_2025-01-01.epub
notes/             <--- Organized using dot hierarchy (topic.subtopic.subsubtopic.md)
prose/             <--- Misc snippets of prose, free writing sessions
style/             <--- Stylesheets for EPUB and PDF pandoc output to drafts/
.gitignore
build.sh
LICENSE
README.md
todo.txt
```

## Contributing

* Look for `todo.txt` items tagged `del:anyone` and complete them
* Help proofread and edit content
* Comment on ideas directly by making a pull request and inserting your comments
  directly in the file you are commenting on

## License

This work is licensed under a [Creative Commons
Attribution-NonCommercial-NoDerivs 4.0 International License][cc-by-nc-nd].

[![CC BY-NC-ND 4.0][cc-by-nc-nd-image]][cc-by-nc-nd]

[cc-by-nc-nd]: http://creativecommons.org/licenses/by-nc-nd/4.0/
[cc-by-nc-nd-image]: https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png
