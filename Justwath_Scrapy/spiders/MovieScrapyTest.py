# import imp, time, sys, requests, scrapy
# from pytest import yield_fixture
# from Justwath_Scrapy.items import JustwatchItem
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from scrapy import signals
# from scrapy.http import TextResponse, HtmlResponse
# from itemadapter import is_item, ItemAdapter
# from scrapy.utils.python import to_bytes
# from selenium.webdriver.chrome.options import Options
# from time import sleep
# from fake_useragent import UserAgent
# from .movie_datas import *



# class MovieScrapyTestSpider(scrapy.Spider):
#     name="MovieScrapyTest"
#     custom_settings = {
#         'DOWNLOADER_MIDDLEWARES': {
#         'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#         'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,        
#         }
#     }
#     categ = {
#         'netflix':"넷플릭스",
#         'disney-plus':'디즈니플러스',
#         'watcha':'왓챠',
#         # 'wavve':'웨이브'
#     }
#     def start_requests(self):
#         all_category_urls = []
#         for category in self.categ.keys():
#             all_category_urls.append(get_urls(category))
        
#         for urls in all_category_urls:
#             for url in urls:
#                 yield scrapy.Request(url, callback=self.link_parse)
#             time.sleep(10)

#         # for year in map(str,range(2004,2006)):
            
#         #     ss = 'https://www.justwatch.com/kr/%EB%8F%99%EC%98%81%EC%83%81%EC%84%9C%EB%B9%84%EC%8A%A4/{}?content_type=movie&release_year_from={}&release_year_until={}'.format(category,year, year)
#         #     urls.append(ss)
#         # for url in urls:
#         #     yield scrapy.Request(url, callback=self.link_parse)


#     def link_parse(self, response):
#         path_chrome = r'C:\Workspace\AtHome\Justwath_Scrapy\webdriver\chromedriver_win32_99\chromedriver.exe' 
#         chrome_options = Options()
#         # chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-gpu")

#         # driver.maximize_window()
#         driver = webdriver.Chrome(executable_path=path_chrome, chrome_options=chrome_options)
#         driver.get(response.url)
#         start = time.time()
#         driver.implicitly_wait(10)
#         counter = driver.find_element_by_class_name("total-titles").text


#         last_height = driver.execute_script("return document.body.scrollHeight")
#         while True:
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             sleep(2)
#             new_height = driver.execute_script("return document.body.scrollHeight")
#             if new_height == last_height:
#                 break
#             last_height = new_height
#             wait=WebDriverWait(driver, 3)

#         try:
#             # ID가 myDynamicElement인 element가 로딩될 때 까지 10초 대기
#             element = WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "filter-bar__reset-button"))
#             )
        
#             end = time.time()

#         except TimeoutException:
#             # 실패 시에는 에러메시지로 Time Out 출력
#             print('Time Out')

#         print("끝")

#         # 영화링크수집
#         elem = driver.find_elements_by_css_selector('div.title-list-grid div.title-list-grid__item a.title-list-grid__item--link')
#         linkUrls = []
#         for e in elem:
#             linkUrl = e.get_attribute('href')
#             linkUrls.append(linkUrl)

#         # print("영화링크 수집 끝")
#         print(linkUrls)
#         driver.quit()


#         # parse로 스크랩요청
#         for i in linkUrls:
#             yield scrapy.Request(i, callback=self.parse)


#     def parse(self, response):
#         item = JustwatchItem()   
#         try:
#             item['title_kor'] = response.css("div.title-block > div > h1::text").get().strip()
#         except:
#             item['title_kor'] = None       
#         try:
#             item['opening_date'] = response.css("div.title-block > div > span::text").get().replace("(","").replace(")","").strip()        
#         except:
#             item['opening_date'] = None
#         try:
#             item['just_rating'] = response.css('div.detail-infos > div > div > div > a::text')[0].get().strip()
#         except:
#             item['just_rating'] = None
#         try:
#             item['imdb_rating'] = response.css('div.detail-infos > div > div > div > a::text')[1].get().strip()
#         except:
#             item['imdb_rating'] = None   
#         genre = response.xpath('//*[@id="base"]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/span/text()').getall()
#         genre = ",".join(genre).replace(" ","")
#         item['genre'] = genre
#         runtime = response.xpath('//*[@id="base"]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[2]/text()').getall()
#         runtime = ",".join(runtime).replace(" ","")
#         item['runtime'] = runtime
#         director = response.xpath('//*[@id="base"]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/span/a/text()').getall()
#         director = ",".join(director).replace(" ","")
#         item['director'] = director
#         actors = response.xpath('//*[@id="base"]/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div/a/text()').getall() 
#         actors = ",".join(actors).replace(" ","")
#         item['actors'] = actors
        
#         try:
#             item['synopsis'] = response.xpath('//*[@id="base"]/div[2]/div/div[2]/div[2]/div/div[1]/div[4]/p/span/text()').get()
#         except:
#             item['synopsis']= None

#         item['posterLink'] = response.xpath('//*[@id="base"]/div[2]/div/div[1]/div/aside/div/div/picture').css('img').attrib['data-src'].strip()
       
#         yield item

    




        