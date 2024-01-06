from flask import Blueprint, request
from amazon.paapi import AmazonAPI
from dotenv import load_dotenv
from ..database.database import Database
from ..model.schedule_item import ScheduleItem
from ..model.schedule_search import ScheduleSearch
from bson import json_util
import json, os, datetime

routes_bp = Blueprint('routes',__name__)

load_dotenv()
db_host = os.environ.get("DATABASE_HOST")
db_port =  int(os.environ.get("DATABASE_PORT"))
db_username =  os.environ.get("DATABASE_USERNAME")
db_password =  os.environ.get("DATABASE_PASSWORD")

db = Database(host = db_host, port = db_port, username = db_username, password = db_password)

@routes_bp.route("/ping", methods=['GET'])
def ping():
    return "pong"

@routes_bp.route("/schedule", methods=['POST'])
def set_schedule():
    
    args = request.json
    
    schedule_type = args['type']
    cron = args['cron']
    
    if schedule_type == 'search':
        keywords = args['keywords']
        product_qty = args['product_qty']
        
        schedule = ScheduleSearch(
            keywords,
            product_qty,
            cron
        )
        
    elif schedule_type == 'item':
        asins = args['asins']
        
        schedule = ScheduleItem(
            asins,
            cron
        )
        
    db.insert_one(schedule.to_json())
    return {"status": "OK"}
