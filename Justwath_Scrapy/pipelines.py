from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter, XmlItemExporter, JsonItemExporter
from imp import reload
import os
BASE_PATH = None
def in_ipynb():
    try:
        cfg = get_ipython().config
        return True
    except NameError:
        return False
def setBasePath():
    import os
    global BASE_PATH
    condition = in_ipynb()
    if condition == True:
        BASE_PATH = os.path.dirname(os.path.abspath(""))
    elif condition == False:
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
setBasePath()
temp_path = os.path.join(BASE_PATH, "..", "moviedata", "MovieCrawlerFile.csv")

class JustwatchCsvPipeline(object):
    def __init__(self):
        self.file = open(temp_path, 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
 
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item