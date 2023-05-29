import os
import openai

openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")

SUMMARY_TEMPLATE = """
I am looking for a job and I want to have an easier time parsing through job ads.
In continuation, I will provide you with the details of the job ad. Once I am done, I will
say 'Go!' and you will provide me with a succint summary of the job ad.

The role name is: {role}

The hiring team says this about themselves: {team}

The role is described as: {role_description}

The benefits are: {benefits}

The responsibilities are: {responsibilities}

The salary is: {salary}. If the salary is not in USD, convert it to USD.

Go
"""

def get_summary(role, team, role_description, benefits, responsibilities, salary):
    summary = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": SUMMARY_TEMPLATE.format(
                    role=role,
                    team=team,
                    role_description=role_description,
                    benefits=benefits,
                    responsibilities=responsibilities,
                    salary=salary
                )
            }
        ]
    )
    return summary["choices"][0]["message"]["content"]
