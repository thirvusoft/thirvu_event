// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt
frappe.provide("frappe.desk");

frappe.ui.form.on("Event", {
	refresh: function (frm) {
		frm.add_custom_button(__('Add Users'), function() {
			new frappe.desk.eventParticipants(frm, "User");
		}, __("Add Participants"));

	},

});

