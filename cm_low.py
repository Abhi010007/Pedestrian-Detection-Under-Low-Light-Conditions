from ultralytics.utils.metrics import ConfusionMatrix
from pathlib import Path
import numpy as np

# Init CM
cm = ConfusionMatrix(nc=1)  # Change nc (num classes) if more

# Paths
pred_dir = Path('runs/detect/predict/labels')
gt_dir = Path("C:/Master_Project/Low_Beam_Results/predict/labels")

for pred_file in pred_dir.glob('*.txt'):
    gt_file = gt_dir / pred_file.name

    # Read predictions: class conf x y w h
    preds = np.loadtxt(pred_file).reshape(-1, 6)[:, [0, 2, 3, 4, 5]]  # remove confidence

    # Read ground truths: class x y w h
    gts = np.loadtxt(gt_file).reshape(-1, 5)

    # Update CM
    cm.process_batch(detections=preds, labels=gts)

# Plot or print matrix
cm.plot(save_dir='.')
print(cm.matrix)
