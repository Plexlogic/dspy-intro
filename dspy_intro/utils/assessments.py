import dspy
import re
import sys

ASSESSMENT_SIGNATURES = {}


class Assess(dspy.Signature):
    assessed_text = dspy.InputField()
    assessment_question = dspy.InputField()
    assessment_answer = dspy.OutputField(desc="Yes or No")

def abbreviate(s, length=200):
    s = re.sub("\n+", " | ", s)
    return s if len(s) <= length else (s[:length - 3] + "...")

def get_assessment_signature(**kwargs):
    key = ",".join(kwargs.keys())
    if key not in ASSESSMENT_SIGNATURES:
        fields = {
            'assessment_question': dspy.InputField(),
            'assessment_answer': dspy.OutputField(desc="Yes or No"),
        }
        for kwarg in kwargs:
            fields[kwarg] = dspy.InputField()
        ASSESSMENT_SIGNATURES[key] = type('CustomAssess', (dspy.Signature,), fields)
    return ASSESSMENT_SIGNATURES[key]


class Assessment():
    total_weight = 0
    total_value = 0

    def add_question(self, assessment_question, weight=1, **kwargs):
        AssessSignature = get_assessment_signature(**kwargs)
        assessment_answer = dspy.ChainOfThought(AssessSignature)(
            assessment_question=assessment_question,
            **kwargs,
        ).assessment_answer

        if "debug_assessments" in sys.argv:
            print(abbreviate(assessment_question))
            for kwarg in kwargs:
                print(abbreviate(kwarg + '=' + kwargs[kwarg]))
            print(abbreviate(assessment_answer))
            print()

        self.add_score(1 if assessment_answer.lower() == 'yes' else 0, weight)

    def add_score(self, value, weight=1):
        self.total_weight += weight
        self.total_value += value

    def total(self, trace, threshold=1):
        total = self.total_value / self.total_weight
        print(f"Assessment: {total}")
        if trace is not None:
            return total
        return total
        result = total >= threshold
        return True if result else [False]

def example_metric(gold, pred, trace=None):
    question, answer, tweet = gold.question, gold.answer, pred.output
    
    if len(tweet) > 280:
        return 0

    assessment = Assessment(tweet)
    assessment.add_question("Does the assessed text make for a self-contained, engaging tweet?", 1)
    assessment.add_question(f"The text should answer `{question}` with `{answer}`. Does the assessed text contain this answer?", 1)

    correct, engaging = [m.assessment_answer.lower() == 'yes' for m in [correct, engaging]]
    score = (correct + engaging) if correct and (len(tweet) <= 280) else 0

    return assessment.total(trace, 1)