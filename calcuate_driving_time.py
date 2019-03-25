{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "import json\n",
    "import urllib.request\n",
    "from user_definition import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "orig_coord = '37.7909,-122.3925'\n",
    "dest_coord = '37.7765,-122.4506'\n",
    "output_file_name = 'output.txt'\n",
    "# https://developers.google.com/maps/documentation/javascript/get-api-key\n",
    "# with open('/Users/areevesman/projects-ua/credentials/ge') as f:\n",
    "#     apikey = f.read()\n",
    "apikey='AIzaSyCaDOY12_vl72zRX_LZkdiiwnhC36O6Kn0'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'destination_addresses': ['University Center, San Francisco, CA 94117, USA'],\n",
       " 'origin_addresses': ['208 Spear St, San Francisco, CA 94105, USA'],\n",
       " 'rows': [{'elements': [{'distance': {'text': '6.9 km', 'value': 6874},\n",
       "     'duration': {'text': '22 mins', 'value': 1337},\n",
       "     'duration_in_traffic': {'text': '21 mins', 'value': 1247},\n",
       "     'status': 'OK'}]}],\n",
       " 'status': 'OK'}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "output_file = open(output_file_name, \"a\")\n",
    "url = \"https://maps.googleapis.com/maps/api/distancematrix/json?key={0}&origins={1}&destinations={2}&mode=driving&departure_time=now&language=en-EN&sensor=false\".format(\n",
    "    str(apikey), str(orig_coord), str(dest_coord))\n",
    "result = json.load(urllib.request.urlopen(url))\n",
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'21 mins'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "driving_time = result['rows'][0]['elements'][0]['duration_in_traffic']['text']\n",
    "driving_time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "output_file.write(str(datetime.datetime.now()) + \"\\n\")\n",
    "output_file.write(result['origin_addresses'][0] + \"\\n\")\n",
    "output_file.write(result['destination_addresses'][0] + \"\\n\")\n",
    "output_file.write(driving_time + \"\\n\\n\")\n",
    "\n",
    "output_file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
