import time

import psutil
import time
import logging
import click

# Configure logging
logger = logging.getLogger('BlenderLogger')
logger.setLevel(logging.INFO)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(r'performance.log')

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)



def log_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_cpu = psutil.cpu_percent(interval=None)
        start_memory = psutil.virtual_memory().used

        result = func(*args, **kwargs)

        end_time = time.time()
        end_cpu = psutil.cpu_percent(interval=None)
        end_memory = psutil.virtual_memory().used

        logger.info(f"Execution Time: {end_time - start_time:.2f} seconds")
        logger.info(f"CPU Usage: {end_cpu - start_cpu:.2f}%")
        logger.info(f"Memory Usage: {end_memory - start_memory} bytes")

        return result
    return wrapper




@log_performance
def consume_cpu_and_memory(memory:int,processor:int,sleep:int):
    # Create a large list to consume memory
    large_list = [i for i in range(memory)]
    
    # Perform intensive computations to consume CPU
    result = 0
    for i in range(processor):
        result += i ** 2

    # Keep the script running for a while to observe resource usage
    time.sleep(sleep)

