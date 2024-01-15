# 📊 Normal Distribution of 100 kΩ Resistors

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Statistics-Gaussian-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Sample_Size-1000-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Institute-NSUT-blue?style=for-the-badge" />
</p>

> **Centre for Electronic Design and Technology**  
> Netaji Subhas University of Technology, New Delhi  
> *Date: January 2024*

---

## 📋 Table of Contents
- [Synopsis](#-synopsis)
- [Introduction](#-introduction)
- [Procedure](#-procedure)
- [Results](#-results)
- [Conclusion](#-conclusion)

---

## 🎯 Synopsis

This project involves recording the resistance values of **1000 resistors**, each nominally rated at 100 kΩ, and analyzing the resulting data to verify the presence of a **Gaussian (Normal) distribution**. By measuring and plotting the resistance values, the project aims to observe how closely the distribution of real-world component values follows the theoretical bell curve predicted by statistical manufacturing processes.

## 📖 Introduction

Component values in electronic manufacturing are subject to natural variation due to material properties, fabrication tolerances, and environmental factors. For resistors, this variation is expected to follow a **normal distribution** centered around the nominal value. By measuring a large sample size (n = 1000), statistical significance can be established and the distribution parameters (mean, standard deviation) can be reliably estimated.

## ⚙️ Procedure

1. **1000 resistors** (nominal 100 kΩ) were measured using a digital multimeter
2. Resistance values were recorded in a CSV file
3. Data was analyzed using **Python** with `numpy`, `matplotlib`, and `scipy`
4. Histogram plotted and fitted with a Gaussian curve
5. Statistical parameters (mean, std deviation, variance) were calculated

## 📊 Results

The histogram of measured resistance values shows a clear **bell-shaped distribution** centered near the nominal value of 100 kΩ, confirming the expected Gaussian behavior.

## ✅ Conclusion

The experiment successfully demonstrated that the resistance values of 1000 nominally identical resistors follow a **normal distribution**. The measured mean closely matches the nominal value, and the spread is consistent with the manufacturer's specified tolerance.

## 📦 Bill of Materials

| S.No | Component | Value | Qty |
|------|-----------|-------|-----|
| 1 | Resistor | 100 kΩ (5%) | 1000 |
| 2 | Digital Multimeter | — | 1 |

## 🛠️ Technologies Used

`Python` · `NumPy` · `Matplotlib` · `SciPy` · `Pandas`

## 👥 Authors
- **Ansh Gupta** — NSUT, New Delhi
- **Shubham Kumar** — NSUT, New Delhi

---
*Centre for Electronic Design and Technology, NSUT, New Delhi*
