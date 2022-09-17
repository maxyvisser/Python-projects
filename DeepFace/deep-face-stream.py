from deepface import DeepFace

DeepFace.stream(
    db_path="~/Pictures",
    model_name="Facenet",
    detector_backend="retinaface")
