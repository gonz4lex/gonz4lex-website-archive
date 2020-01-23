title: A date with Julia
date: 2020-1-2 11:00
category: julia, data science
tags: learn
slug: a_date_with_julia
author: Alex Gonzalez
status: draft
summary: Getting started with Julia, and dynamic and idiomatic language perfect for data science.
header_cover: images/julia-lang.png


Julia is great, albeit a little complicated to get at around when you first meet. It's great because it writes like Python and [runs like C](https://syl1.gitbook.io/julia-language-a-concise-tutorial/language-core/performances). The optionally typed nature of Julia increases its performance well beyond Python in some cases, but it's better suited to problems that require writing custom algorithms rather than rely on standard solutions. For other less non-trivial tasks, Python is just more simple to use and has a richer package ecosystem ([for now](https://juliaobserver.com)).

That said, if you are still considering using Julia, let's get started with its basics to see if it's the language for you. We will cover both its syntax and concepts as we go through some examples.




# Data Structures

# Strings

# Conditionals

# Loops

# Functions

# Multiple dispatch

One of the reasons for the performance of Julia is the way it relies on types to execute functions based on their parameter types.

For example, the `+` operator can call one of its many methods depending on the types of the operands.