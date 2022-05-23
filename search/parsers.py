from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
from requests import get
import re


MAX_PER_SITE = 10
TORRENT_MASK = 'magnet:?'


class Parser(ABC):
    @staticmethod
    @abstractmethod
    def parse(response):
        pass


class PirateBayParser(Parser):
    @staticmethod
    def check_td_href(tag):
        return tag.find('div', class_='detName')

    @staticmethod
    def parse(response):
        soup = BeautifulSoup(response, 'html.parser')
        return [
           {
            'title': i.find('div', class_='detName').find('a')['title'],
            'link': i.find(href=re.compile('magnet:?'))['href']
           }
            for i in soup.find_all('td')
            if PirateBayParser.check_td_href(i)
        ][:MAX_PER_SITE]


class One337xParser(Parser):
    @staticmethod
    def parse(response):
        pass

    @staticmethod
    def parse_inner_link(response):
        soup = BeautifulSoup(response, 'html.parser')

        return [
            i['href']
            for i in soup.find_all(href=re.compile('/torrent/'))
        ]


