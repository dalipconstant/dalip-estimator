# Dalip Estimator

A simple empirical estimator for gravitational acceleration derived directly from gravitational lensing observables.

This repository provides a minimal Python implementation of the relation

g = (LB × D) / b

which allows fast, first-pass estimates of gravitational acceleration and enclosed mass using only measured light deflection and impact parameter values.

The method is intended as a **phenomenological computational tool**, not a modification of General Relativity.


---

## Formula

Gravitational acceleration:

g = (LB × D) / b

Enclosed mass (Newtonian relation):

M = g b² / G


where

- LB : light deflection angle  
- b  : impact parameter  
- D  : calibrated proportionality coefficient (1.09 × 10¹¹, arcsec-based)  
- G  : gravitational constant  


---

## Features

- Uses only directly observable lensing quantities
- No mass modeling or iterative fitting required
- Unit conversion built-in (arcsec / rad / deg, meters / km / AU / solar radius / light-years)
- Lightweight, single-file Python script
- Designed for quick exploratory or consistency checks


---

## Installation

Requires Python 3.x only.

No external libraries.

