import scrapy


class JustwatchItem(scrapy.Item):

    title_kor = scrapy.Field()
    opening_date = scrapy.Field()
    just_rating = scrapy.Field()
    imdb_rating = scrapy.Field()
    runtime = scrapy.Field()
    synopsis = scrapy.Field()
    director = scrapy.Field()
    actors = scrapy.Field()
    genre = scrapy.Field()
    posterLink = scrapy.Field()