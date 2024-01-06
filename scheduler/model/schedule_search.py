import bson, json

class ScheduleSearch(object):
  
  def __init__(self,
               keywords,
               product_qty,
               cron):
      
      self.type = "search"
      self.keywords = keywords
      self.product_qty = product_qty
      self.cron = cron

  def to_json(self):
    schedule_search = {
            "type": self.type,
            "keywords": self.keywords,
            "product_qty": self.product_qty,
            "cron": self.cron
            }
    return json.loads(bson.json_util.dumps(schedule_search))

  def to_bson(self):
      data = self.dict(by_alias=True, exclude_none=True)
      if data["_id"] is None:
          data.pop("_id")
      return data
