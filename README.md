# Purpose/usage

The project has a single executable for now, `ggmon`, which takes no arguments.

It records any clipboard copies (Ctrl-C or Ctrl-Alt-C) of items from Path of Exile.
These are stored in an `items` directory in the current working directory where the program was run from, each named with a nanosecond timestamp.
This allows the order of copies (and thus crafts) to be identified in the future.

Note that it has no safeguards around basic/advanced copies and just stores the files verbatim, take care to copy in the correct format for what you intend to do with the files.

It will ignore non-item clipboard contents and will keep track of the "last" item seen to avoid duplicates, take this into consideration.

# Installation

Install Python 3.12 and then either go for Poetry if you want to fiddle with the code or for pipx if you're fine with just building and using it.

## Poetry

Install [Poetry](https://python-poetry.org/docs/#installation).
Download the repository source and unpack it.
`poetry install`
`poetry run ggmon`

## pipx

Install [pipx](https://github.com/pypa/pipx?tab=readme-ov-file#on-windows).
`pipx install git+https://github.com/zao/geargrind.git`
`ggmon`
