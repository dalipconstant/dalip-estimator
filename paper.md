---
title: "dalip-estimator: A lightweight empirical tool for estimating gravitational acceleration from lensing observables"
tags:
  - Python
  - astronomy
  - gravitational lensing
  - astrophysics
authors:
  - name: Aryan
    affiliation: 1
affiliations:
  - name: Independent Researcher, Delhi, India
    index: 1
date: 2026
bibliography: paper.bib
---

# Summary

dalip-estimator is a lightweight Python tool that provides a fast empirical estimate of effective gravitational acceleration directly from gravitational lensing observables. The estimator uses a simple algebraic relation between light-deflection angle and impact parameter, enabling rapid exploratory calculations without requiring mass modeling or iterative fitting.

The software is intended as a computational tool for quick diagnostics and educational use rather than a new physical theory.

# Statement of Need

Estimating gravitational strength from lensing geometry often requires detailed modeling workflows that may be computationally expensive for exploratory analysis. dalip-estimator provides a simple and transparent alternative for rapid calculations, making it useful for preliminary investigations, teaching demonstrations, and parameter exploration.

# Functionality

The package implements:

- empirical gravitational acceleration estimation
- simple command-line usage
- lightweight Python implementation
- reproducible examples via provided scripts

# Example

```python
from dalip_estimator import estimate_g

g = estimate_g(LB_arcsec=1.75, b_m=6.9634e8)
print(g)
