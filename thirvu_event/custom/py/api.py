import frappe
from frappe.utils import (nowdate,nowtime)
from frappe.utils import (today,add_days)
from frappe.auth import LoginManager
from frappe.core.doctype.user.user import generate_keys
from frappe.utils.password import get_decrypted_password

@frappe.whitelist(allow_guest=True)
def event_list(user): 
    username=frappe.get_doc("User",{"full_name":user})

    event_list = frappe.db.get_all("Event Participants", filters={"reference_docname": username.name, "reference_doctype": "User",'attendance':0},fields=["parent"]
    )

    today_event = []
    upcoming = []

    for i in event_list:
        events_today = frappe.db.get_all("Event",
            fields=["name", "starts_on"],
            filters={
                "status": "Open",
                "name": i["parent"],
                "starts_on": ["between", (nowdate(), nowdate())]
            }
        )
        today_event.extend(events_today)

        events_upcoming = frappe.db.get_all("Event",
            fields=["name", "starts_on"],
            filters={
                "status": "Open",
                "name": i["parent"],
                "starts_on": [">",add_days(today(), 1) ]
            }
        )

        upcoming.extend(events_upcoming)
        frappe.errprint(upcoming)

    frappe.local.response['today'] = today_event
    frappe.local.response['upcoming'] = upcoming


@frappe.whitelist()
def attendance(name, user):
    username=frappe.get_doc("User",{"full_name":user})
    doc = frappe.get_doc("Event", name)

    for i in doc.event_participants:
        if i.reference_docname == username.name:
            i.attendance = 1
            i.is_partner_attended = 1
            i.date=nowdate()
            i.time=nowtime()


    try:
        doc.save(ignore_permissions=True)
        frappe.db.commit()
        frappe.local.response['message'] = "Thankyou for Attending the Event"
    except BaseException as e:
        frappe.local.response['message'] = e


# @frappe.whitelist( allow_guest=True )
# def login(email,password):
# #  args=json.loads(args)
#     try:
#        login_manager = frappe.auth.LoginManager()
#        login_manager.authenticate(user=email, pwd=password)
#        login_manager.post_login()
#     except frappe.exceptions.AuthenticationError:
#        frappe.clear_messages()
#        frappe.local.response["message"] = "Incorrect Username or Password"
#        return
#     frappe.db.commit()
#     user = frappe.get_doc('User', frappe.session.user)
#     frappe.local.response['message']='Logined Sucessfully'

@frappe.whitelist( allow_guest=True )
def change_password(email,old_password,password):
#  args=json.loads(args)
    try:
       login_manager = frappe.auth.LoginManager()
       login_manager.authenticate(user=email, pwd=old_password)
       login_manager.post_login()
       user_doc = frappe.get_doc('User',email)
       user_doc.new_password = password
       user_doc.save()

    except frappe.exceptions.AuthenticationError:
       frappe.clear_messages()
       frappe.local.response["message"] = "Incorrect Username or Old Password"
       return

    frappe.db.commit()
    frappe.local.response['message']='Password Changed Sucessfully'

@frappe.whitelist( allow_guest=True )
def change_user(email,password,new_username):
#  args=json.loads(args)
    try:
       login_manager = frappe.auth.LoginManager()
       login_manager.authenticate(user=email, pwd=password)
       login_manager.post_login()
       user_doc = frappe.get_doc('User',email)
       user_doc.username = new_username
       user_doc.save()

    except frappe.exceptions.AuthenticationError:
       frappe.clear_messages()
       frappe.local.response["message"] = "Incorrect Email or Password"
       return

    frappe.db.commit()
    frappe.local.response['message']='Username Changed Sucessfully'

@frappe.whitelist()
def generate_token(user):
    user_details = frappe.get_doc("User", user)
    api_key = user_details.api_key
    changes = 0
    if not user_details.api_secret:
        api_secret = frappe.generate_hash(length=15)
        user_details.api_secret = api_secret
        changes = 1
    else:
        api_secret = get_decrypted_password("User", user, "api_secret")
    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key
        changes = 1
    if(changes):
        user_details.save(ignore_pernmissions=True)

    return f'token {api_key}:{api_secret}'

@frappe.whitelist( allow_guest=True )
def login(email,password):
#  args=json.loads(args)
    try:
       login_manager = frappe.auth.LoginManager()
       login_manager.authenticate(user=email, pwd=password)
       login_manager.post_login()
    except frappe.exceptions.AuthenticationError:
       frappe.clear_messages()
       frappe.local.response["message"] = "Incorrect Username or Password"
       return
    api_generate = generate_keys(frappe.session.user)
    frappe.db.commit()
    user = frappe.get_doc('User', frappe.session.user)
    frappe.local.response['token']="token "+user.api_key+":"+api_generate["api_secret"]
    
    frappe.local.response['message']='Logined Sucessfully'

# @frappe.whitelist( allow_guest=True )
# def login_1():
#     req = frappe.local.form_dict
#     frappe.db.begin()
#     login_manager = LoginManager()
#     login_manager.authenticate(req.email, req.password)
#     user_detail = frappe.get_doc("User", req.email)
#     try:
#         userlist = frappe.get_doc("User",req.email)
#         frappe.local.response["full_name"] = userlist.full_name
#         frappe.local.response["message"] = "Login Sucessfully" 
#         frappe.db.commit()
     
#     except frappe.exceptions.AuthenticationError:
#        frappe.clear_messages()
#        frappe.local.response["message"] = "Incorrect Username or Password"


