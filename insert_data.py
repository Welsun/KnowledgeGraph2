import os
import json
import re
from mongodb_models import Mongo

import pymongo
class InsertData:
    def __init__(self):
        cur = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        self.datapath = os.path.join(cur, 'dataset/military_weapon.json')
        self.conn = Mongo().connectDB()
        self.collection = self.conn['weapon_data']
        self.unit_dict = {
            '海里':[1852,'米'],
            '英里':[1610,'米'],
            '/节':[1852,'米'],
            'km/节':[1000,'米'],
            '吨':[1000,'千克'],
            '-吨':[1000,'千克'],
            '公里':[1000,'米'],
            '公里/节':[1000,'米'],
            '公里/小时':[1000,'米'],
            '海里节':[1852,'米'],
            '海里，节':[1852,'米'],
            '海里/节':[1852,'米'],
            '海哩/节':[1852,'米'],
            '海浬/节':[1852,'米'],
            '毫米':[0.001,'米'],
            '节':[1852,'米'],
            '节/海里':[1852,'米'],
            '节海里':[1852,'米'],
            '节行驶英里':[1852,'米'],
            '节下海里':[1852,'米'],
            '克':[0.001,'千克'],
            '里':[1852,'米'],
            '里/节':[1852,'米'],
            '米':[1,'米'],
            '千克':[1,'克'],
            '千米':[1000,'米'],
            '千米/节':[1000,'米'],
            '千米/时':[1000,'米'],
            '千米/小时':[1000,'米'],
            '千米每小时':[1000,'米'],
            '万海里/节':[18520000,'米'],
            '英里，节':[1610,'米'],
            '英里/节':[1610,'米'],
            '余英里':[1610,'米'],
            '约海里':[1852,'米'],
            '最大海里':[1852,'米'],
            '人': [1, '人'],
            '位': [1, '位']}
        return






    def insert_main(self):
        count = 0
        for record in open(self.datapath):
            data = {i:j for i,j in json.loads(record).items() if i !='_id'}
            data_new = data.copy()
            print(data_new)
            self.collection.insert(data_new)
            count += 1
        print('finished insert into database with %s records!'%count)
        return

    '检测是否有数字'
    def check_num(self, sent):
        pattern = re.compile('\d+')
        res = pattern.findall(str(sent))
        return res

    '''检查年份'''
    def check_year(self, sent):
        sent = sent.replace(' ', '')
        pattern_year = re.compile('[0-9]{4}年')
        pattern_month = re.compile('[0-9]{1,4}月')
        pattern_day = re.compile('[0-9]{1,4}日')
        default_day = ''
        default_month = ''
        month = pattern_month.findall(sent)
        day = pattern_day.findall(sent)
        year = pattern_year.findall(sent)
        if year:
            year = year[0].replace('年', '')
            if month:
                default_month = month[0].replace('月', '')
            if day:
                default_day = day[0].replace('日', '')
            if year:
                date_new = year + self.full_date(default_month) + self.full_date(default_day)
            else:
                date_new = ''
        else:
            return ''
        return date_new

    '''补全日期'''
    def full_date(self, date):
        if not date:
            date = '01'
        if int(date) < 10 and len(date) < 2:
            date = '0' + date
        return date



if __name__ == '__main__':
    handler = InsertData()
    handler.insert_main()
