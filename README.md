# alexgonzalezc.dev

Hello! This is the source code of my website, made with [Pelican](https://github.com/getpelican/pelican) and Python.

## Code

The source code of the blog can be found in the [`src` branch](https://github.com/gonz4lex/gonz4lex.github.io/tree/src), as the main branch is used to serve the website to Github Pages.
Therefore, `main` and `src` should **NEVER** be merged.

## Writing content

I write posts in the content/posts directory, in Markdown format. Static pages are in content/pages.
I use the [svbhack](https://github.com/gfidente/pelican-svbhack) theme, with some modifications to fit my site.

## Publishing

I use Github Pages for hosting the static website.

The Makefile in this source has a `github` task that publishes the output folder to the `main` branch, which is then served statically over Github Pages.
