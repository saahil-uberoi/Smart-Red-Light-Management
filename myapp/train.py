from import_files import *
import json
from key import get_your_own_key, get_your_own_key1
from traffic_data import low_traffic, high_traffic, ambulance, fire, fire1, ambulance1, animals


def start():
    app = image_analyzer(api_key=get_your_own_key1)
    # app.inputs.delete_all()
    # for i in range(0, len(high_traffic)):
    #     try:
    #         app.inputs.create_image_from_url(url=high_traffic[i], concepts=['high density'])
    #         print i
    #     except:
    #         continue
    # for j in range(0, len(low_traffic)):
    #     try:
    #         app.inputs.create_image_from_url(url=low_traffic[j], concepts=['low density'])
    #         print j
    #     except:
    #         continue
    # for k in range(0, len(ambulance)):
    #     try:
    #         app.inputs.create_image_from_url(url=ambulance[k], concepts=['ambulance'])
    #         print k
    #     except:
    #         continue
    # for l in range(0, len(ambulance1)):
    #     try:
    #         app.inputs.create_image_from_url(url=ambulance1[l], concepts=['ambulance'])
    #         print l
    #     except:
    #         continue
    for m in range(0, len(animals)):
        try:
            app.inputs.create_image_from_url(url=animals[m], concepts=['animals'])
            print m
        except:
            continue
    app.models.create('animals', concepts=['animals'])
    model = app.models.get('animals')
    model.train()


    ## For Predicting and testing purpose

    # image = Image(url='https://s3.scoopwhoop.com/anj/dskjsdjkdsc/184216406.jpg')
    # data = model.predict([image])
    # with open('repo_data.json', 'w') as outfile:
    #     json.dump(data, outfile)
    # print data
start()
