# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2021- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Sale Order Ready to Deliver:Remove Lines',
    'version': '14.0.0.0.0',
    # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'Sale Order Allows us to remove sale order lines when a sale order is not in the state Done, Ready to Deliver or Delivered',
    'category': 'Marketing',
    'description': """
        Sale Order Allows us to remove sale order lines when a sale order is not in the state Done, Ready to Deliver or Delivered.
    """,
    #'sequence': '1'
    #'images': ['images/main_screenshot.png']
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/',
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-sale',
    'depends': ['sale_order_ready_to_deliver'],
    'data': [
        #'views/project_view.xml',
        #'views/hr_employee_view.xml',
        #'views/sale_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}