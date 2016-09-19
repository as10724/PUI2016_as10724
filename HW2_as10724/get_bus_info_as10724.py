# coding: utf-8
# Author: Avikal Somvanshi


from __future__ import print_function
import json
import urllib2 
import os
import sys
import csv


#My_MTA_key = "857fded5-0cd9-4823-805b-25a91f048372"
MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
name = sys.argv[3]

#Building upon the lab example
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(MTA_KEY, BUS_LINE)
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

number_of_buses = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity']
w = csv.writer(open(name, 'wb+'))
w.writerow(['Latitude' , 'Longitude' , 'Stop Name' , 'Stop Status'])
        
for i in range(len(number_of_buses)):
    busline_location = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity'][i][u'MonitoredVehicleJourney'][u'VehicleLocation']
    busline_onward = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity'][i][u'MonitoredVehicleJourney'][u'OnwardCalls']
    if not bool(busline_onward): #Checking if the Onward Calls directory is empty
        stop = 'N/A'
        status = 'N/A'
    else:
        stop = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity'][i][u'MonitoredVehicleJourney'][u'OnwardCalls'][u'OnwardCall'][0][u'StopPointName']
        status = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity'][i][u'MonitoredVehicleJourney'][u'OnwardCalls'][u'OnwardCall'][0][u'Extensions'][u'Distances'][u'PresentableDistance']
        w.writerow([busline_location['Latitude'], busline_location['Longitude'], stop, status])
        
  


