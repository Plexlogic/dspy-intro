import os
import dspy
from pprint import pprint

# We first need to tell dspy which language model we want to use
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
language_model = dspy.OpenAI(model="gpt-4-turbo", api_key=OPENAI_API_KEY)
dspy.settings.configure(lm=language_model)


class Description(dspy.Signature):
    """Creates a concise and direct description to achieve the intent of the title, doesn't include any testing"""

    title = dspy.InputField(desc="The title of the ticket")
    jira_ticket_description = dspy.OutputField(
        desc="A clear outline of the task being described"
    )


class AcceptanceCriteria(dspy.Signature):
    """Considers all possible failure modes and creates acceptance criteria to check for regressions, doesn't describe the task"""

    jira_ticket_description = dspy.InputField(desc="The description of the ticket")
    acceptance_criteria = dspy.OutputField()


class TicketCreator(dspy.Module):
    """Automates the creating of jira tickets"""

    def __init__(self):
        self.create_description = dspy.Predict(Description)
        self.create_acceptance_criteria = dspy.ChainOfThought(AcceptanceCriteria, n=3)

    def forward(self, title):

        description = self.create_description(title=title)

        acceptance_criteria = self.create_acceptance_criteria(
            jira_ticket_description=description.jira_ticket_description
        )

        return {
            "description": description.jira_ticket_description,
            "acceptance_criteria": acceptance_criteria.acceptance_criteria,
        }


ticket_creator = TicketCreator()

title = input("What is the title of the ticket?\n")

ticket = ticket_creator(title=title)

pprint(ticket)
