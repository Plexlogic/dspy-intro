import dspy
import os
import threading
from dspy.evaluate import Evaluate

from utils.settings import OPENAI_API_KEY, use_openai_model
from utils.data import get_text
from utils.assessments import Assessment


class Recommendation(dspy.Signature):
    contract = dspy.InputField(desc="A legal contract to be reviewed")
    negotiation_playbook = dspy.InputField(desc="The negotiations playbook used to review the legal contract")
    recommendations = dspy.OutputField(desc=(
        "A list of recommended changes to the legal contract, for each clause which is not compliant with the negotations playbook. " +
        "Each recommendation is a single line of text."
    ))

RECOMMENDATION_PREDICTOR = dspy.ChainOfThought(Recommendation)

def get_recommendations(prediction):
    return [r for r in prediction.recommendations.splitlines()[1:] if r]

def assessment_metric(example, prediction, trace=None, logger=None):
    # Store recommendations for debugging purposes
    if logger:
        logger.write(prediction.recommendations)

    # Assess recommendations
    contract, negotiation_playbook = example.contract, example.negotiation_playbook
    recommendations = get_recommendations(prediction)
    assessment = Assessment()
    for recommendation in recommendations:
        assessment.add_question(
            "Is the recommendation consistent with the negotiation playbook?",
            1,
            negotiation_playbook=negotiation_playbook,
            recommendation=recommendation,
        )
        assessment.add_question(
            "Can the recommendation be applied to the contract?",
            1,
            contract=contract,
            recommendation=recommendation,
        )

    return assessment.total(trace, 1)


class Logger:
    def __init__(self, path):
        self.path = path
        self.lock = threading.Lock()
        self.log_count = 0

    def write(self, s):
        self.lock.acquire()
        try:
            directory = f"output/{self.path}"
            if not os.path.exists(directory):
                os.makedirs(directory)
            log = open(f"{directory}/{self.log_count}.txt", "w")
            log.write(s)
            log.close()
            self.log_count += 1
        finally:
            self.lock.release()


def create_assessment_metric(path):
    logger = Logger(path)
    def metric(*args, **kwargs):
        return assessment_metric(*args, **kwargs, logger=logger)
    return metric

TRAINING_DATA = [
    dspy.Example(
        contract=get_text("dspy_intro/data/contracts/lease_agreement.txt"),
        negotiation_playbook=get_text("dspy_intro/data/playbooks/lease_agreements.txt"),
    ).with_inputs('contract', 'negotiation_playbook'),
    dspy.Example(
        contract=get_text("dspy_intro/data/contracts/master_services_agreement.txt"),
        negotiation_playbook=get_text("dspy_intro/data/playbooks/master_services_agreements.txt"),
    ).with_inputs('contract', 'negotiation_playbook'),
    dspy.Example(
        contract=get_text("dspy_intro/data/contracts/non_disclosure_agreement.txt"),
        negotiation_playbook=get_text("dspy_intro/data/playbooks/non_disclosure_agreements.txt"),
    ).with_inputs('contract', 'negotiation_playbook'),
    dspy.Example(
        contract=get_text("dspy_intro/data/contracts/severance_agreement.txt"),
        negotiation_playbook=get_text("dspy_intro/data/playbooks/severance_agreements.txt"),
    ).with_inputs('contract', 'negotiation_playbook'),
    dspy.Example(
        contract=get_text("dspy_intro/data/contracts/data_processing_agreement.txt"),
        negotiation_playbook=get_text("dspy_intro/data/playbooks/data_processing_agreements.txt"),
    ).with_inputs('contract', 'negotiation_playbook'),
]