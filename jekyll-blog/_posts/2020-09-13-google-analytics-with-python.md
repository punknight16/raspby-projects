---
layout: default
hook: Hi all, I added to Raspby Projects this week by creating an open source python project to generate funnel charts from Google Analytics Data.
utm_urls:
- https://raspbyprojects.com?utm-source=fwd-discord
- https://raspbyprojects.com?utm-source=kya-slack
- https://raspbyprojects.com?utm-source=gatech-gchat
- https://rapsbyprojects.com?utm-source=hackernews
- https://raspbyprojects.com?utm-source=r/dataengineering
- https://raspbyprojects.com?utm-source=dataengineering-discord
- https://raspbyprojects.com?utm-source=startups-discord
- https://raspbyprojects.com?utm-source=r/sideprojects
---
# Generating Weekly Funnel Charts from GA Data

<div style="display:flex; justify-content: center"><iframe width="560" height="315" src="https://www.youtube.com/embed/FY2BjUY5IVg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

### Introduction
The project I am working on this week is a very simple business analytics platform. I specifically want to create a funnel report on a weekly basis. The top of the funnel should start with unique views and the bottom of the funnel should be a conversion metric (like the number of subscribers). I want to be able to compare my current reports to my past reports in order to see how the blog has grown or shrunk over time. This could lead to data driven decisions when comparing these reports to the publishing schedule that I am also maintaining.

This project didn't just come to me. I have actually been working on a data analytics product called Structure for the past few months. Structure is a very useful tool for non-technical teams. Each person on a cross-functional team can use the visual interface of Structure to understand the KPIs of everyone else, and get the lineage of how any data model was derived. 

For the tool I'm building this week however, I'm not building for a large team. I'm only building for a single, technical user. I need to decide on the core components of this project from that point of view.

### Core Component Analysis

The only goal of this project is to show a funnel plot as described above. To get there, I need to decide what ELT tooling is necessary and what ELT tooling is just fluff. Here's what my core component analysis looks like for this project:

Component | % Value | Total Value
---|---|---
1. Data Sources | 10% | 10%
2. Extract Tool | 8% | 18%
3. Validate Raw Data | 2% | 20%
4. Load Tool | 8% | 28%
5. Store Raw Data | 18% | 46%
6. Transform Tool | 10% | 56%
7. Visualizations | 18% | 74%
8. Scheduler | 8% | 82%
9. Persisting Reports | 12% | 94%
10. Data Monitoring | 4% | 98%
11. Data Characterization | 2% | 100%

From this analysis, I can pretty clearly see what is necessary to capture the majority of the value.

Component | % Value | Total Value
---|---|---
1. Data Sources | 10% | 10%
5. Store Raw Data | 18% | 28%
6. Transform Tool | 10% | 38%
7. Visualizations | 18% | 56%
9. Persisting Reports | 12% | 68%

That is 68% of the value for building out five features. Automation through a scheduler would be really useful long term, but for a proof-of-concept, I think manually generating the reports is fine.

Before we jump into the technical research, I need to go over some of the business questions first.
* Do I need to actually build anything or can I bootstrap this product by bundling an existing kit of services?
* Can a user implement this tool in their current workflow or would they have to create a new behavior?

### Stitch Data

As an initial answer to my first question, I immediately thought of Stitch. Stitch can move data from my data sources into an S3 bucket, which I already have the infrastructure set up for. This basically takes care of steps 1 and 5 in my component analysis. Being able to access the raw data at any time, allows me to avoid persisting any intermediate transformations of my data. I can just go from raw data to visualization. The metrics in my Google Analytics API might change from week-to-week, but once the raw data is persisted, I have a snapshot of what my data looked like at a specific period in time. Here is a link to Stitch for those interested:

* [Stitch Data](https://stitchdata.com)

### Using Python Libraries for Everything Else

When I started searching for services that could generate funnel plots, I quickly noticed that I was given two distinct paths. The first was to pay for a data warehouse service (like Snowflake) and connect that up to a visualization tool (like Tableau). If I was running a large business, this is absolutely the best path to go, but this is a small side-project that I want to spend as little time maintaining as possible.

The second choice was to use a set of Python libraries to generate the results I wanted. Working backwards based on my business requirements, I found Plotly as a visualization tool, PANDAs as a transformation tool, and Boto3 as an SDK for extracting my S3 data programmatically. Python comes pre-installed on a Raspberry Pi, so this felt like a great option for this project. Installing the libraries was as simple as 3 commands:

* `pip3 install boto3`
* `pip3 install pandas`
* `pip3 install plotly`

Once I finished my research, I started to map out the high-level abstract classes I would need to keep this project organized and extensible. In my first pass, I had a simple "main" class and then an Inquirer (std.in) class, a getDataFromS3 class, a Transform class, and a Visualization Class. As I dug deeper into the project, I updated these classes accordingly.

### UPDATED High-level Abstract Classes
* main
* inquirer -> get("year", "week") from user
* extract -> get data from s3 and put in file
* load -> get data from file and put in main
* transform -> create DataFrame, filter, and aggregate
* plot -> visualize and export html file

Based on the week-by-week nature of Raspby Projects, I hadn't really though through how the program would choose which week to create a plot for. Because I wanted to keep the app simple, I decided to just let the Inquirer class request the year and week from the user, and then generate both the report and the filename of the report using that input. If I only allowed the app to create a plot for the most recent week, I wouldn't have been able to generate plots for past weeks that I had missed or regenerate plots if needed.

### A list of Tutorials and Resources I used for this project

At the beginning of this project, I hadn't used Python more than once or twice. My friend had previously given me a Python reference book that proved extremely helpful. Other than that, I used a bunch of tutorials, documentation, and stack overflow to cobble together this project:

* [Python Main Function](https://realpython.com/python-main-function)
* [Python Boto3 AWS s3](https://realpython.com/python-boto3-aws-s3)
* [Plotly Funnel Charts](https://plotly.com/python/funnel-charts)
* [Plotly Renderers](https://plotly.com/python/renderers)
* [Tutorial that Uses Pandas](https://canonicalized.com/google-analytics-python-pandas-plolty)

If you like this project, please star it on Github. You can click the button at the top of the page to jump to this GitHub repo.
