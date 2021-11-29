import feedparser

rss_url = 'https://reddit.com/.rss'
parser =feedparser.parse(rss_url)

for entry in parser.entries:
    print(entry.title)
    print(entry.links[0].href)
    print(entry.content[0].value)
    print('________________________')

