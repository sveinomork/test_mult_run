from python_high_usage import consume_cpu_and_memory
import click

@click.command()
@click.argument('memmory',type=int)
@click.argument('processor',type=int)
@click.argument('sleep',type=int)
def cli(memmory,processor,sleep):
    consume_cpu_and_memory(memmory,processor,sleep)

if __name__ == "__main__":
    print("starting")
    cli()
