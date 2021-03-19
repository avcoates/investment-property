# About This Project

## Motivation:

I want to purchase a so called "House Hack", where you buy a 1-4 family property,
live in one room and rent out the other rooms/units.

As a first time buyer, there are a good amount of variables to take into account when considering a property.
This information is on the multi listing site that my realator gave me access to.
There is one problem, my buyer portal does not give me access to the tools available to the agent.
I can not export search results to a csv file!

So what can I do?
I first started copying and pasting property information into a google sheet.
That went ok for a week as I put in the properties that seems most attractive at first glance,
but this was taking far too long.
Next I looked up my MLS and noticed that the agent portal has an export to csv option.
I could get my realator to supply me with this file, say, once a week, but I didn't want to wait
and I wanted more frequent updates than that.

## My Solution:

### Part one
Create a web scrapper for my MLS using python.
This scrapper is meant to be ran daily. It creates a csv file
for each saved search (I am looking in a few locations) and spits all the listings
to the file.

### Part two
Read each daily report file and calculate the most attractive properties.
*more details on calculations*

### Part three
Trigger this report when I get my daily email with new or status changed properties.


## Outcomes and What I Learned:
Firstly, i'd like to say how much I appreciated this little project.
It made me feel like I was in college again writing a nifty little program.

The power of web scrapping is crazy. It was awesome to learn this.
I am lucky and the MLS for the most part did not seem to care about
a scrapper on this site, but I still throttled the requests because that 
seemed to be the only thing that made it stop my requests.

The chances of this scrapper breaking are coupled to the chances of
the html output and url structure changing. Relying on that seems very
volitile and a high liklyhood of breaking, but im sure thats the nature
of web scrapping itself. It isn't an API.

Next steps are learning more about web scrapping and using proxies as this
almost seems neccessary for any other project.
