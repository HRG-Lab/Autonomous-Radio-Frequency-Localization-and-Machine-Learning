import pyshark
import csv


cap = pyshark.LiveCapture(interface='wlan0')
count=0

str = 'mycsv%d.csv' % count
with open(str, 'w') as f:
	thewriter = csv.writer(f)
	for packet in cap.sniff_continuously(packet_count=6500):
		if "wlan" in packet:
			try:
				RSSI = packet.radiotap.dbm_antsignal
				addr = packet.wlan.ta

				thewriter.writerow([addr, RSSI, 'tile0'])

			except AttributeError as e:
				pass


