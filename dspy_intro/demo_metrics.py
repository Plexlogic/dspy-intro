from utils.settings import use_openai_model

from dspy.evaluate import Evaluate
from contract_reviews import RECOMMENDATION_PREDICTOR, TRAINING_DATA, create_assessment_metric

use_openai_model("gpt-4o", 500)

evaluator = Evaluate(devset=TRAINING_DATA, num_threads=5, display_progress=True, display_table=5)
evaluator(RECOMMENDATION_PREDICTOR, metric=create_assessment_metric("demo_metrics"))
