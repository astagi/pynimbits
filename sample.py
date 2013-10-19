from nimbits import Nimbits

email = ''
key = ''
nimbits_client = Nimbits(email, key)
entity = "SampleValue"
nimbits_client.set_value(entity, lt=0.0, lg=0.0, d=3.5, t=1375830638376)
value = nimbits_client.get_value(entity)
if value:
    print value['d']
tree = nimbits_client.get_tree()
if tree:
    print tree