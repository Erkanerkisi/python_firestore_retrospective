from datetime import datetime, timedelta

import firebase_admin
from firebase_admin import credentials, firestore

cd = credentials.Certificate("path")

firebase_admin.initialize_app(cd)
x = datetime.now() - timedelta(days = 2)
datab = firestore.client()
# ***********************************  fourls
fourls = datab.collection('fourls').where("retroDate", ">", x)

docs = fourls.stream()

print("x : {}".format(x))

for doc in docs:
    print(f'---- {doc.to_dict()["retroDate"]}-- {doc.to_dict()["templateType"]} -- {doc.to_dict()["textContent"]}')

# ***********************************  madsadglad
madsadglad = datab.collection('madsadglad').where("retroDate", ">", x)

docs = madsadglad.stream()

for doc in docs:
    print(f'---- {doc.to_dict()["retroDate"]}-- {doc.to_dict()["templateType"]} -- {doc.to_dict()["textContent"]}')

# ***********************************  leancoffee
leancoffee = datab.collection('leancoffee').where("retroDate", ">", x)

docs = leancoffee.stream()

for doc in docs:
    print(f'---- {doc.to_dict()["retroDate"]}-- {doc.to_dict()["templateType"]} -- {doc.to_dict()["textContent"]}')


# ***********************************  sailorboat
sailorboat = datab.collection('sailorboat').where("retroDate", ">", x)

docs = sailorboat.stream()

for doc in docs:
    print(f'---- {doc.to_dict()["retroDate"]}-- {doc.to_dict()["templateType"]} -- {doc.to_dict()["textContent"]}')

# ***********************************  starfish
starfish = datab.collection('starfish').where("retroDate", ">", x)

docs = starfish.stream()

for doc in docs:
    print(f'---- {doc.to_dict()["retroDate"]}-- {doc.to_dict()["templateType"]} -- {doc.to_dict()["textContent"]}')

# ***********************************  stopstartcontinue
stopstartcontinue = datab.collection('stopstartcontinue').where("retroDate", ">", x)

docs = stopstartcontinue.stream()

for doc in docs:
    print(f'---- {doc.to_dict()["retroDate"]}-- {doc.to_dict()["templateType"]} -- {doc.to_dict()["textContent"]}')

# ***********************************  whatwentwell
whatwentwell = datab.collection('whatwentwell').where("retroDate", ">", x)

docs = whatwentwell.stream()

for doc in docs:
    print(f'---- {doc.to_dict()["retroDate"]}-- {doc.to_dict()["templateType"]} -- {doc.to_dict()["textContent"]}')

# ***********************************  wrap
wrap = datab.collection('wrap').where("retroDate", ">", x)

docs = wrap.stream()

for doc in docs:
    print(f'---- {doc.to_dict()["retroDate"]}-- {doc.to_dict()["templateType"]} -- {doc.to_dict()["textContent"]}')
