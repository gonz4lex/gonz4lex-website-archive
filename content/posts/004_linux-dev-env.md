title: How I got started with Linux
date: 2019-12-08 22:50
category: linux
tags: linux, learning
slug: linux-dev-env
author: Alex Gonzalez
status: published
summary: An overview of my Linux development setup.
header_cover: 

I recently got the itch of purchasing a new laptop for development and learning, so I took the chance on Black Friday and got myself a nice HP Stream 14. I am a long-time Windows user so I thought it would be a great opportunity to get started with Linux and set up a developer workstation while documenting the process.

# Objectives

I wanted this machine to be equipped for:

* data science and machine learning investigation
* writing
* web and software development, mostly in Python
* indie game development
* cloud deployments


For that, I will be using tools like Visual Studio Code, Zsh (with Oh My Zsh), Godot and a nice terminal emulator like Tilix.

# Linux

I searched for a bit trying to decide which Linux flavor I would use. I tried Elementary OS and Ubuntu Budgie, but finally decided myself for the true and tested Ubuntu 18.04 LTS, which grants support and maintenance for up to 5 years. After all, I just want to learn and have fun with this laptop.

At first, I experienced some issues with the system. For example, the Wi-Fi adapter wasn't recognised by the OS, so I had no connection. The Stream 14 doesn't have an Ethernet port, so that wasn't an option either. Finally I had to use my phone's connection through USB thethering so I could run the following commands:

```bash
sudo apt-get upgrade
sudo apt-get update
```

This fixes any broken packages. After that, I was able to install Git and clone a repo with the drivers for my adapters. This got my connection ready to start the real setup.

# Visual Studio Code

# Tilix

# Godot


# Python

Even though Python comes installed in Linux distros by default, its package manager `pip` wasn't available on my system. A swift `sudo apt-get install pip3` took that problem away.
Take note of the `pip3` part, which installs the module for Python 3.

