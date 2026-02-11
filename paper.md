---
title: "dalip-estimator: A lightweight empirical tool for estimating gravitational acceleration from lensing observables"
tags:
  - Python
  - astronomy
  - astrophysics
  - gravitational lensing
  - scientific computing
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

dalip-estimator is a lightweight Python package that provides a fast empirical estimate of effective gravitational acceleration directly from gravitational lensing observables. The software implements a simple algebraic scaling relation between light-deflection angle and impact parameter, enabling rapid exploratory calculations without requiring detailed mass modeling or iterative numerical fitting.

The estimator is intended as a practical computational tool for quick diagnostics, educational demonstrations, and preliminary analysis workflows in gravitational lensing studies. It is presented strictly as a phenomenological estimator rather than a new physical theory. The implementation is inspired by classical gravitational lensing concepts discussed in foundational studies [@einstein1916; @dyson1920; @schneider1992].

# Statement of Need

Estimating gravitational strength from lensing geometry typically involves multi-parameter mass modeling pipelines or numerical optimization procedures. While such approaches are essential for precision analysis, they can be computationally intensive for exploratory studies or rapid parameter scans.

dalip-estimator provides a transparent and easy-to-use alternative that enables users to obtain order-of-magnitude gravitational estimates directly from observable quantities. This makes it useful for:

- preliminary data exploration,
- teaching demonstrations,
- rapid consistency checks,
- lightweight computational workflows.

# Functionality

The package provides:

- empirical estimation of gravitational acceleration from light-deflection data,
- a minimal Python interface for quick calculations,
- reproducible example scripts,
- simple unit conversion handling,
- lightweight implementation designed for clarity and usability.

The approach follows standard gravitational lensing scaling behavior discussed in the literature [@weinberg1972; @schneider1992].

# Example Usage

```python
from dalip_estimator import estimate_g

# Example: Solar limb deflection
g = estimate_g(LB_arcsec=1.75, b_m=6.9634e8)
print(g)
