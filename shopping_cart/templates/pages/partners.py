# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import frappe.website.render

def get_context(context):
	return {
		"partners": frappe.db.sql("""select * from `tabParty`
			where ifnull(sales_partner, '')!='' and ifnull(show_in_website, 0)=1
			order by name asc""", as_dict=True),
		"title": "Partners"
	}

def clear_cache(doc, trigger):
	if doc.page_name:
		frappe.website.render.clear_cache("partners")
