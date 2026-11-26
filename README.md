# Alarm Threshold Transfer Across Networks (OCAD-TT)

Label-free threshold setting in one-class network anomaly detection (Isolation Forest, autoencoder).
Graduation Project 1, Ankara Science University, Department of Computer Engineering. Based on our TÜBİTAK 2209-A proposal.

**Team (Group 32, ABC Team):** Berra Bayındır, Ceren Torun, Aslıhan Kaçmaz
**Advisor:** Assist. Prof. Dr. Didem Tufan

## Problem
One-class detectors are trained on normal traffic only and need an alarm threshold. A threshold tuned on one network can produce far more false alarms, or miss attacks, on another network where no attack labels exist. We measure how reliable such thresholds are after transfer, compare label-free ways to reset them, and compare results with finite-sample theory.

## v0 scenario
1. Train an Isolation Forest on normal flows of NF-UNSW-NB15-v2 only.
2. Set the source threshold as the (1 − α) percentile of normal validation scores.
3. Apply it unchanged to a small subsample of NF-CSE-CIC-IDS2018-v2.
4. Report the false positive rate (FPR) and the violation ratio (FPR / α).

## Getting started
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/theory_bound.py       # reproduces the theoretical bounds (Table 3 of the proposal)
```
Datasets are not stored in this repository. Download them from the University of Queensland NetFlow datasets page and place them under `data/`.

## Repository structure
- `src/` data preparation, models, threshold methods, theoretical bound script
- `notebooks/` exploration and experiments
- `docs/` GP1 report and notes
- `data/` local datasets (git-ignored)

## Status
Work in progress. v0 is due in January 2027.
