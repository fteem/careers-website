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
                _make_software_engineer(i+1)
            )
            db.session.add(
                _make_data_scientist(i+1)
            )
            db.session.add(
                _make_product_manager(i+1)
            )
            db.session.add(
                _make_marketing_specialist(i+1)
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

def _make_software_engineer(level):
    fake = Faker()
    return Listing(
        title="Software Engineer {level}".format(level=level),
        slug="software-engineer-{level}".format(level=level),
        location="{city}, {state}".format(city=fake.city(), state=fake.state()),
        salary=100000,
        currency="USD",
        team_description="Join our talented engineering team and work on exciting projects. We value innovation, collaboration, and continuous learning. As a member of our team, you will have the opportunity to contribute your skills and expertise to develop cutting-edge software applications. We foster a dynamic and supportive environment that encourages personal and professional growth. Collaborate with like-minded individuals who are passionate about pushing boundaries and creating impactful solutions.",
        role_description="We are seeking a skilled software engineer to join our team. As a software engineer, you will be responsible for designing, developing, and maintaining software applications. Work closely with cross-functional teams to gather requirements, create technical solutions, and ensure the software meets high-quality standards. Take ownership of projects, write clean and efficient code, and participate in code reviews to foster a culture of excellence and continuous improvement.",
        responsibilities="In this role, you will be responsible for writing clean and efficient code, implementing software solutions, participating in code reviews, and collaborating with team members to deliver high-quality software products. You will contribute to the entire software development lifecycle, from requirements gathering to deployment and maintenance. Additionally, you will troubleshoot issues, perform debugging, and optimize performance as needed to ensure the software meets the needs of our users.",
        benefits_compensation="We offer a competitive salary package, comprehensive benefits, and a flexible work environment. Our benefits include health insurance, retirement plans, paid time off, and opportunities for professional development. Join our team and be part of a company that values its employees and promotes a culture of innovation, collaboration, and growth. Together, let's build software solutions that make a difference."
    )


def _make_data_scientist(level=1):
    fake = Faker()
    return Listing(
        title="Data Scientist {level}".format(level=level),
        slug="data-scientist-{level}".format(level=level),
        location="New York, NY",
        salary=120000,
        currency="USD",
        team_description="Join our data science team and work on cutting-edge projects. As a member of our team, you will have the opportunity to leverage your analytical skills and contribute to impactful solutions. Collaborate with talented professionals in a collaborative and intellectually stimulating environment. We encourage curiosity, creativity, and data-driven decision-making. Be part of a team that is passionate about solving complex problems and extracting meaningful insights from data.",
        role_description="We are looking for a talented data scientist to join our team. As a data scientist, you will be responsible for analyzing and interpreting complex datasets. You will extract actionable insights, build predictive models, and develop algorithms to solve real-world problems. Apply your expertise in statistics, machine learning, and data visualization to drive data-informed decision-making and help shape our business strategies.",
        responsibilities="In this role, you will be responsible for developing and implementing machine learning models, performing statistical analysis, and communicating findings to stakeholders. You will work closely with cross-functional teams to understand business requirements and translate them into data-driven solutions. Additionally, you will clean and preprocess data, conduct exploratory data analysis, and evaluate model performance to ensure the accuracy and effectiveness of our data-driven solutions.",
        benefits_compensation="We offer a generous compensation package, including a competitive salary, stock options, and performance bonuses. In addition to financial rewards, we provide comprehensive benefits such as health insurance, retirement plans, and paid time off. We believe in investing in our employees' growth and development, and we provide opportunities for continuous learning and professional advancement. Join our data science team and make a meaningful impact by turning data into actionable"
    )

def _make_product_manager(level=1):
    fake = Faker()
    return Listing(
        title="Product Manager {level}".format(level=level),
        slug="product-manager-{level}".format(level=level),
        location="{city}, {state}".format(city=fake.city(), state=fake.state()),
        salary=110000,
        currency="USD",
        team_description="Join our dynamic product management team and shape the future of our products. As a member of our team, you will work closely with cross-functional teams, including engineering, design, and marketing, to define product vision, strategy, and roadmap. Be part of a collaborative and fast-paced environment where you can make a significant impact and drive the success of our products.",
        role_description="We are seeking a skilled product manager to join our team. As a product manager, you will play a critical role in defining and driving the product strategy. You will gather market insights, analyze user needs, and translate them into product requirements. Work closely with engineering teams to ensure the successful delivery of product features that meet user expectations and drive business growth.",
        responsibilities="In this role, you will be responsible for gathering and prioritizing product requirements, conducting market research, and defining the product roadmap. You will collaborate with cross-functional teams to ensure the successful execution of the product strategy. Additionally, you will work closely with designers to create intuitive and user-friendly product experiences. Your responsibilities will also include tracking product performance, analyzing user feedback, and continuously iterating to improve the product.",
        benefits_compensation="We offer a competitive salary package, comprehensive benefits, and a flexible work environment. In addition to financial rewards, we provide opportunities for professional growth and development. Be part of a company that values its employees and fosters a culture of innovation and collaboration. Join our product management team and help shape the future of our products, delighting users and driving business success."
    )


def _make_marketing_specialist(level=1):
    fake = Faker()
    return Listing(
        title="Marketing Specialist {level}".format(level=level),
        slug="marketing-specialist-{level}".format(level=level),
        location="{city}, {state}".format(city=fake.city(), state=fake.state()),
        salary=80000,
        currency="USD",
        team_description="Join our marketing team and help us reach new audiences. As a member of our team, you will play a vital role in driving brand awareness, creating engaging content, and executing marketing campaigns across various channels. Collaborate with passionate professionals in a fast-paced and dynamic environment. We encourage innovation, creativity, and data-driven decision-making.",
        role_description="We are looking for a talented marketing specialist to join our team. As a marketing specialist, you will be responsible for planning and executing marketing campaigns to drive brand awareness and generate leads. Utilize your expertise in digital marketing, content creation, and campaign optimization to reach our target audience effectively and drive business growth.",
        responsibilities="In this role, you will be responsible for developing marketing strategies, creating engaging content, and executing multi-channel campaigns. You will collaborate with cross-functional teams to ensure brand consistency and drive marketing initiatives that align with business goals. Additionally, you will analyze campaign performance, track key metrics, and provide actionable insights to optimize marketing efforts.",
        benefits_compensation="We offer a competitive salary package and comprehensive benefits. In addition to financial rewards, we provide a collaborative and supportive work environment where your ideas and contributions are valued. Take advantage of professional development opportunities and grow your marketing skills. Join our marketing team and be part of a company that values creativity, innovation, and results-driven marketing strategies."
    )

