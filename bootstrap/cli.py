import click

from bootstrap.core import Generator


@click.command()
@click.option('--output', default='.', help='output directory')
@click.option('--name', prompt='package name', help='your package name')
@click.option('--author', prompt='your name', help='your name')
@click.option('--version', default='0.1.0', help='version')
@click.option('--email', default='example@example.com', help='author email')
@click.option('--url', default='https://github.com/', help='url')
@click.option('--description', default='short description', help='your package description')
def generate_skeleton(name=None, output=None, author=None, email=None, url=None, description=None, version=None):
    directory = '{}/{}'.format(output, name)
    Generator(
        directory=directory,
        name=name,
        author=author,
        version=version,
        email=email,
        url=url,
        description=description
    ).generate()


def main():
    generate_skeleton()


if __name__ == '__main__':
    main()
