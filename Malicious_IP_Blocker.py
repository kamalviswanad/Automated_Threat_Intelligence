import os
import datetime
import requests
import subprocess


THREAT_FEED_URL = "https://feodotracker.abuse.ch/downloads/ipblocklist.json"
LOG_FILE_PATH = "/var/log/threat_scraper.log"

def log_message(message):
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}] {message}\n"
    

    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(log_entry)

def fetch_and_block_ips():
    
    log_message("INFO: Starting automated Threat Intelligence sync...")
    
    try:
        
        response = requests.get(THREAT_FEED_URL, timeout=15)
        response.raise_for_status()
        threat_data = response.json()
        
        log_message(f"INFO: Successfully ingested {len(threat_data)} threat indicators.")
        
        
        for entry in threat_data:
            ip_address = entry.get("ip_address")
            malware = entry.get("malware", "Unknown Vector")
            
            if ip_address:
                
                cmd = ["sudo", "ufw", "deny", "from", ip_address, "to", "any"]
                
                try:
                    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
                    log_message(f"SUCCESS: Perimeter defense updated. Blocked malicious IoC: {ip_address} ({malware})")
                except subprocess.CalledProcessError as e:
                    log_message(f"ERROR: Failed to inject rule for {ip_address}: {e.stderr.decode().strip()}")
                    
    except requests.exceptions.RequestException as e:
        log_message(f"CRITICAL: Data pipeline failure. Feed unreachable: {e}")
    except ValueError:
        log_message("CRITICAL: Data normalization failure. Payload formatting variation detected.")

if __name__ == "__main__":
    fetch_and_block_ips()
