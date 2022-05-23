from abc import ABC, abstractmethod
from requests import get
import json

from .parsers import (
    PirateBayParser, One337xParser,
)
sites_url = None
sites_config = 'search/sites_config.json'


with open(file=sites_config, mode='r') as fin:
    sites_url = json.load(fin)


class Loader(ABC):

    @classmethod
    @abstractmethod
    def load(cls, search_word):
        return None


class PirateBayLoader(Loader):
    SITE_DATA = sites_url['pirate_bay']
    URL = SITE_DATA['prefix']
    SUFFIX = SITE_DATA['suffix']

    PARSER = PirateBayParser

    @classmethod
    def load(cls, search_word):
        response = get(cls.URL + search_word + cls.SUFFIX)

        return cls.PARSER.parse(response=response.content)


class One337xLoader(Loader):
    SITE_DATA = sites_url['1337x']
    URL = SITE_DATA['prefix']

    PARSER = One337xParser

    @classmethod
    def load(cls, search_word):
        response = get(cls.URL + search_word)

        inner_data = cls.PARSER.parse_inner_link(response)

        return cls.PARSER.parse(inner_data)
