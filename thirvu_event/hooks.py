from . import __version__ as app_version

app_name = "thirvu_event"
app_title = "Thirvu Event"
app_publisher = "Thirvusoft"
app_description = "Thirvu Event"
app_email = "thirvusoft@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/thirvu_event/css/thirvu_event.css"
# app_include_js = "/assets/thirvu_event/js/thirvu_event.js"

# include js, css files in header of web template
# web_include_css = "/assets/thirvu_event/css/thirvu_event.css"
# web_include_js = "/assets/thirvu_event/js/thirvu_event.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "thirvu_event/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Event" : "/custom/js/event.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "thirvu_event.utils.jinja_methods",
#	"filters": "thirvu_event.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "thirvu_event.install.before_install"
# after_install = "thirvu_event.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "thirvu_event.uninstall.before_uninstall"
# after_uninstall = "thirvu_event.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "thirvu_event.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Event": {
		"after_insert": "thirvu_event.custom.py.qr.after_insert",
		
	},
	
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"thirvu_event.tasks.all"
#	],
#	"daily": [
#		"thirvu_event.tasks.daily"
#	],
#	"hourly": [
#		"thirvu_event.tasks.hourly"
#	],
#	"weekly": [
#		"thirvu_event.tasks.weekly"
#	],
#	"monthly": [
#		"thirvu_event.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "thirvu_event.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "thirvu_event.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "thirvu_event.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"thirvu_event.auth.validate"
# ]
