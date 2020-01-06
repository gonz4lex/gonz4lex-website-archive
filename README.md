# alexgonzalezc.dev

Hello! This is the built output of my website, made with [Pelican](https://github.com/getpelican/pelican) and Python.

## Code

The source code of the blog can be found in the [`src` branch](https://github.com/gonz4lex/gonz4lex.github.io/tree/src), as the master branch is used to serve the website to Github Pages.
Therefore, `master` and `src` should **NEVER** be merged.

## Writing content

I write posts in the content/posts directory, in Markdown format. Static pages are in content/pages.
I use the [Clean Blog](https://github.com/gilsondev/pelican-clean-blog) theme, with some modifications to fit my site.

## Publishing

I use Github Pages for hosting the static website.

In the source, there is a Makefile with a `github` task that publishes the output folder to the `master` branch, which is then served statically over Github Pages.
