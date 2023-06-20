#import the necessary libraries.
import csv
import matplotlib.pyplot as plt
from collections import Counter
import time


#initialize a dictionary to store each source IP address.
ip_counts = Counter()

#open the csv file and loop through each row.
with open('traffic_packets.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract the source IP address from the row
        source_ip = row['src_ip']
        
        # Update the count for the source IP address
        ip_counts[source_ip] += 1
        
        # Clear the previous plot and plot the new data
        plt.clf()
        plt.bar(ip_counts.keys(), ip_counts.values())
        plt.xlabel('Source IP')
        plt.ylabel('Count')
        plt.title('Count of Source IP Addresses')
        plt.draw()
        plt.show()
        
        # Add a delay to simulate real-time processing
        time.sleep(1)
