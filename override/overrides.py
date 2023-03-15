import frappe
from erpnext.manufacturing.doctype.downtime_entry.downtime_entry import DowntimeEntry
from frappe.model.document import Document

class MyDowntimeEntry(Document):
    def validate(self):
      frappe.msgprint("This after overrriding")
