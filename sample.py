from nimbits import Nimbits

email = ''
key = ''
nimbits_client = Nimbits(email, key)
entity = "SampleValue"
nimbits_client.create_entity(name=name, description="Sample description", 
    entityType=1, protectionLevel=2, alertType=0, parent=email)
nimbits_client.set_value(name, lt=0.0, lg=0.0, d=3.5, t=1375830638376)
value = nimbits_client.get_value(name)
print value['d']