import frappe
from pyqrcode import create as qr_create
import io
import os
import json

@frappe.whitelist()
def after_insert(doc, event):
    # QR Generation
    data = doc.name
    data = json.dumps(data)
    qr_image = io.BytesIO()
    data_ = qr_create(data, error='L')
    data_.png(qr_image, scale=1, quiet_zone=1)
    name = frappe.generate_hash('', 5)
    
    new_file = frappe.get_doc({
        "doctype": "File",
        "file_name": f"QRCode-{name}.png".replace(os.path.sep, "__"),
        "is_private": 0,
        "content": qr_image.getvalue(),
        "attached_to_doctype":  doc.doctype, 
        "attached_to_name": doc.name
    })
    new_file.save(ignore_permissions=True)
    frappe.db.commit()