# We will define input for each components
# Input to all stages(data ingestion, data validations, model_training, model_evaluation, model_deployment) will be declared over here
# Also Training Pipeline Configuration Class will be declared too

class DataIngestionConfig:...
class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...

