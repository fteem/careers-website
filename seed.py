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
            db.session.add(
                _make_software_engineer(i)
            )
            db.session.add(
                _make_data_scientist(i)
            )
            db.session.add(
                _make_product_manager(i)
            )
            db.session.add(
                _make_marketing_specialist(i)
            )

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

def _make_software_engineer():
    fake = Faker()
    level = fake.random_int(min=1, max=4)
    return Listing(
        title="Software Engineer {level}".format(level=level),
        slug="software-engineer-{level}".format(level=level),
        location="{city}, {state}".format(city=fake.city(), state=fake.state()),
        salary=100000,
        currency="USD",
        team_description="Join our talented engineering team and work on exciting projects.",
        role_description="Develop and maintain software applications.",
        responsibilities="Write clean and efficient code, participate in code reviews, and collaborate with the team.",
        benefits_compensation="Competitive salary, health insurance, and flexible work hours."
    )


def _make_data_scientist(level=1):
    fake = Faker()
    return Listing(
        title="Data Scientist {level}".format(level=level),
        slug="data-scientist-{level}".format(level=level),
        location="New York, NY",
        salary=120000,
        currency="USD",
        team_description="Join our data science team and work on cutting-edge projects.",
        role_description="Analyze and interpret complex datasets to extract insights.",
        responsibilities="Develop machine learning models, perform statistical analysis, and collaborate with cross-functional teams.",
        benefits_compensation="Generous compensation package, stock options, and professional development opportunities."
    )

def _make_product_manager(level=1):
    fake = Faker()
    return Listing(
        title="Product Manager {level}".format(level=level),
        slug="product-manager-{level}".format(level=level),
        location="{city}, {state}".format(city=fake.city(), state=fake.state()),
        salary=110000,
        currency="USD",
        team_description="Join our dynamic product management team and shape the future of our products.",
        role_description="Define product vision, roadmap, and strategy.",
        responsibilities="Gather user feedback, prioritize features, and collaborate with engineering and design teams.",
        benefits_compensation="Competitive salary, equity grants, and flexible work environment."
    )


def _make_marketing_specialist(level=1):
    fake = Faker()
    return Listing(
        title="Marketing Specialist {level}".format(level=level),
        slug="marketing-specialist-{level}".format(level=level),
        location="{city}, {state}".format(city=fake.city(), state=fake.state()),
        salary=80000,
        currency="USD",
        team_description="Join our marketing team and help us reach new audiences.",
        role_description="Plan and execute marketing campaigns across various channels.",
        responsibilities="Create engaging content, analyze campaign performance, and collaborate with sales teams.",
        benefits_compensation="Competitive salary, performance bonuses, and career growth opportunities."
    )

