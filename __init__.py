#This file is part sale_opportunity_shop module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .opportunity import *

def register():
    Pool.register(
        SaleOpportunity,
        module='sale_opportunity_shop', type_='model')
