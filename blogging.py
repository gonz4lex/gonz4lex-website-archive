import sys
from datetime import datetime
from colorama import Fore

TEMPLATE = """

title: {title}
date: {year}-{month}-{day} {hour}:{minute:02d}
category:
tags:
slug: {slug}
author: Alex Gonzalez
summary:
header_cover:
status: draft


"""

def make_post(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/posts/_{}.md".format(slug)
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print(Fore.GREEN + "SUCCESS! " + Fore.RESET + "File created: " + f_create)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        make_post(sys.argv[1])
    else:
        print("Please specify a post title.")