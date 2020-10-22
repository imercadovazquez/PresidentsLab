import pytest
import requests


url_ddg = "https://api.duckduckgo.com/?q=presidents of the united states&format=json&pretty=1"


def test_ddg0():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    a = False
    for item in rsp_data['RelatedTopics']:
        if "Lincoln" in item['Text']:
            a = True
            return
    assert a == True


@pytest.mark.parametrize("president", ['Washington', 'Adams', 'Jefferson', 'Madison',
                                  'Monroe', 'Jackson', 'Buren', 'Harrison',
                                  'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce',
                                  'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes',
                                  'Garfield', 'Arthur','Cleveland', 'McKinley', 'Roosevelt',
                                  'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover',
                                  'Roosevelt', 'Truman', 'Eisenhower','Kennedy', 'Nixon',
                                  'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Obama',
                                  'Trump'])
def test_ddg1(president):
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    a = False
    for item in rsp_data['RelatedTopics']:
        if president in item['Text']:
            a = True
            return            
    assert a == True


