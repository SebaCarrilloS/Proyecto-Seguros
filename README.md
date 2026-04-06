# 🛡️ Insurance Portfolio Optimization

## 🎯 Objetivo

Desarrollar un modelo de severidad de siniestros y simular estrategias de pricing con el objetivo de mejorar la rentabilidad de un portafolio de seguros.

---

## 🧠 Problema de negocio

En la industria aseguradora, una parte importante de las pérdidas suele concentrarse en un subconjunto reducido de clientes.  
El desafío es identificar estos segmentos de alto riesgo y definir estrategias que permitan optimizar el pricing y mejorar la rentabilidad del portafolio.

---

## 🧱 Enfoque del proyecto

El proyecto se desarrolló de forma end-to-end, abarcando desde el análisis exploratorio hasta la simulación de decisiones de negocio:

### 1. 📊 Análisis exploratorio (EDA)
- Evaluación de la distribución de pérdidas (`loss`)
- Identificación de comportamiento heavy-tail
- Análisis de concentración de riesgo (curva tipo Pareto)

### 2. 🛠️ Feature Engineering
- Transformación logarítmica del target
- Clasificación de variables categóricas por cardinalidad
- Aplicación de:
  - One-hot encoding (baja cardinalidad)
  - Target encoding con suavizado (media/alta cardinalidad)
- Separación train/validation para evitar data leakage

### 3. 🤖 Modelamiento
- Modelo baseline: Ridge Regression
- Modelo principal: LightGBM
- Evaluación en:
  - escala logarítmica
  - escala original (interpretación de negocio)

### 4. 💰 Simulación de pricing
- Estimación de pérdidas esperadas
- Definición de primas con margen
- Simulación de estrategias de pricing diferenciadas
- Evaluación de impacto en profit

---

## 📊 Resultados principales

- El **20% de los siniestros concentra aproximadamente XX% de las pérdidas**.
- Se identifican segmentos de alto riesgo con menor rentabilidad bajo pricing uniforme.
- La aplicación de pricing diferenciado permite mejorar el profit total en aproximadamente **$XX**.

---

## 💡 Insights de negocio

- El riesgo no está distribuido uniformemente, sino altamente concentrado.
- Estrategias focalizadas en segmentos de alto riesgo tienen alto impacto en la rentabilidad.
- Los modelos predictivos permiten transformar datos en decisiones concretas de pricing.

---

## 🧠 Conclusión

El uso de modelos de machine learning, combinado con una estrategia de pricing basada en riesgo, permite optimizar la rentabilidad del portafolio asegurador y mejorar la toma de decisiones.

---

## 🛠️ Tecnologías utilizadas

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- LightGBM  
- Matplotlib  

---

## 📁 Estructura del proyecto

insurance_project/
│
├── notebooks/
│ ├── 01_eda.ipynb
│ ├── 02_feature_engineering.ipynb
│ ├── 03_modeling.ipynb
│ ├── 04_pricing_simulation.ipynb
│
├── data/
│ ├── raw/
│ ├── processed/
│
├── src/
│
├── main.py
└── README.md



---

## 🚀 Cómo ejecutar el proyecto

1. Ejecutar notebooks en orden:
   - 01_eda.ipynb  
   - 02_feature_engineering.ipynb  
   - 03_modeling.ipynb  
   - 04_pricing_simulation.ipynb  

2. Ejecutar pipeline:

```bash
python main.py
