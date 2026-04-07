# 2D Seismic Forward Modeling and Post-Stack Time Migration
### Integrated Framework for Structural Imaging and Signal Analysis
**Author:** Mahla Zafaryazdi

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Field: Geophysics](https://img.shields.io/badge/Field-Geophysics-green.svg)]()

This repository provides a high-fidelity numerical simulation of seismic wave propagation and imaging. It implements the full seismic pipeline—from synthetic velocity model building to advanced **Post-Stack Time Migration (PSTM)** and **Kirchhoff Depth Migration (KDM)**—using Python-based computational tools.

---

## 🛑 Problem Statement: The Challenge of Subsurface Imaging

In seismic exploration, raw data recorded at the surface does not provide a true map of the subsurface. The primary challenge, addressed in this project, is **Spatial Aliasing and Diffraction Overlap**.

When a seismic wave hits a complex boundary (folded, dipping, or discontinuous), it creates **Diffraction Hyperbolas**. As shown in the image below (from Chapter 4, Yilmaz), these hyperbolas obscure the true location, dip, and spatial resolution of reflectors, making structural interpretation impossible without advanced processing.

![Diffraction Hyperbolas in Seismic Data](images/diffractions.png)
*Figure 1: Exploding reflector model showing diffraction hyperbolas (top) overlapping at the surface (bottom).*

This project focuses on **Migration**: a crucial signal processing technique that collapses these hyperbolas and relocates seismic energy to its true spatial $(x, z)$ origin.

---

## 🎯 Project Objectives

Derived from the methodology presented in my final defense (PowerPoint available in the repo), the goals are:
1. **Geometric Modeling:** Construction of complex interfaces including Sinusoidal (folded), Flat, and Dipping (fault-like) reflectors.
2. **Ray Theory Analysis:** Normal-incidence ray tracing and estimation of reflector normals.
3. **Seismic Synthesis:** Generating unmigrated zero-offset sections using a **60 Hz Ricker Wavelet**.
4. **Advanced Imaging:** Comparative analysis of PSTM (Time-Domain) vs. KDM (Depth-Domain) migration algorithms.

---

## 🧠 Connection to Machine Learning & Geophysics

This framework serves as a robust **Synthetic Data Generator** for modern ML applications in Earth Science:
- **Automatic Picking:** Training architectures like **UNet/CNN** for layered boundary detection.
- **Inversion:** Generating training pairs for Physics-Informed Neural Networks (**PINNs**).

---

## 📊 Results: A Comparative Look

### Time Migration vs. Depth Migration
Migration effectively focuses seismic energy, transforming uninterpretable time sections into a clear structural map. Note the subtle differences in layer positioning between PSTM and KDM, highlighting the importance of proper structural imaging.

| Post-Stack Time Migration (PSTM) | Kirchhoff Depth Migration (KDM) |
| :---: | :---: |
| *Structural positioning in **Seconds*** | *Structural map in **Meters*** |
| ![PSTM](images/final_migration_time.png) | ![KDM](images/final_migration_depth.png) |
## 📊 Dynamic Migration Workflow Analysis

The core of this seismic imaging framework is the ability to collapse diffraction energy and relocate reflections to their true spatial coordinates. The animation below demonstrates the step-by-step transition of the seismic data:

1. **Unmigrated Time Section (Raw Data):** Characterized by overlapping diffraction hyperbolas and structural distortions.
2. **Post-Stack Time Migration (PSTM):** Collapses hyperbolas to their apexes, significantly improving lateral resolution in the time domain.
3. **Kirchhoff Depth Migration (KDM):** Converts the time-section into a true structural depth map (meters), providing the final geological interpretation.

![Seismic Migration Workflow](images/migration_comparison.gif)
*Animation: Transition from raw data (Fig 3) to Time Migration (Fig 4) and Depth Migration (Fig 5).*

## 🖼 Project Workflow & Visual Results

### 1. Model Geometry & Velocity Field
The initial structural model consists of three primary reflectors: Sinusoidal, Flat, and Dipping layers.
![Model Geometry](images/2.png)

### 2. Ray Tracing Analysis
Normal-incidence rays were traced to understand the wave propagation paths.
![Ray Tracing](images/5.png)

### 3. Zero-Offset Section (Unmigrated)
The exploding reflector model results in complex diffraction patterns and overlapping energy.
![Zero-Offset Data](images/6.png)

### 4. Migration Results (Time vs. Depth)
Below is the comparison between the processed sections.
| Post-Stack Time Migration (PSTM) | Post-Stack Depth Migration (PSDM) |
| :---: | :---: |
| ![PSTM](images/7.png) | ![PSDM](images/5.png) |


## 💡 Key Insights & Concluding Remarks

1. **The Exploding Reflector Model (ERM) vs. Zero-Offset Mapping:**
   To simulate the seismic section, we utilized two fundamental concepts as illustrated in the provided figures:
   ![exploding reflector model](images/1.png)
   * **(a) Exploding Reflector Model:** In this theoretical approach, the reflectors "explode" at $t=0$. The wave travels only **upward** to the surface. To compensate for the one-way travel time, we use **half the true medium velocity** ($V/2$).
   * **(b) Zero-Offset Model:** This represents the actual acquisition geometry where a source and receiver are co-located. The recorded time is the **two-way travel time** (downward + upward), using the **full velocity** of the medium.
   * *Conclusion:* Our simulation successfully maps the complex diffraction patterns by honoring these wave propagation physics.

2. **Diffraction Resolution:** The implementation effectively demonstrated the "bow-tie" effect and overlapping diffractions caused by complex subsurface geometries, particularly in the Sinusoidal layer.

3. **Time vs. Depth Limitation:** While **Post-Stack Time Migration (PSTM)** successfully collapsed diffraction hyperbolas, it remains in the time domain. For accurate structural interpretation, **Post-Stack Depth Migration (PSDM)** is required to transform the image into the depth domain (meters).

4. **Future Enhancements:** Implementing **Pre-Stack Migration** and iterative velocity analysis would be the next step to handle strong lateral velocity variations more accurately.
---

## 📧 Contact
**Mahla Zafaryazdi Mohajer** - [mahlazafar8@gmail.com| mmphajer25@ku.edu.tr | mahla.zafar@aut.ac.ir] 