# Copyright (c) 2022, test and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class RTPDI(Document):
	pass

@frappe.whitelist(allow_guest=True)
def rt_pdi():
    rt = frappe.db.get_list('Quality Inspection Parameter',
        filters=
        {'parameter_group':'FUNCTIONAL OPERATION'},
        fields=['*']
        )
    return rt