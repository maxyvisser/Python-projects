from deep_daze import Imagine

imagine = Imagine(
    text="austronaut",
    image_width=256,
    num_layers=16,
    batch_size=1,
    gradient_accumulate_every=16 # Increase gradient_accumulate_every to correct for loss in low batch sizes
)

imagine()