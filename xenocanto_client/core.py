"""
advanced query tags:
    'gen': genus
    'rec': recordist
    'cnt': country
    'loc': location
    'rmk': recordist remarks
    'lat': latitude +- one degree
    'lon': longitude +- one degree
    'box': LAT_MIN,LON_MIN,LAT_MAX,LON_MAX
    'also': species in the background
    'type': song vs call
    'nr': catalog number
    'q': exact quality
    'q<': quality lower than
    'q>': quality greater than
    'q': 0 - unrated quality
    'area': africa america asia australia europe
    'since': number of days that have passed since recording
    'year': recordings from given year
    'month': recordings from given month
"""
import urllib.parse
import requests

baseurl = 'http://www.xeno-canto.org/api/2/recordings'


def generate_query_string(basic_query, adv_query_dict):
    """
    :param basic_query: basic query string (eg. 'blue jay')
    :param adv_query_dict: advanced query dict (eg. {'cnt': 'brazil'})
    :return: urlencoded query string for xeno-canto (eg.
    """
    query_string = ''
    adv_query_string = adv_query_dict_to_string(adv_query_dict)

    if basic_query:
        query_string += basic_query

        if adv_query_string:
            query_string += ' ' + adv_query_string

    elif adv_query_string:
        query_string += adv_query_string

    return urllib.parse.quote(query_string, safe=':')


def request_results(basic_query, adv_query_dict):
    """
    :param basic_query: basic query string (eg. 'blue jay')
    :param adv_query_dict:  advanced query dict (eg. {'cnt': 'brazil'})
    :return:
    """

def adv_query_dict_to_string(query_dict):
    return ' '.join(['{}:{}'.format(key, value) for (key, value) in query_dict.items()])
