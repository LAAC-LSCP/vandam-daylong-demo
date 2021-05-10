from ChildProject.projects import ChildProject
from ChildProject.annotations import AnnotationManager
from ChildProject.metrics import segments_to_annotation

from pyannote.metrics.detection import DetectionPrecisionRecallFMeasure

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import normalize

import random

import seaborn as sns
import matplotlib.pyplot as plt

speakers = ['CHI', 'OCH', 'FEM', 'MAL']
sets = ['its', 'vtc (conf 50%)', 'vtc (drop 50%)', 'vtc (conf 75%)', 'vtc (drop 75%)']

project = ChildProject('.')
am = AnnotationManager(project)
am.read()

def confusion(segments, prob):
    segments['speaker_type'] = segments['speaker_type'].apply(
        lambda s: random.choice(speakers) if random.random() < prob else s
    )
    return segments

def drop(segments, prob):
    return segments.sample(frac = 1-prob)

intersection = AnnotationManager.intersection(am.annotations, ['vtc', 'its'])
segments = am.get_collapsed_segments(intersection)
segments = segments[segments['speaker_type'].isin(speakers)]
segments.sort_values(['segment_onset', 'segment_offset']).to_csv('test.csv', index = False)

conf50 = segments[segments['set'] == 'vtc'].copy()
conf50 = confusion(conf50, 0.5)
conf50['set'] = 'vtc (conf 50%)'

conf75 = segments[segments['set'] == 'vtc'].copy()
conf75 = confusion(conf75, 0.75)
conf75['set'] = 'vtc (conf 75%)'

drop50 = segments[segments['set'] == 'vtc'].copy()
drop50 = drop(drop50, 0.5)
drop50['set'] = 'vtc (drop 50%)'

drop75 = segments[segments['set'] == 'vtc'].copy()
drop75 = drop(drop75, 0.75)
drop75['set'] = 'vtc (drop 75%)'

segments = pd.concat([segments, conf50, conf75, drop50, drop75])

metric = DetectionPrecisionRecallFMeasure()

scores = []
for speaker in speakers:
    ref = segments_to_annotation(segments[(segments['set'] == 'vtc') & (segments['speaker_type'] == speaker)], 'speaker_type')

    for s in sets:
        hyp = segments_to_annotation(segments[(segments['set'] == s) & (segments['speaker_type'] == speaker)], 'speaker_type')
        detail = metric.compute_components(ref, hyp)
        precision, recall, f = metric.compute_metrics(detail)

        scores.append({
            'set': s,
            'speaker': speaker,
            'recall': recall,
            'precision': precision,
            'f': f
        })

scores = pd.DataFrame(scores)
scores.to_csv('scores.csv', index = False)

plt.rcParams.update({'font.size': 12})
plt.rc('xtick', labelsize = 10)
plt.rc('ytick', labelsize = 10)

fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize=(6.4*2, 4.8*2))

plt.savefig('Fig4.pdf', bbox_inches = 'tight')
