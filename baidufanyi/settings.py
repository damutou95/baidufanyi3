# -*- coding: utf-8 -*-

# Scrapy settings for baidufanyi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'baidufanyi'

SPIDER_MODULES = ['baidufanyi.spiders']
NEWSPIDER_MODULE = 'baidufanyi.spiders'
SPLASH_URL = 'http://localhost:8050'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baidufanyi (+http://www.yourdomain.com)'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False
HEADERS = {
# 'Accept':  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# #'Accept-Encoding':  'gzip, deflate, br',
# 'Accept-Language':  'zh-CN,zh;q=0.9',
# 'Cache-Control':  'max-age=0',
# 'Connection':  'keep-alive',
# 'Cookie':  'BAIDUID=92D7E68170373AC3900003967D6B6B40:FG=1; BIDUPSID=92D7E68170373AC3900003967D6B6B40; PSTM=1546563918; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; IMG_WH=414_736; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; FEED_SIDS=71898_0129_8; SE_LAUNCH=5%3A25810970_0%3A25812087; rsv_i=43fd1Y5bX3a1CRaONILBZ27MwFA20noEKVANClc8iIUeaFak%2BuZ%2BcdLS0a2aDZEWtylWSIiuRxRqYnlJPXCk%2Bl7M9mWO%2FwI; H_WISE_SIDS=127980_126886_125818_127694_114550_127237_129070_126170_128066_127491_128853_120124_123019_128713_118879_118868_118842_118827_118789_128037_107312_126996_129180_127771_127404_129087_127768_128448_117430_128451_128818_128402_129079_129036_127029_128789_129010_128967_128247_128805_128771_127797_114819_126720_124030_128341_110085_123289_127125_128763_128807_127319_128600_127416_129251_128961_100459; PSINO=6; locale=zh; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1548725500,1548725509,1548726545,1548726559; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1548726763; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1548726545,1548726559,1548727056,1548727072; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1548727072',
# 'Host':  'fanyi.baidu.com',
# 'Referer':  'https://www.baidu.com/link?url=0cMAyE_tRRtapbq3yi2eVEXplbVOoNhL0tXtEWF0Yi_2olOu7uLpWSzkMfNXSaI9-WAih5CrGYntmOnweTh9hK&wd=&eqid=a84b878000038d1f000000065c4fab9a',
# #'Upgrade-Insecure-Requests':  '1',
'User-Agent':  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    #'baidufanyi.middlewares.BaidufanyiSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {

    'scrapy_splash.SplashCookiesMiddleware': 710,
    'scrapy_splash.SplashMiddleware': 750,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 800,
    'baidufanyi.middlewares.HttpProxyMiddleware': 850,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
#HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'baidufanyi.pipelines.BaidufanyiPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
