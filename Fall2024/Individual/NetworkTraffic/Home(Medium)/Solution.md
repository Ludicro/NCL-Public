# Q1: What brand smart devices are being communicated with in this packet capture?
**A1:** Look at the packet infos until you see the first packet where a command is sent and it tell you the name in the protocol

# Q2: What is the IP address of the device that sent a discovery message?
**A2:** After you see connections with the smart device, you notice one IP is sending SYN 

# Q3: What is the model name of the device with the Stairway alias?
**A3:**Looking at the packet where the response to the `get_sysinfo` command is, we can go through the information and find the model attribute

# Q4: What is the software version of the device with the Sub alias?
**A4:**Find which packet has the alias Sub and then find `sw_ver` value

# Q5: How many times is the Stairway device state changed?
**A5:**Apply the filter `ip.addr==10.0.0.4` as that's the IP of the device "Stairway".

Then you can search when the string `set_relay_state` appears and count how many times it switches.