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
<img width="810" height="490" alt="image" src="https://github.com/user-attachments/assets/5f082b9b-fff7-4762-8d5a-b0e494980a5e" />

------------------------------------------------------------------------------------------------------
STEP 2: The code

1. Run and code in the file ```Malicious_IP_Blocker.py``` [extracts malicious IP, block them in firewall, and logs the action]

Handling permissions in this automation

2. Open the system sudoers configuration using the safe editor: ```sudo visudo```
3. Scroll to the bottom of the file and add: ```{username} ALL=(ALL) NOPASSWD: /usr/sbin/ufw``` and save the file.
4. run the file ```python3 Malicious_IP_Blocker.py```, to run the python code and add malicious IP's to the firewall to block them automatically.
5. run ```sudo ufw status verbose``` on the terminal to the new rules are active.
   <img width="785" height="338" alt="image" src="https://github.com/user-attachments/assets/ffa7fd92-8a5b-438c-9564-6542458b97af" />

   
To log the actions :
7. sudo touch /var/log/threat_scraper.log
8. sudo chown kamal:kamal /var/log/threat_scraper.log
As the directory, /var/log/ is owned by the system root user, the  python script will not be able to create that file by default. So, we have to create the file manually so the code can run smoothly. 


Running the code:
1. python3 fw_updater.py
2. cat /var/log/threat_scraper.log [for logs]

------------------------------------------------------------------------------------------------------
STEP 3: Crontab
Cron tab is used to make this code run on autonomous mode. 

1. Open cron tab ```crontab -e```.
2. At the bottom of the file add: ```0 * * * * /usr/bin/python3 {directory path}/Malicious_IP_Blocker.py```, and save it

Now this code runs every hour at exactly 00 minutes and blocks the malicious IP addresses to prevent attacks form those IPs. 

⚆_⚆


   

