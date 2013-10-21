from nimbits import Nimbits, NimbitsError

email = ''
key = ''

nimbits_client = Nimbits(email, key)
entity = "SampleValue"

try:
    print nimbits_client.set_value(entity, d=3.6, t=1375830638376)
    value = nimbits_client.get_value(entity)
    print value['d']
    tree = nimbits_client.get_tree()
    print tree
except NimbitsError as ne:
    print ne.message