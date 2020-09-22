---
layout: default
hook: I thought it would be cool to create a distributed network of blogs via RSS feed. Here's how I set it up:
utm_urls:
- https://raspbyprojects.com?utm_source=fwd-discord
- https://raspbyprojects.com?utm_source=gatech-gchat
- https://rapsbyprojects.com?utm_source=hackernews
- https://raspbyprojects.com?utm_source=startups-discord
---
# RSS Feed on your homepage with python

<div style="display:flex; justify-content: center"><iframe width="560" height="315" src="https://www.youtube.com/embed/wIAz494FuSc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

### Introduction
I started researching this project a few times before cutting it down to the bare bones project it is now. The problem with building a homepage is that any feature can grow larger an larger in scope if it's the window to additional features. A deconstructed component analysis helped me slash the scope of this project, so I could focus on only the features that provided me value.

The basic product that I wanted to build was an RSS feed that allowed people to network with each other through their own blogs. Looking at the big picture, this is like a social network, but each given node on the network is managed by a different person, rather than an overarching entity like Facebook.


### Component Analysis
The core components for this project are:

Component | Value | Total
---|---|---
1. RSS index | 10% | 10%
2. RSS reader | 20% | 30%
3. Persisting Raw RSS data | 5% | 35%
4. Transforming Raw RSS data | 20% | 55%
5. Persisting Transformed data | 5% | 60%
6. Templating data into HTML | 20% | 80%
7. Ranking RSS links | 8% | 88%
8. Streaming RSS links | 12% | 100%

This is an ELT project, just like the one I worked on last week. I have to extract data from an outside service (rss), load the raw data into my Raspberry Pi, transform it, then publish it. My last project required some persisting of raw data because I wanted to be able to go back and see how my statistics had changed over time. This project doesn't need that. All I need to do is generate a new set of links every week. So here is the bare minimum:

Component | Value | Total
---|---|---
1. RSS index | 10% | 10%
2. RSS reader | 20% | 30%
4. Create a list of Links | 20% | 50%
6. Publish the list of links | 20% | 70%

This means I can get 70% of my functionality by doing 4 components. That's good enough for a proof of concept, and I can extend that application as needed later on.


### Classes at a high-level of abstraction
Using these components as guidance, I came up with 5 files that this application will need:
* main.py
* parser.py - parse RSS urls from a yaml into list
* extractor.py - extract links from rss feeds
* transformer.py - sort links by publish date, and get projection of links after sorted
* exporter.py - export the list of links to a yaml file

### Research
Here are some of the tutorials and documentation I used to hack this project together:

* [yaml parser for python tutorial](http://zetcode.com/python/yaml)
* [python RSS reader](https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.html)
* [jekyll data files](https://jekyllrb.com/docs/datafiles/)
* [jekyll layouts tutorial](https://www.youtube.com/watch?v=bDQsGdCWv4l)

Hopefully this project provides a basic network, so other people can start to network with their own articles and interests.
