import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def main(count, name):
    """
    Simple program that greets NAME for a total of COUNT times.
    """
    # 会当作help信息进行输出
    for x in range(count):
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    main()
