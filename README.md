# Pedestrian Detection Under Low-Light Conditions

This repository contains Python scripts for video inference and analysis from my University of Galway master's project on low-light pedestrian detection. The experiments used YOLO to analyse recorded video and compare pedestrian detection confidence under low- and high-beam lighting. The project also used an Arduino-based RGB sensor setup to collect lighting measurements. The Arduino sketch, experiment videos, model weights and input CSVs are not included.

## Analysis scripts

- [`calc_confi.py`](calc_confi.py) and [`high_beam.py`](high_beam.py) use Ultralytics YOLO and OpenCV for video inference. They expect the trained weights at `runs/detect/train4/weights/best.pt` and require the video paths to be set for your environment.
- [`low_sce.py`](low_sce.py) and [`conf_illu.py`](conf_illu.py) plot detection confidence against measured illumination for the low-beam and high-beam runs, respectively.
- [`calc.py`](calc.py) joins weighted confidence and illumination by video name and plots both lighting conditions. It keeps rows with weighted confidence of at least 0.60.

## Reproducing the comparison plot

Install pandas and Matplotlib. Place the following experiment CSVs in the working directory, then run `python calc.py`.

| Condition | Weighted confidence | Illumination |
| --- | --- | --- |
| Low beam | `final_weighted_confidence_low_beam.csv` | `Low_Light_with_Illumination_with_Video_Name.csv` |
| High beam | `final_weighted_confidence_high_beam.csv` | `High_Beam_with_Illumination_with_Video_Name.csv` |

The confidence files need `Video Name` and `Weighted Confidence` columns. The illumination files need `Video Name` and `Illumination` columns. The experiment CSVs are required inputs and are external to this repository.

The current plot draws its reference line at 0.50, although the data filter and legend use 0.60. The comparison shows detector confidence for the retained rows.
