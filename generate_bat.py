from pathlib import Path
def gen_bat_file1(task_number, timeout, bat_name):
    """Generate a bat file with a given task name."""
    with open(bat_name, "w") as bat_file:
        bat_file.write(f'echo {task_number}\n')
        # timeout /t 60 >nul
        bat_file.write(f'timeout /t {timeout} >nul\n')
        # echo Task number 1 completed after 1 minute.
        bat_file.write(f'echo Task number {task_number} completed after {timeout} seconds.\n')

def gen_bat_file2(python_file:Path,bat_file:Path,memory:int=1024,processor:int=1,sleep:int=60):
    """Generate a bat file with a given task name."""
    with open(bat_file, "w") as bat:
        bat.write(f'echo {bat_file.name}\n')
        # timeout /t 60 >nul
        bat.write(f'python {python_file} {memory} {processor} {sleep} \n')
       