import datetime
import json
import urllib.request
from user_definition import *

orig_coord = '37.7909,-122.3925'
dest_coord = '37.7765,-122.4506'
output_file_name = 'output.txt'
apikey='AIzaSyCaDOY12_vl72zRX_LZkdiiwnhC36O6Kn0'

output_file = open(output_file_name, "a")
url = "https://maps.googleapis.com/maps/api/distancematrix/json?key={0}&origins={1}&destinations={2}&mode=driving&departure_time=now&language=en-EN&sensor=false".format(str(apikey), str(orig_coord), str(dest_coord))
result = json.load(urllib.request.urlopen(url))

driving_time = result['rows'][0]['elements'][0]['duration_in_traffic']['text'] 
output_file.write(str(datetime.datetime.now()) + "\n") 
output_file.write(result['origin_addresses'][0] + "\n") 
output_file.write(result['destination_addresses'][0] + "\n")
output_file.write(driving_time + "\n\n")
output_file.close()
