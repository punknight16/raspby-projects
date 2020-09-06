---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---
# Getting started with a Jekyll Blog

### Introduction

One of the things that's really nice about getting a new computer, of any kind, is starting out with a clean slate. There are no poorly organized folders  in your home directory, and there are relatively few apps to clutter up your desktop.

Once I got my Raspberry Pi up and running for the first time, I had a little trouble deciding what to do next. My first thought was to create a blog, so here we are. A blog is an excellent way to organize projects and publish the results. Before this Raspberry Pi, I was working on a Macbook Pro. All Macbook users can access the terminal, so these concepts apply whether you are using a Raspberry Pi or a Macbook.

A Macbook has a lot of built-in software for creating content and for entertainment purposes, so my projects could quickly become disorganized, spread across multiple folders and online storage spaces. With this Raspberry Pi, I hope to have the entirety of a project stored in a single folder that can act as a single source of truth for that project.

### Core Concepts

The out of the box software that comes with a Raspberry Pi is a little less user friendly than on a Mac, so I want these projects to be really well researched and spec'ed out before I jump into them. For most of these projects, I could probably just find a tutorial on how to code a particular solution, but I want to also think through the business-side of things. For example, is the project entirely automated or do I need to schedule one hour a week maintaining the infrastructure? Will users be able to adopt using a new tool in their normal workflow or will they need to create a new workflow? And last but not least, when is it time to wind up the project?

For this blog, I've spent a little bit of time going through a "core concepts analysis" before starting. For the core concepts analysis, I wrote out everything that seems important for a blog, and then listed the potential value of each concept.

Blog Concept | Potential Value | Total Value
---|---|---
1. Content | 15% | 15%
2. Posting Platform | 4% | 19%
3. Image Hosting | 1% | 20%
4. Content Delivery Network (CDN) | 2% | 22%
5. Analytics Toolset | 8% | 30%
6. SEO | 2% | 32%
7. Email Collection | 4% | 36%
8. Publishing Schedule | 10% | 46%
9. Hosting | 2% | 48%
10. Subscription/Paywall | 8% | 56%
11. Domain Name | 4% | 60%
12. Theme | 12% | 72%
13. Infographics/Images | 8% | 80%
14. Video Content | 4% | 84%
15. Comments/Likes | 1% | 85%
16. RSS Feed | 2% | 87%
17. Hooks/Social Media | 12% | 99%
18. A/B Testing | 1% | 100%

Attacking all fo these concepts at once seems like a fairly difficult task, so I narrowed my work down to just the most valuable concepts:

Blog Concept | Percentage Value | Total Value
---|---|---
1. Content | 15% | 15%
2. Theme | 12% | 27%
3. Hook/Social Media | 12% | 39%
4. Publishing on a Schedule | 10% | 49%

So it looks like I can get about half my value from just 4 core concepts. This analysis also helps me determine that the "posting platform" (*i.e.* Wordpress) is not important. Instead of focusing on the posting platform itself, I should find a platform that is good at handling a theme and easy to maintain.

### Platform Research: Jekyll

I have written a few blogs before, and this time I want to try Jekyll. Jekyll is a command line tool instead of a visual tool like Wordpress. I think long-term it might be easier to maintain than a Wordpress blog. I also like the idea of the site being completely persisted on my Raspberry Pi, and then mirrored into the cloud. This means I can close down the site, store it on GitHub, and upload it somewhere else with ease.

To download Jekyll on the Raspberry Pi, I went to the Ubuntu install docs and followed the steps. Then, I just followed the last three steps of the quick start guide. Here are the links:

* [Install Jekyll on Linux](https://jekyllrb.com/docs/installation/ubuntu)
* [Jekyll Quickstart Guide](https://jekyllrb.com/docs)

For a theme, I looked at some gem themes after finding a Youtuber that had some pretty good Jekyll tutorials. Here is his video:

* [Youtube Tutorial on Jekyll Themes](https://youtu.be/NoRS2D-cyko)

### Tracking Hooks and Social Media

After creating some content, the only way to get that content to people is to use hooks or ads on social media. These hooks or "click bait" lines are the only thing that convince people to click the link to the content that was posted. Some hooks work better than others, so keeping track of these hooks can provide valuable information on what works and what doesn't.

Jekyll posts are written in a format called markdown. The markdown format allows for metadata (called "front matter") to be stored at the top of a file. We can store the "hook" that is used for a post in the front matter of that post.

Next, even if the same hook is used in every forum and channel on social media, the click conversion rate for each social media site will still vary. To track the click conversion rate of each social media site, I'll add campaign parameters to the URL of the post for each different forum that I post in. Google Analytics comes with the ability to track referring sources, but you can also add three parameters to the end of your url to add additional data about your reference. They are: 

* utm_source
* utm_media
* utm_campaign

So as an example you might see this in the url:

`https://www.example.com?utm_source=summer-mailer&utm_medium=email&utm_campaign=summer-sale`
 
Once we have metadata on the referring source, we can also use "event measurements" in Google Analytics to give a very clear idea of which referrers are giving the best conversions. Finally, the Google Analytics UI isn't great, so it's a good idea to plan to pull this data into Snowflake using Stitch data or an open source integration tool that we haven't built yet.

Once all of our data is in Snowflake, we can generate reports on user behavior and find out where users are dropping off in our funnel.

### Scheduling

When creating a blog, consistency is key. Creating a publishing schedule can help with publishing consistent content. This concept is talked about in depth by a blogger named Neil Patel: 

* [How To Start A Blog by Neil Patel](https://neilpatel.com/how-to-start-a-blog)

The Raspberry Pi comes with Libre Spreadsheet software, but I think I'm going to use the recommended software of Google Sheets hooked up to Google Calendar. This will allow me to connect all of this data with Snowflake later on. The columns of the Publishing Schedule table include:

* Publishing Date
* Title
* Keyword
* Status

*Note: Status has 7 discrete possibilities: schedule, drafted, reviewed, hook created, campaign created, published, analytics reported.*

### Hosting

The last thing I need is hosting. Now, the cheapest way to host a blog would be through GitHub pages. I tried out GitHub Pages in preparation for this post, and it just seems like a more difficult experience than hosting with S3 Buckets. The AWS documentation is horrible, but once you figure it out,the tool is extremely powerful. I found a decent blog article on how to install the AWS CLI client and an AWS Live Coding video on hosting a Jekyll blog in an S3 bucket:

* [Blog on Installing AWS CLI on Raspberry Pi](https://iotbytes.wordpress.com/aws-iot-cli-on-raspberry-pi)
* [Live Coding with AWS: Efficient Content Delivery](https://www.youtube.com/watch?v=CDLW9llfbn0)

AWS has a command line utility that allows you to type a single command, and your local website gets uploaded to the cloud.

`aws s3 sync --region=<region> <source-folder> s3://<destination-bucket> --acl=public-read`

One last problem with this solution, is it's not easy to host a domain on AWS without using their DNS called Route53. I'll give Route53 a try, and that should be it.

There is a lot of content here to digest, but this strategy is a maintainable, long-term solution for working on a blog with a group of other people. If you are interested in setting something like this up, feel free to subscribe, and I will reach out to you.
