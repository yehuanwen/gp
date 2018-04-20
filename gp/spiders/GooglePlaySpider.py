import scrapy
from gp.items import ProductItem, GPReviewItem
from urllib import parse
import time
import re


class GooglePlaySpider(scrapy.Spider):
    name = 'gp'
    allowed_domains = ['play.google.com']

    def __init__(self, *args, **kwargs):
        urls = kwargs.pop('urls', [])  # 获取参数
        if urls:
            self.start_urls = urls.split(',')
            print('start urls = ', self.start_urls)

    def parse(self, response):
        print('Begin parse ', response.url)

        item = ProductItem()

        item['updated_at'] = int(time.time())

        content = response.xpath('//div[@class="LXrl4c"]')

        exception_count = 0

        try:
            item['gp_icon'] = response.urljoin(content.xpath('//img[@class="T75of ujDFqe"]/@src')[0].extract())
        except Exception as error:
            exception_count += 1
            print('gp_icon except = ', error)
            item['gp_icon'] = ''

        try:
            item['gp_name'] = content.xpath('//h1[@class="AHFaub"]/span/text()')[0].extract()
        except Exception as error:
            exception_count += 1
            print('gp_name except = ', error)
            item['gp_name'] = ''

        try:
            item['gp_tag'] = content.xpath('//a[@itemprop="genre"]/text()')[0].extract()
        except Exception as error:
            exception_count += 1
            print('gp_tag except = ', error)
            item['gp_tag'] = ''

        item['gp_url'] = response.url

        try:
            show_more_content = content.xpath('//div[@jsname="sngebd"]/text()').extract()
            app_introduction = ''
            for more in show_more_content:
                app_introduction = app_introduction + more + '\n'
            item['gp_intro'] = app_introduction.strip('\n')
        except Exception as error:
            exception_count += 1
            print('gp_intro except = ', error)
            item['gp_intro'] = ''

        try:
            item['gp_developer'] = content.xpath('//a[@class="hrTbp R8zArc"]/text()')[0].extract()
        except Exception as error:
            exception_count += 1
            print('gp_developer except = ', error)
            item['gp_developer'] = ''

        try:
            gp_rating = content.xpath(
                '//div[@class="BHMmbe"]/text()')[
                0].extract()
            item['gp_rating'] = gp_rating.replace(',', '.')
        except Exception as error:
            exception_count += 1
            print('gp_rating except = ', error)
            item['gp_rating'] = ''

        try:
            parse_result = parse.urlparse(response.url)
            params = parse.parse_qs(parse_result.query, True)

            item['gp_package'] = params['id'][0]
        except Exception as error:
            exception_count += 1
            print('gp_package except = ', error)
            item['gp_package'] = ''

        try:
            thumbnails = content.xpath('//div[@class="NIc6yf"]/img/@src').extract()
            gp_picture = ''
            for thumbnail in thumbnails:
                gp_picture = gp_picture + response.urljoin(thumbnail) + ','
            item['gp_picture'] = gp_picture.strip(',')
        except Exception as error:
            exception_count += 1
            print('gp_picture except = ', error)
            item['gp_picture'] = ''

        try:
            if len(content.xpath('//div[@class="xyOfqd"]/div/div[2]/span/text()')) > 0:
                item['gp_update'] = content.xpath('//div[@class="xyOfqd"]/div/div[2]/span/text()')[0].extract()
            else:
                item['gp_update'] = ''
        except Exception as error:
            exception_count += 1
            print('gp_update except = ', error)
            item['gp_update'] = ''

        try:
            recent_change = content.xpath(
                '//div[@class="DWPxHb"]/content/text()').extract()
            gp_news = ''
            for change in recent_change:
                gp_news = gp_news + change + '\n'
            item['gp_news'] = gp_news.strip('\n')
        except Exception as error:
            exception_count += 1
            print('gp_news except = ', error)
            item['gp_news'] = ''

        try:
            item['gp_version'] = \
                content.xpath('//div[@class="xyOfqd"]/div[4]/span/div/span/text()')[
                    0].extract().strip()
        except Exception as error:
            exception_count += 1
            print('gp_version except = ', error)
            item['gp_version'] = ''

        try:
            item['gp_downloads'] = \
                content.xpath('//div[@class="xyOfqd"]/div[3]/span/div/span/text()')[
                    0].extract().strip()
        except Exception as error:
            exception_count += 1
            print('gp_downloads except = ', error)
            item['gp_downloads'] = ''

        try:
            if len(content.xpath('//div[@class="MSLVtf NIc6yf"]/img/@src')) > 0:
                item['gp_video_image'] = response.urljoin(
                    content.xpath('//div[@class="MSLVtf NIc6yf"]/img/@src')[0].extract())
            else:
                item['gp_video_image'] = ''
        except Exception as error:
            exception_count += 1
            print('gp_video_image except = ', error)
            item['gp_video_image'] = ''

        try:
            if len(content.xpath('//button[@class="lgooh  "]/@data-trailer-url')) > 0:
                item['gp_video_url'] = content.xpath('//button[@class="lgooh  "]/@data-trailer-url')[
                    0].extract()
            else:
                item['gp_video_url'] = ''
        except Exception as error:
            exception_count += 1
            print('gp_video_url except = ', error)
            item['gp_video_url'] = ''

        try:
            featured_review = response.xpath('//div[@jscontroller="H6eOGe"]')
            reviews = []
            for featured in featured_review:
                avatar_url = featured.xpath('div/div[1]/img[@class="T75of oRT0Bc"]/@src')[
                    0].extract()

                user_name = featured.xpath('div/div[2]/div[1]/div[1]/span/text()')[0].extract().strip()

                rating_star = featured.xpath('div/div[2]/div[1]/div[1]/div/span[1]/div/div/@aria-label')[
                    0].extract()
                rating_star = re.search(r"\d+", rating_star).group(0)

                review_text = featured.xpath(
                    'div/div[2]/div[1]/div[1]/span/text()').extract()
                review_text = "".join(list(review_text)).strip()

                review = GPReviewItem()
                review['avatar_url'] = avatar_url
                review['user_name'] = user_name
                review['rating_star'] = rating_star
                review['review_text'] = review_text

                reviews.append(review)

            item['gp_review'] = reviews
        except Exception as error:
            exception_count += 1
            print('gp_review except = ', error)
            item['gp_review'] = ''

        if exception_count >= 3:
            print('spider_failure_parse_too_much_exception')
            return

        yield item

