from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation +" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(first_name="", last_name="", company="", home_phone="")] + [
    Contact(first_name=random_string("fname-",10), last_name=random_string("lname-",20),
            company=random_string("company-",20), home_phone=random_string("hphone-",7))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__,indent=2))
