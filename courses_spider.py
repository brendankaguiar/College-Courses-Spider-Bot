import scrapy

class CoursesSpider(scrapy.Spider):
    name = "courses"

    def start_requests(self):
        url = 'https://catalog.unr.edu/preview_degree_planner.php?catoid=24&poid=17619&print'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #write html file
        filename = f'{self.name}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        #parse HTML using scrapy xpath/css methods
        encoding = 'utf-8'
        main_class(response.body.decode(encoding))

def main_class(doc):#HTML doc as input
    print(doc)
    #parse HTML using python string/list methods
