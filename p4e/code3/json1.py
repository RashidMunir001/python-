import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
count=0
for k,v in info.items():
    {
    print(k,v)

    }
print('just values')
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
