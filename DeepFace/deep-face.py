from deepface import DeepFace

base = "/media/maxy/Seagate Backup Plus Drive/Deepface/known/"

df = DeepFace.find(
    img_path=base,
    db_path="/media/maxy/Seagate Backup Plus Drive/iCloud/",
    model_name="Facenet512",
    distance_metric="euclidean_l2",
    enforce_detection=False,
    detector_backend="retinaface",
    prog_bar=True)

print(df)
