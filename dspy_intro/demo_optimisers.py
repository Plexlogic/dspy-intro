import dspy
from dspy.teleprompt import BootstrapFewShot
from contract_reviews import (
    Recommendation,
    RECOMMENDATION_PREDICTOR,
    TRAINING_DATA,
    create_assessment_metric,
    assessment_metric,
)
from utils.settings import use_openai_model
from dspy.evaluate import Evaluate

use_openai_model("gpt-4o", 1000)
NUM_THREADS = 4

class RecommendationModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.signature = Recommendation
        self.predictor  = RECOMMENDATION_PREDICTOR
        
    def forward(self, **kwargs):
        result = self.predictor(**kwargs)
        return dspy.Prediction(**result)

teleprompter = BootstrapFewShot(
    metric=create_assessment_metric("optimiser"),    
    max_bootstrapped_demos=16, 
    max_labeled_demos=16,
    max_rounds=5,
)

print("\nOptimising...\n")
optimized_program = teleprompter.compile(RecommendationModule(), trainset=TRAINING_DATA)

optimized_program.save("optimized_program.json")

print("\nAssessing unoptimised predictor...\n")
evaluator = Evaluate(devset=TRAINING_DATA, num_threads=NUM_THREADS, display_progress=True, display_table=5)
evaluation = evaluator(RECOMMENDATION_PREDICTOR, metric=create_assessment_metric("unoptimised"))
print(f"Evaluation: {evaluation}")

print("\nAssessing unoptimised predictor (repeat)...\n")
evaluator = Evaluate(devset=TRAINING_DATA, num_threads=NUM_THREADS, display_progress=True, display_table=5)
evaluation = evaluator(RECOMMENDATION_PREDICTOR, metric=create_assessment_metric("unoptimised 2"))
print(f"Evaluation: {evaluation}")

print("\nAssessing optimised predictor...\n")
evaluator = Evaluate(devset=TRAINING_DATA, num_threads=NUM_THREADS, display_progress=True, display_table=5)
evaluation = evaluator(optimized_program, metric=create_assessment_metric("optimised"))
print(f"Evaluation: {evaluation}")
