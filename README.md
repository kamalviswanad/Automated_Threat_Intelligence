# Automated_Threat_Intelligence

In this project, I used feodotracker to extract malicious IP addresses (C2 center) and automated the process to block malicious IP's to prevent any attacks in the future. 

This project has ____ steps:
1.

------------------------------------------------------------------------------------------------------
STEP 1: Initial Setup

1. Installing Uncomplicated Firewall and enabling it.
      ``` sudo apt update && sudo apt install ufw -y ```
       ```sudo ufw enable```
2. run ```curl https://feodotracker.abuse.ch/downloads/ipblocklist.json``` on the terminal to verify the API's working.

------------------------------------------------------------------------------------------------------
STEP 2: The code

1. Run and code in the file ```Malicious_IP_Blocker.py``` [extracts malicious IP, block them in firewall, and logs the action]

Handling permissions in this automation

2. Open the system sudoers configuration using the safe editor: ```sudo visudo```
3. Scroll to the bottom of the file and add: ```{username} ALL=(ALL) NOPASSWD: /usr/sbin/ufw``` and save the file.
4. run the file ```python3 fw_updater.py```, to run the python code and add malicious IP's to the firewall to block them automatically.
5. run ```sudo ufw status verbose``` on the terminal to the new rules are active.
6. 
   

