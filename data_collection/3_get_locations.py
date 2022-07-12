import scrapy
import requests
import json
import re
from scrapy.crawler import CrawlerProcess

class LocationSpider(scrapy.Spider):
    name = "loc_spider"

    def __init__(self, data, *args, **kwargs):
        super(LocationSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get('start_urls')
        self.y = kwargs.get('year')
        self.data = data
        self.venues = kwargs.get('venue')

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield scrapy.Request(url, callback=self.parse, cb_kwargs={'year':self.y[i], 'venue':self.venues[i]})


    def parse(self, response, year, venue):
        for y in year:
            for sel in response.xpath('//html//header//h2[@id="'+y+'"]'):
                self.data.append([sel.xpath('text()').extract()[0], venue, y])

def getCity(element):
    data1 = element.split()
    k = [l for l in data1 if l.endswith(":")]
    if not k:
        return ('', '')
    index1 = data1.index(k[0])
    loc = data1[index1+1:]
    characters = ['[', ']', ')', '(', '/']
    pattern = re.compile("[Oo]nline|[Ee]vent|Virtual|/")
    newloc = ''
    for e in loc:
        if not (pattern.match(e)):
            for i in characters:
                e = e.replace(i, '')
            newloc = newloc + ' ' + e
    data2 = newloc.split(',')
    city = data2[0][1:]
    country = data2[-1][1:]
    if city == country:
        return '', country
    return city, country

def getLoc(filename):
    f = open(filename)
    data = json.load(f)
    venues = []
    years = []
    urls = []
    for i, e in enumerate(data):
        if e['type'] == 'Conference and Workshop Papers':
            if e['venue'] not in venues:
                venues.append(e['venue'])
                urls.append(e['url'])
                years.append([e['year']])
            else:
                index = venues.index(e['venue'])
                if e['year'] not in years[index]:
                    years[index].append(e['year'])
    data = []
    process = CrawlerProcess()
    process.crawl(LocationSpider, data, start_urls=urls, year=years, venue=venues)
    process.start()
    locations = []
    for e in data:
        location = getCity(e[0])
        if location:
            locations.append([e[1], e[2], location[0], location[1]])
    return locations

def getConferenceInformation(title, types, venues, years):
    originalTitle = title
    newtitle = title.split()
    title = ""
    characters = ["(", ".", "[", "'"]
    for e in newtitle:
        if not any(i in e for i in characters):
            title += " " + e
    title = title.replace("-", " ")
    title = title.replace(":", " ")
    title = title.replace("/", " ")
    title = title.replace("&#146;", "")
    response = requests.get("https://dblp.org/search/publ/api?q=title:"+title+"&format=json")
    response = response.json()
    if response['result']['hits']['@total'] == '0':
        return venues, str(years), None, types, originalTitle
    elif response['result']['hits']['@total'] > '1':
        response = response['result']['hits']['hit'][1]['info']
    else:
        response = response['result']['hits']['hit'][0]['info']
    venue_type = response['type']
    try:
        venue = response['venue']
    except KeyError as ve:
        return venues, str(years), None, types, originalTitle
    year = response['year']
    url = response['key']
    index = url.rindex("/")
    url = url[:index+1]
    url = "https://dblp.org/db/" + url + "index.html"
    return venue, year, url, venue_type, originalTitle

def writeVenues(venues, file_name):
    aList = []
    for e in venues:
        aList.append({'title':e[4], 'type':e[3], 'venue':e[0], 'year':e[1], 'url':e[2]})
    jsonString = json.dumps(aList)
    jsonFile = open(file_name, "w")
    jsonFile.write(jsonString)
    jsonFile.close()

def writeLocations(locations, file_name):
    aList = []
    for e in locations:
        aList.append({'venue':e[0], 'year':e[1], 'city':e[2], 'country':e[3]})
    jsonString = json.dumps(aList)
    jsonFile = open(file_name, "w")
    jsonFile.write(jsonString)
    jsonFile.close()

def getAllTitles(url):
    resp = requests.get(url)
    data = json.loads(resp.text)
    titles = []
    types = []
    venues = []
    years = []
    for e in data:
        titles.append(e["title"])
        years.append(e["publication_year"])
        types.append(e["host_venue"]["type"])
        venues.append(e["host_venue"]["display_name"])
    return titles, types, venues, years

if __name__ == "__main__":
    titles, types, newvenues, years = getAllTitles('https://raw.githubusercontent.com/a-baur/IDE_Projekt/master/data_collection/2_get_works_output/tuhh.json')
    venues = []
    for i, e in enumerate(titles):
        a = getConferenceInformation(e, types[i], newvenues[i], years[i])
        venues.append(a)
    writeVenues(venues, "venues_tuhh.json")
    locations = getLoc("venues_tuhh.json")
    writeLocations(locations, "locations_tuhh.json")

    titles, types, newvenues, years = getAllTitles('https://raw.githubusercontent.com/a-baur/IDE_Projekt/master/data_collection/2_get_works_output/uhh.json')
    venues = []
    for i, e in enumerate(titles):
        a = getConferenceInformation(e, types[i], newvenues[i], years[i])
        venues.append(a)
    writeVenues(venues, "venues_uhh.json")
    locations = getLoc("venues_uhh.json")
    writeLocations(locations, "locations_uhh.json")

    titles, types, newvenues, years = getAllTitles('https://raw.githubusercontent.com/a-baur/IDE_Projekt/master/data_collection/2_get_works_output/haw.json')
    venues = []
    for i, e in enumerate(titles):
        a = getConferenceInformation(e, types[i], newvenues[i], years[i])
        venues.append(a)
    writeVenues(venues, "venues_haw.json")
    locations = getLoc("venues_haw.json")
    writeLocations(locations, "locations_haw.json")
