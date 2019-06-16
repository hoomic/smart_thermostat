# Smart Thermostat

## Outline

This repository contains code in python to run a smart thermostat on a Raspberry Pi using a 4-relay board and a DHT22 humidity and temperature sensor. The code is split into 4 broad categories: thermostat logic, application for web and smartphones, database for visualization and learning, and GUI for the thermostat.

## TODO

### Thermostat Logic
- [x] Thermostat class that measures temperature and has controls to turn on/off different modes
- [ ] Logic to activate different modes based on the set temperature

### Application for Web and Smartphone
- [ ] Write an application in [BeeWare](https://beeware.org) to be deployed to web browsers and smartphones.
- [ ] On smartphones, allow MAC address to be registered to the thermostat for schedule tracking
- [ ] General application should allow user to set mode and/or set temperature.

### Database for Visualization and Learning
- [ ] Create a database in SQLite that records usage and settings throughout the day
- [ ] use `nmap -sn 192.168.1.0/24` to see which registered users are in the house at any given time
- [ ] Use data from above to automatically create a therostat schedule

### GUI for Thermostat
- [ ] Write code to display current temperature, current set temperature, and current mode onto a screen
- [ ] Create buttons for the touch screen that allow the user to set the temperature and mode

## Future Additions

- [ ] Create thermometer plugs that connect to the main thermostat and can be registered to different rooms so that you can set the temperature for an individual room. 
