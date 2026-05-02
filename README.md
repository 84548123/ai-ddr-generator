# 🏠 AI DDR Report Generator

## 📌 Overview
This project builds an AI-powered pipeline that converts inspection reports and thermal imaging data into structured, client-ready Detailed Diagnostic Reports (DDR).

## 💡 Key Highlights
- Multi-source data fusion (Inspection + Thermal)
- Structured information extraction
- Conflict-aware reasoning (no hallucination)
- Fault-tolerant pipeline with fallback logic
- Automated PDF report generation

## 🧠 Architecture
PDF → Extraction → Chunking → Structured Data → Conflict Resolver → DDR Generator → PDF Output

## ⚙️ Reliability Features
- Handles missing data explicitly ("Not Available")
- Detects inconsistencies between sources
- Fallback system when API fails

## 📄 Sample Output
(https://github.com/84548123/ai-ddr-generator/blob/main/Output/final_ddr.pdf)

## 🎥 Demo
(https://www.loom.com/share/66ac5094cb9d48ee975a3483bb4dd65b)
