# CPUTemperature2HA

PYTHON Install:
sudo apt update
sudo apt install python3-pip

SETUP SCRIPT

mkdir -p /home/USER/Scripts
nano /home/USER/Scripts/cpu_temperatur_publisher.py

WARNING: Please change HOMEASSISTANTIP and ACCESS-TOKEN to your data. You can change "friendly_name" to set an own entity-name.

TEST SCRIP
python3 /home/USER/scripts/cpu_temperatur_publisher.py

Maybe you have to make the script executable:
sudo chmod +x /home/USER/scripts/cpu_temperatur_publisher.py

SETUP systemd Service
sudo nano /etc/systemd/system/cpu_temperature_publisher.service

WARNING: Please Change "SYSTEMBENUTZER" to your Systemuser

ACTIVATE systemd SERVICE:
sudo systemctl daemon-reload
sudo systemctl start cpu_temperature_publisher.service
sudo systemctl enable cpu_temperature_publisher.service

CHECK systemd SERVICE:
sudo systemctl status cpu_temperature_publisher.service

