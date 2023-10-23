#!/bin/bash

sudo apt update
sudo apt install cron

current_directory="$PWD"

echo "*/5 * * * * $current_directory/script.sh" | crontab -