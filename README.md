# Preliminary Hemodialysis Membrane Design

## Overview

This project presents a comprehensive analysis and preliminary design of a **hemodialysis membrane system** for urea removal from blood. The study applies fundamental mass transfer principles including Fick's law, diffusion through membranes, and convective mass transfer to determine the required membrane surface area for effective hemodialysis treatment.

## Project Details

**Course:** CE 318: Heat and Mass Transfer  
**Instructor:** Dr. Dave (Hsinhan) Tsai, PhD  
**Department:** Chemical and Biological Engineering, University at Buffalo  
**Institution:** The State University of New York, Buffalo, New York, 14260-4200, USA

---

## Team Members

- **[Aymen Ahmad](https://www.linkedin.com/in/aymen-ahmad-cbe2027/)**
- **[Kashfy Gazi](https://www.linkedin.com/in/kashfy-gazi-876048397/)** • [GitHub](https://github.com/Kashfy)
- **[Radi Imran](https://www.linkedin.com/in/radiimran/)**
- **[Gabriel Pin de Jesus](https://www.linkedin.com/in/gabrielpindejesus/)**

---

## Project Objectives

The primary goal of this project is to determine the **membrane surface area required** to reduce blood urea concentration from an initial level (2000 mg/L) to a target level (600 mg/L) using mass transfer principles in a hollow fiber hemodialysis system.

## System Description

The project analyzes a **hollow fiber hemodialysis unit** where:
- **Blood** flows through the inside of hollow fibers
- **Dialysate** flows around the outside of the fibers in counter-current configuration
- **Urea** diffuses from the blood side through the membrane to the dialysate side

This configuration provides a large membrane surface area in a compact volume, making it ideal for waste removal from blood in patients with kidney failure.

## Key Design Parameters

### Flow Rates and Concentrations
- Initial urea concentration in blood: **2000 mg/L**
- Target urea concentration after treatment: **600 mg/L**
- Blood volumetric flow rate: **1000 mL/min**
- Dialysate volumetric flow rate: **2400 mL/min**

### Dialyzer Specifications
- Operating temperature: **37.4°C** (physiological body temperature)
- Fiber length: **20 cm**
- Membrane thickness: **25 μm**
- Membrane void fraction: **0.2**
- Hollow fiber diameter: **180 μm**

### Blood and Plasma Properties
- Blood cell volume fraction: **45%**
- Plasma volume fraction: **55%**
- Blood density: **990 kg/m³**
- Blood viscosity: **3.0 cP**
- Protein concentration in plasma: **75 g/L**

## Key Results

| Parameter | Value | Units |
|-----------|-------|-------|
| Dialysate outlet urea concentration | 583.3 | mg/L |
| Temperature-corrected urea diffusivity | 1.87 × 10⁻⁹ | m²/s |
| Effective membrane diffusivity | 3.74 × 10⁻¹⁰ | m²/s |
| Overall mass transfer coefficient | 1.50 × 10⁻⁵ | m/s |
| Log-mean concentration difference | 951 | mg/L |
| **Required membrane surface area** | **1.64** | **m²** |
| Number of hollow fibers | 1.45 × 10⁴ | fibers |
| Estimated membrane cost | 24.60 | $ |

## Governing Equations

The design uses the following key equations:

1. **Overall membrane mass transfer equation:**
   - ṅₐ = Kₒ · Aₘ · ΔC_lm

2. **Required membrane surface area:**
   - Aₘ = [Qb(Cb,i - Cb,o)] / (Kₒ · ΔC_lm)

3. **Log-mean concentration difference:**
   - ΔC_lm = (ΔC₁ - ΔC₂) / ln(ΔC₁/ΔC₂)

4. **Fick's Law of diffusion:**
   - Jₐ = (D_Ae/δₘ) · (C_A,b - C_A,d)

## Major Assumptions

- Steady-state operation with constant flow rates
- Counter-current flow configuration
- Negligible inlet dialysate urea concentration
- Isothermal operation at 37.4°C
- Membrane resistance dominates (blood-side and dialysate-side resistances neglected)
- Urea transport follows Fick's Law
- No pressure-driven ultrafiltration
- Effective diffusivity reduced by membrane void fraction

## Key Findings

The analysis determined that:

✓ A **membrane surface area of 1.64 m²** is required to achieve the desired urea removal  
✓ This corresponds to approximately **14,500 hollow fibers**  
✓ The **log-mean concentration difference of 951 mg/L** provides the driving force for diffusion  
✓ **Urea removal rate of 1400 mg/min** is achieved through the system  
✓ Membrane resistance is the dominant factor limiting mass transfer


## Methodology

The project employs a systematic approach:

1. **System Modeling** - Defined the hemodialysis system as a membrane separation process
2. **Governing Equations** - Applied mass balance and Fick's law of diffusion
3. **Parameter Calculation** - Computed all transport parameters needed for design
4. **Sensitivity Analysis** - Evaluated system response to design parameter variations
5. **Design Optimization** - Determined the optimal membrane surface area

## Applications

This preliminary design has direct applications in:
- Kidney dialysis systems for treating end-stage renal disease (ESRD)
- Medical device engineering and biomedical design
- Mass transfer process design in clinical settings

## Limitations & Future Work

The analysis assumes:
- Blood-side and dialysate-side mass transfer resistances are negligible
- Uniform membrane properties throughout the system
- Steady-state conditions throughout operation

Future improvements could include:
- Consideration of blood-side and dialysate-side resistances
- Non-steady-state transient analysis
- Optimization for multiple performance criteria
- Validation against experimental hemodialysis data

## References

The project references key literature including:
- Azar et al. - Vascular access design
- Yartsev - Physical principles of hemodialysis
- Perez-Garcia et al. - Dialyzer design
- Yehl et al. - Single-use hemodialysis systems

---

## Contact & Links

**Project Repository:** [GitHub - CE-318-Final-Project-Hemodyalasis](https://github.com/Kashfy/CE-318-Final-Project-Hemodyalasis)

**Team LinkedIn Profiles:**
- [Aymen Ahmad](https://www.linkedin.com/in/aymen-ahmad-cbe2027/)
- [Kashfy Gazi](https://www.linkedin.com/in/kashfy-gazi-876048397/)
- [Radi Imran](https://www.linkedin.com/in/radiimran/)
- [Gabriel Pin de Jesus](https://www.linkedin.com/in/gabrielpindejesus/)

---

**Last Updated:** June 2026  
**Status:** Complete
