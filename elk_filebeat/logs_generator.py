import logging
import random
import time

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Add a file handler to write logs to a file
file_handler = logging.FileHandler('logs/example.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
logging.getLogger().addHandler(file_handler)

# List of log types
log_types = ['application', 'security', 'database', 'network']

# Function to generate random log entries
def generate_log_entry():
    log_level = random.choice(['INFO', 'WARNING', 'ERROR'])
    log_type = random.choice(log_types)
    log_message = f'This is a sample {log_type} log message.'
    
    logging.log(getattr(logging, log_level), f'[{log_type.upper()}] - {log_message}')

# Generate and log random entries
for _ in range(100):
    generate_log_entry()