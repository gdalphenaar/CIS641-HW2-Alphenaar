title: This Site Itself
short-title: About
date: 2022-06-10
published:

This site is made with a combination of [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) and [Flask-FlatPages](https://flask-flatpages.readthedocs.io/en/latest/index.html) (this page itself was originally a Markdown document rendered to HTML using Flask-FlatPages). Frozen-Flask is nice because it spits out static HTML files based on Flask templates (nice for hosting on GitHub Pages, like this site). Flask-FlatPages is nice because it combines Markdown-based "blogging"-type capabilities with Flask templates.

I think both of these together make for a powerful combo of a static site that's easy to build in Flask with easy-to-update blog-style posts. Admittedly, this is probably a little overpowered for something like this, but I really wanted to be able to use Flask (which I know fairly well) to whip up quick static sites because I'm pretty bad at webdev-type tasks...

A big part of the motivation here was to be able to have a small number of relatively fixed pages (i.e., the [about me]({{ url_for('about') }}) page), while also being able to quickly add new project pages and blog-esque posts using Markdown (like this [project page]({{  url_for("page", path='guitar-monitor') }})). I'll post further findings and/or developments here, if only for my own posterity...