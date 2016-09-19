# coding: utf-8
# Author: Avikal Somvanshi

from __future__ import print_function
import json
import urllib2 
import os
import sys

#My_MTA_key = "857fded5-0cd9-4823-805b-25a91f048372"
MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]

#Building upon the lab example
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(MTA_KEY, BUS_LINE)
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

busline_name = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity'][0][u'MonitoredVehicleJourney'][u'PublishedLineName']
print ('Bus Line :' , busline_name)

number_of_buses = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity']
print ('Number of Active Buses :', str(len(number_of_buses)))

for i in range(len(number_of_buses)):
    busline_location = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity'][i][u'MonitoredVehicleJourney'][u'VehicleLocation']
    print ('Bus ', str(i), ' is at latitude ', str(busline_location[u'Latitude']), ' and longitude ', str(busline_location[u'Longitude']))



