# projects1
“Cybersecurity and penetration testing projects focused on vulnerability assessment, network security, and ethical hacking techniques.” “Collection of ethical hacking labs, security tools, and penetration testing practice projects.” “Hands-on cybersecurity experiments covering web, network, and system exploitation in a legal lab environment.”
This is a total overview of my cybersecurity journey

PROJECT 2 :1.  configure SSH using the password method. 
1. install fail2ban and get my ip
<img width="1365" height="762" alt="Screenshot 2026-04-06 143509" src="https://github.com/user-attachments/assets/9f06437d-a0de-4a9d-9b98-d47ab8a12ded" />
2.Installation and configuration of fail2ban using “sudo apt install fail2ban -y”.  creating configuration using “sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local” and “sudo nano /etc/fail2ban/jail.local” where I have to modify SSH section then restart fail2ban using “sudo systemctl restart fail2ban
<img width="1366" height="765" alt="nano" src="https://github.com/user-attachments/assets/9b7adeda-c9ce-4537-8a56-85d8d0286866" />
3.1.	From my attacker machine (Windows) trying to SSH it using “ssh abiodun @192.168.1.180” 
This shows a failed login attempts after I intentionally enter WRONG passwords 3 times
<img width="1366" height="768" alt="Screenshot (28)" src="https://github.com/user-attachments/assets/d692e80d-138a-455c-bee6-793b49f406eb" />
Then check fail2ban status using “sudo fail2ban-client status sshd”
<img width="1366" height="768" alt="Screenshot 2026-04-07 111939" src="https://github.com/user-attachments/assets/a693be57-a340-4978-9534-dc63c6fb9fb8" />
Then I use sudo cat /var/log/fail2ban.log to view the logs which shows the failed attempts + ban
<img width="1365" height="768" alt="Screenshot 2026-04-07 112249" src="https://github.com/user-attachments/assets/d907a78c-3164-44af-9518-db0dcd063850" />



 
