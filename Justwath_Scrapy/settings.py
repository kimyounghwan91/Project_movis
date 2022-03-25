# Scrapy settings for Justwath_Scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Justwath_Scrapy'

SPIDER_MODULES = ['Justwath_Scrapy.spiders']
NEWSPIDER_MODULE = 'Justwath_Scrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Justwath_Scrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# 병렬 처리. 주석처리면 기본 16으로 설정됨
# Scrapy 다운로더가 수행 할 최대 동시 (즉, 동시) 요청 수
CONCURRENT_REQUESTS = 12

# 다운로드 딜레이
# 웹 사이트에서 연속 페이지를 다운로드하기 전에 다운로더가 기다려야하는 시간 (초)
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:

# 웹 사이트 도메인 동시 병렬 처리 개수
CONCURRENT_REQUESTS_PER_DOMAIN = 3
# 특정 웹 사이트 IP 주소 병렬 처리 개수
#CONCURRENT_REQUESTS_PER_IP = 16


# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Justwath_Scrapy.middlewares.JustwathScrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Justwath_Scrapy.middlewares.JustwathScrapyDownloaderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
}


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Justwath_Scrapy.pipelines.JustwatchCsvPipeline': 300,
   # 'Justwath_Scrapy.pipelines.MySQLPipeline' : 800,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 3
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3000
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


DUPEFILTER_CLASS ='scrapy.dupefilters.BaseDupeFilter'
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]
HTTPERROR_ALLOWED_CODES = [404]

#csv 저장시 순서 정렬

FEED_EXPORT_FIELDS = ["title_kor" , "opening_date" , "just_rating" , "imdb_rating" , "runtime" , "synopsis" , "director" , "actors" , "genre" , "posterLink"]