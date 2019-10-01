import os
import unittest
from flask_cors import CORS
from dotenv import load_dotenv
from flask_script import Manager, Server
from config.app import create_app
from routes.api import blueprint
# from app.helpers.image_helper import IMAGE_SET
# from flask_uploads import configure_uploads, patch_request_class
# from flask_mail import Mail
from flask_orator import Orator

load_dotenv()

app = create_app(os.getenv('CONFIG_NAME'))
app.register_blueprint(blueprint)
app.app_context().push()

CORS(app)
db = Orator(app)

manager = Manager(app)
manager.add_command("runserver", Server(host=app.config['HOST'], port=app.config['PORT']))

# from app.main.models import blacklist, contract,customer, department, level, machine, machine_customer, machine_group,machine_models, machine_status, machine_type, service_code, technician, ticket_origin, ticket_status, ticket_tracking,ticket_type, user,sales_item,sales_order,status_job,consumable_request, additional_note, action_code, fault_area_code, problem_code, part, part_inventory, ce,  meter_reading, toner_stock, helpdesk_comment, sales,prioritys,installation,spr_request,ticket_ce,pm_checklis,fcm,tracking_meter_reading,tracking_close_job,tracking_survey,pm_checklist_pp,component_taken, quotation, quotation_item,transfer_order, holiday,working_hours,invoice,direct_message,stn,supervisor,supervisor_ce,postal_code,dsta

@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()
