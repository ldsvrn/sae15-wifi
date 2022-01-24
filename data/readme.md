# Data sets location
This directory contains three another ones related to the data sets and called **raw**, **processed**, **cleaned**. A description of each one is given below. 

## Raw directory
This directory contains original and immutable data sets. Do not edit raw data, especially with Excel, open files only in read only mode. This directory contains two subfolders, each one contains data related to an experiment. The first one is related to an experiment performed at the ground floor and the second one to the first floor. Each subfolder name structure starts with the localization and finishes by the day of the experiment. Each subfolder contains data files related to the signal strength of each Wi-Fi network advertised by hotpots. The filename has tree parts separated by a - and the final one indicated the where the experiment has been performed according to the building map (*build_C-wifi_measurement.pdf*) in the reference folder. All data files have the following structure :

- the name of Wi-Fi network,
- the virtual MAC address announcing the network.
- the signal strength (dBm).

The virtual MAC address is encoded directly in a bit string (b' '), to represent the hex format.  

## Processed directory
This directory contains intermediate transformed data sets. This working directory could contain multiple data sets.

## Cleaned directory
This directory contains canonical data sets could be used for publication. These data sets would be used for the analysis.
