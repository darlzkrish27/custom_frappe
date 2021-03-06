# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "custom_app"
app_title = "Custom App"
app_publisher = "Krishna"
app_description = "This is Customisation for frappe"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "krishna@agiliq.com"
app_license = "MIT"

# Includes in <head>
# ------------------
# include js, css files in header of desk.html
app_include_css = "/assets/custom_app/css/custom_app.css"
app_include_js = "/assets/custom_app/js/custom_app.js"

# include js, css files in header of web template
web_include_css = [
	"https://fonts.googleapis.com/css?family=Poppins:400,600,700,800",
	"/assets/custom_app/css/bootstrap.min.css",
	"/assets/custom_app/css/font-awesome.min.css",
	"/assets/custom_app/css/magnific-popup.css",
	"/assets/custom_app/css/owl.carousel.min.css",
	"/assets/custom_app/css/animate.css",
	"/assets/custom_app/css/main.css",
	"/assets/custom_app/css/style.css",
	"/assets/custom_app/css/meanmenu.min.css",
	"/assets/custom_app/css/responsive.css",
]
web_include_js = [
	# "/assets/custom_app/js/custom_app.js",
	# "/assets/custom_app/js/jquery-2.2.4.min.js",
	"/assets/custom_app/js/bootstrap.min.js",
	"/assets/custom_app/js/isotope.pkgd.min.js",
	"/assets/custom_app/js/jquery.magnific-popup.min.js",
	"/assets/custom_app/js/owl.carousel.min.js",
	"/assets/custom_app/js/owl.animate.js",
	"/assets/custom_app/js/jquery.scrollUp.min.js",
	"/assets/custom_app/js/jquery.counterup.min.js",
	"/assets/custom_app/js/modernizr.min.js",
	"/assets/custom_app/js/waypoints.min.js",
	"/assets/custom_app/js/jquery.meanmenu.min.js",
	"/assets/custom_app/js/custom.js",
	"/assets/custom_app/js/my_custom.js",
]

update_website_context = [
  'custom_app.www.custom_homepage.get_context'
]

website_context = {
"favicon": "/assets/custom_app/images/favicon.ico",
"splash_image": "/assets/custom_app/images/favicon.ico"
}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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
role_home_page = {
	"Guest": "index"
}

# Website user home page (by function)
# get_website_user_home_page = "custom_app.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "custom_app.install.before_install"
# after_install = "custom_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "custom_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"custom_app.tasks.all"
# 	],
# 	"daily": [
# 		"custom_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"custom_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"custom_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"custom_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "custom_app.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "custom_app.event.get_events"
# }

