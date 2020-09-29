import json
import os
from random import randint

os.system("del output_list.json")
os.system("del outputx.json")
os.system("del -R outputtweets/*")
tweets = []
dirname = "outputtweets"
i = 0
with open("tweets.json", "r") as rfile:
    for line in rfile:
        if len(line) > 1:
            t = json.loads(line)
            path_file = os.path.join(dirname, str(i + 1) + '.json')
            open(path_file, 'w').write(line)
            i = i + 1
for filename in os.listdir(dirname):
    if filename.endswith(".json"):
        path = dirname + "/" + filename
        command = "gsutil cp %s gs://dlt-sntmnt-poc-284722-files-source-1599614649" % path
        os.system(command)