#!/usr/bin/env python3

import feedparser
import jinja2

def get_latest_feeds(url):
    feed_lst=[]
    feeds = feedparser.parse(url)
    count = 0
    for f in feeds['entries']:
        title = f['title']
        link = f['link']
        if count < 3:
            feed_lst.append('[{}]({})'.format(title, link))
            count += 1
        else:
           break
    return feed_lst

def template_readme(feed_lst, readme):
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = readme
    template = templateEnv.get_template(TEMPLATE_FILE)
    feed_text = ""
    for feed in feed_lst:
        feed_text += "- " + feed + "\n"
    outputText = template.render(FEEDS=feed_text)
    
    f = open(readme, "w")
    f.write(outputText)
    f.close()

def main():
    latest_feeds = get_latest_feeds('https://eoli3n.github.io/feed.xml')
    template_readme(latest_feeds, './README.md')

if __name__ == '__main__':
    main()
