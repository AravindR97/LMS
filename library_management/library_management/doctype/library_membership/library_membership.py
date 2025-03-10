# Copyright (c) 2025, Aravind R and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMembership(Document):
	def before_save(self):
		membership_period = frappe.db.get_single_value("Library Settings", "membership_period")
		self.to_date = frappe.utils.add_days(self.from_date, membership_period or 30)
	
	def before_submit(self):
		exists = frappe.db.exists("Library Membership",
							{
								"library_member": self.library_member,
								"docstatus": 1,
								"to_date": [">", self.from_date]
							})
		if exists:
			frappe.throw(f"{self.full_name} already has an active membership")
