import json
import os
from random import randint

tweets = []
with open("tweets.json", "r") as rfile:
    for line in rfile:
        t = {}
        data = json.loads(line)
        if data['lang'] == 'en':
            t['Source_Product_Review_ID'] = 'twitter#'+str(randint(1,500))
            t['Product_Name'] = None
            t['Product_Category'] = None
            t['Product_Price'] = None
            t['Review_Date'] = data['created_at']
            t['Review_Headline'] = None
            t['Review_Text'] = data['text']
            t['User_ID'] = data['user']['id']
            t['User_Name'] = data['user']['name']
            t['User_Age'] = None
            t['User_Location'] = data['user']['location']
            t['Positive_Words'] = None
            t['Negetive_Words'] = None
            t['Review_Sentiment'] = None
            t['Review_Rating'] = None
            tweets.append(t)
with open('output_list.json', 'w') as filehandle:
    json.dump(tweets, filehandle)
filehandle.close()
os.system("cat output_list.json | jq -c '.[]' > outputx.json")
dirname = "outputtweets"
f1 = open('outputx.json', 'r')
if not os.path.exists(dirname):
    os.makedirs(dirname)
for i, text in enumerate(f1):
    path_file = os.path.join(dirname, str(i + 1) + '.json')
    open(path_file, 'w').write(text)

for filename in os.listdir(dirname):
    if filename.endswith(".json"):
        path = dirname + "/" + filename
        command = "gsutil cp %s gs://dlt-sntmnt-poc-284722-files-source-1599614649" % path
        os.system(command)
