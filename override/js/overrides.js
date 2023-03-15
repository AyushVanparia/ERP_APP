frappe.ui.form.on('Downtime Entry', {
	refresh: function(frm) {
			frappe.msgprint(__("This is after Overriding"))
	}
});