// Copyright (c) 2025, Aravind R and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Member", {
	refresh(frm) {
        frm.add_custom_button("Create Membership", ()=>{
            frappe.new_doc("Library Membership", {
                "library_member": frm.doc.name,
                "from_date": frappe.datetime.get_today()
            })
        })
	},
});
