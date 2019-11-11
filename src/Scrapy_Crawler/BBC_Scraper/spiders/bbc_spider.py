import scrapy
from BBC_Scraper.items import BbcScraperItem
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

class BBCSpider(CrawlSpider):
    name  = "bbcScraper"
    allowed_domains = ['bbc.com']

        # Return an iter of requests
    def get_start_urls():
        groups_list = ['india', 'international', 'entertainment', 'sport', 'science', 'social']
        start_urls = ["https://www.bbc.com/hindi/"+group for group in groups_list]
        return start_urls

    start_urls = get_start_urls()

    rules = [
                Rule(
                    LinkExtractor(
                        canonicalize=True,
                        unique=True
                    ),
                    follow = True,
                    callback = "parse_news_pages"
                    )
            ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # def parse(self, response):
        # page = response.url.split("/")[-1]
        # filename = 'scraped_files/%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        #
        # for selector_type in ["//*[@class='faux-block-link__overlay-link']","//*[@class='bold-image-promo']"]:
        #     for url_box in response.xpath(selector_type):
        #         item = BbcScraperItem()
        #         url = url_box.xpath("@href").get()
        #         if url is not None:
        #             print(url)
        #             if url.startswith('http'):
        #                 item['url'] = url
        #             elif url.startswith('www'):
        #                 item['url'] = 'https://'+url
        #             else: #Relative path
        #                 item['url'] = 'https://www.bbc.com' + url
        #         request = scrapy.Request(item['url'],callback = self.parse_article)
        #         request.meta['item'] = item
        #         yield request

    def parse_news_pages(self, response):
        items = []
        # Only extract canonicalized and unique links (with respect to the current page)
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)

        for link in links:
                is_allowed = False
                for allowed_domains in self.allowed_domains:
                        if allowed_domains in link.url:
                                is_allowed = True

                if is_allowed:
                        item = BbcScraperItem()
                        item['url'] = response.url

                        title = response.xpath("//*[@class='story-body__h1']/text()").extract_first()
                        item['title'] = title

                        NewsContent = response.xpath("//*[@class='story-body__inner']/p/text()").extract()
                        news_content = ('\n'.join(NewsContent))
                        item['content'] = news_content

                        date = response.xpath("//*[@class='date date--v2']").xpath("@data-datetime").get()
                        item['time'] = date

                        items.append(item)
        return items
        # Only extract canonicalized and unique links (with respect to the current page)
        # page = response.url.split("/")[-1]
        # print(page)
        # filename = 'scraped_files/%s.html' % page
        # self.log('Saved file %s' % filename)
        # for selector_type in ["//*[@class='unit__link-wrapper']"]:
        #     for url_box in response.xpath(selector_type):
        #         item = BbcScraperItem()
        #         url = url_box.xpath("@href").get()
        #
        #         if url is not None:
        #             if url.startswith('http'):
        #                 item['url'] = url
        #             elif url.startswith('www'):
        #                 item['url'] = 'https://'+url
        #             else: #Relative path
        #                 item['url'] = 'https://www.bbc.com' + url
        #             request = scrapy.Request(item['url'],callback = self.parse_article)
        #             request.meta['item'] = item
                # yield request


    # def parse_article(self,response):
    #     item = response.meta['item']
    #     item = self.getNewsDetails(item, response)
    #     item['url'] = response.url
    #     return item
    #
    # def getNewsDetails(self,item,response):
    #     title = response.xpath("//*[@class='story-body__h1']/text()").extract_first()
    #     item['title'] = title
    #
    #     NewsContent = response.xpath("//*[@class='story-body__inner']/p/text()").extract()
    #     news_content = ('\n'.join(NewsContent))
    #     item['content'] = news_content
    #
    #     date = response.xpath("//*[@class='date date--v2']").xpath("@data-datetime").get()
    #     item['time'] = date
    #     # Before returning to the item
    #     self.parse_news_pages(response)
    #
    #     return item
