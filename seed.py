import click
from app import app, db
from app.models import Listing
from faker import Faker
from slugify import slugify

@app.cli.command("seed")
@click.option('-t', '--table', 'table', help="Name of table to seed", type=str)
@click.option('-c', '--count', 'count', help="Number of rows to seed to TABLE", show_default=True, default=1, type=int)
def create_user(table, count):
    if table == 'listings':
        for i in range(count):
            l = _make_listing()
            db.session.add(l)
            db.session.commit()

def _make_listing():
    fake = Faker()
    job=fake.job()

    paragraph = lambda sentences : " ".join(sentences)

    l = Listing(
        title=job,
        slug = slugify(job),
        location = fake.city(),
        salary = fake.random_int(min=1000),
        currency = fake.currency_code(),
        team_description=paragraph(fake.paragraphs(nb=3)),
        role_description=paragraph(fake.paragraphs(nb=5)),
        responsibilities=paragraph(fake.paragraphs(nb=5)),
        benefits_compensation=paragraph(fake.paragraphs(nb=3))
    )
    return l
