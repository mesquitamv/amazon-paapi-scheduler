import bson, json

class ScheduleItem(object):
  
  def __init__(self,
               asins,
               cron):
      
      self.type = 'item'
      self.asins = asins
      self.cron = cron

  def to_json(self):
    schedule_item = {
            "type": self.type,
            "asins": self.asins,
            "cron": self.cron
            }
    return json.loads(bson.json_util.dumps(schedule_item))

  def to_bson(self):
      data = self.dict(by_alias=True, exclude_none=True)
      if data["_id"] is None:
          data.pop("_id")
      return data
