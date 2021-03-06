from datetime import datetime, timedelta

import firebase_admin
from firebase_admin import credentials, firestore

cd = credentials.Certificate("path.json")

firebase_admin.initialize_app(cd)
x = datetime.now() - timedelta(days = 10)
datab = firestore.client()
# ***********************************  fourls
fourls = datab.collection('fourls').where("retroDate", "<", x)

docs = fourls.stream()

print("x : {}".format(x))

for doc in docs:
    doc.reference.delete()

# ***********************************  leancoffee
leancoffee = datab.collection('leancoffee').where("retroDate", "<", x)

docs = leancoffee.stream()

for doc in docs:
    doc.reference.delete()

# ***********************************  madsadglad
madsadglad = datab.collection('madsadglad').where("retroDate", "<", x)

docs = madsadglad.stream()

for doc in docs:
    doc.reference.delete()

# ***********************************  sailorboat
sailorboat = datab.collection('sailorboat').where("retroDate", "<", x)

docs = sailorboat.stream()

for doc in docs:
    doc.reference.delete()

# ***********************************  starfish
starfish = datab.collection('starfish').where("retroDate", "<", x)

docs = starfish.stream()

for doc in docs:
    doc.reference.delete()

# ***********************************  stopstartcontinue
stopstartcontinue = datab.collection('stopstartcontinue').where("retroDate", "<", x)

docs = stopstartcontinue.stream()

for doc in docs:
    doc.reference.delete()

# ***********************************  whatwentwell
whatwentwell = datab.collection('whatwentwell').where("retroDate", "<", x)

docs = whatwentwell.stream()

for doc in docs:
    doc.reference.delete()

# ***********************************  wrap
wrap = datab.collection('wrap').where("retroDate", "<", x)

docs = wrap.stream()

for doc in docs:
    doc.reference.delete()
