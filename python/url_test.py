import urllib
from elementtree.ElementTree import Element, ElementTree, SubElement, dump, parse, tostring

busList = [


"194101331": {
	"name": "133",
	"direction": 0
},
"194101332": {
	"name": "133",
	"direction": 1
},
"196102331" : {
	"name":"233",
	"direction": 0
},
"196102332": {
	"name": "233",
	"direction": 1
},
"196103372" : {
	"name":"337",
	"direction": 0
},
"196103371" : {
	"name":"337",
	"direction": 1
},
"196107331" : {
	"name":"733",
	"direction": 0
},
"196107332" : {
	"name":"733",
	"direction": 1
},
"196108071": {
	"name":"807",
	"direction": 0
},
"196108072": {
	"name": "807",
	"direction": 1
}




url_base = "http://apis.its.ulsan.kr:8088/Service4.svc/AllBusArrivalInfo.xo?stopid="
stop_id = 40233

url = url_base + str(stop_id)
resp = urllib.urlopen(url)

tree = ElementTree()
tree.parse(resp)
root = tree.getroot()
bus_list = root[0]

while bus_list[0] != "AllBusArrivalInfoTable":
	bus_list = bus_list[len(bus_list)-1]


