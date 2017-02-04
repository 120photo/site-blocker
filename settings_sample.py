from datetime import datetime as dt
# Change to read "live" when you want to go live.
mode = "dev"

# Use Military time to determind the hours you want the app to block sites.
start_hours = dt(dt.now().year, dt.now().month, dt.now().day, 8, 55) # Starts at 8:55AM
end_hours = dt(dt.now().year, dt.now().month, dt.now().day, 17) # Ends at 5:00PM

hosts_dev = "hosts"
hosts_live = "/etc/hosts" #path for macOS and linux, change for windows.
