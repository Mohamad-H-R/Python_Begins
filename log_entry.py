# input log entry and findting its position
log_entry = "Error 404: File not found at /var/www/html/index.php"
error_position = log_entry.find("Error")
file_position = log_entry.find("/var")

# input file path and change \\ to /
file_path = "C:\\User\\Documents\\config.txt"
unix_path = file_path.replace("\\", "/")

# split server log entry with ,
server_log_entry = 'server01,warning,disk_space_low,2024-01-15'
components = server_log_entry.split(',')
print(components)

# input username
username = 'Admin_user'
standardized_username = username.lower()

# input employee id
employee_id = 'EMP123'
is_valid = employee_id.isalpha()

# input config line
config_line = 'db_host=localhost:5432\n'
clean_config = config_line.rstrip()
print(clean_config)