import json

class test:
  a = int(0)
  b = str('123')

test_dict= test.__dict__
test_json = json.dumps(test_dict)
print (test_json)