#This file is part sale_opportunity_shop module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['SaleOpportunity']
__metaclass__ = PoolMeta


class SaleOpportunity:
    __name__ = "sale.opportunity"
    shop = fields.Many2One('sale.shop', 'Shop')

    @classmethod
    def __setup__(cls):
        super(SaleOpportunity, cls).__setup__()
        cls._error_messages.update({
                'opportunity_not_shop': 'Select a shop "%s" oportunity',
            })

    @staticmethod
    def default_shop():
        User = Pool().get('res.user')
        user = User(Transaction().user)
        return user.shop.id if user.shop else None

    def _get_sale_opportunity(self):
        '''
        Add shop in sale for an opportunity
        '''
        if not self.shop:
            self.raise_user_error('opportunity_not_shop', (
                    self.rec_name,)
                    )
        sale = super(SaleOpportunity, self)._get_sale_opportunity()
        sale.shop = self.shop
        return sale
