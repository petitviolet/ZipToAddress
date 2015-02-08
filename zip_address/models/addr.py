# -*- encoding:utf-8 -*-
''' ad_address table configuration
'''

from database import Base

from sqlalchemy import Column
from sqlalchemy.dialects.mysql import (INTEGER, VARCHAR, TINYINT)

class AdAddress(Base):
    __tablename__ = 'ad_address'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    id = Column(INTEGER(9), primary_key=True)
    ken_id = Column(INTEGER(2))
    city_id = Column(INTEGER(5))
    town_id = Column(INTEGER(9))
    zip = Column(VARCHAR(8))
    office_flg = Column(TINYINT(1))
    delete_flg = Column(TINYINT(1))
    ken_name = Column(VARCHAR(8))
    ken_furi = Column(VARCHAR(8))
    city_name = Column(VARCHAR(24))
    city_furi = Column(VARCHAR(24))
    town_name = Column(VARCHAR(32))
    town_furi = Column(VARCHAR(32))
    town_memo = Column(VARCHAR(16))
    kyoto_street = Column(VARCHAR(32))
    block_name = Column(VARCHAR(64))
    block_furi = Column(VARCHAR(64))
    memo = Column(VARCHAR(255))
    office_name = Column(VARCHAR(255))
    office_furi = Column(VARCHAR(255))
    office_address = Column(VARCHAR(255))
    new_id = Column(INTEGER(11))

    def __init__(self, id, ken_id, city_id, town_id, zip, office_flg, delete_flg,
                 ken_name, ken_furi, city_name, city_furi, town_name, town_furi,
                 town_memo, kyoto_street, block_name, block_furi, memo,
                 office_name, office_furi, office_address, new_id):
        self.id = id
        self.ken_id = ken_id
        self.city_id = city_id
        self.town_id = town_id
        self.zip = zip
        self.office_flg = office_flg
        self.delete_flg = delete_flg
        self.ken_name = ken_name
        self.ken_furi = ken_furi
        self.city_name = city_name
        self.city_furi = city_furi
        self.town_name = town_name
        self.town_furi = town_furi
        self.town_memo = town_memo
        self.kyoto_street = kyoto_street
        self.block_name = block_name
        self.block_furi = block_furi
        self.memo = memo
        self.office_name = office_name
        self.office_furi = office_furi
        self.office_address = office_address
        self.new_id = new_id

    def __repr__(self):
        return "<AdAddress {0}, {1}>".format(self.zip, self.ken_name)

    def __str__(self):
        return "<AdAddress {0}, {1}>".format(self.zip, self.ken_name)

    def to_dict(self):
        ''' convert format to dictionary
        '''
        dic = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        return dic
