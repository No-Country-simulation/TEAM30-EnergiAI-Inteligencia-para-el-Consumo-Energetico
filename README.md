<div align="center">
  
  # ⚡ EnergiAI 
  ### *Inteligencia para el Consumo Energético*

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
  ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
  ![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
  ![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
  ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
  ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

</div>

<br>

> Proyecto desarrollado por el **TEAM30** para el **Hackathon ONE G9 – Alura + Oracle**.

## 🌍 Introducción

**EnergiAI** es una solución desarrollada enfocada en analizar el consumo energético de viviendas y pequeños establecimientos mediante técnicas de Ciencia de Datos e Inteligencia Artificial. 

El proyecto busca identificar patrones de consumo, calcular un Índice de Eficiencia Energética (IEE), clasificar el nivel de eficiencia energética y generar recomendaciones personalizadas que ayuden a optimizar el consumo eléctrico y reducir el costo estimado de la energía.

## 🎯 Objetivos

* Analizar patrones de consumo energético.
* Identificar las variables que influyen en la eficiencia energética.
* Construir un Índice de Eficiencia Energética (IEE).
* Entrenar un modelo de Machine Learning para clasificar el nivel de eficiencia.
* Generar recomendaciones inteligentes basadas en los resultados del modelo.
* Integrar el modelo mediante un microservicio desarrollado con FastAPI para su consumo desde un backend en Spring Boot.

## 🏗️ Arquitectura y Tecnologías

La solución está compuesta por los siguientes componentes:
* **Frontend:** (Por definir).
* **Backend:** Desarrollado en **Java 21** con el framework **Spring Boot**. Implementa **Spring Security** para la protección y autenticación de la API, **Spring Data JPA** para la persistencia, **Flyway** para el control de versiones y migraciones de la base de datos, y **Lombok** para la optimización del código. El motor de base de datos utilizado es **PostgreSQL**.
* **Inteligencia Artificial:** Microservicio desarrollado con FastAPI (Python) y modelo de Machine Learning (Scikit-Learn) serializado en formato `.pkl`.
* **Infraestructura:** Despliegue sobre Oracle Cloud Infrastructure (OCI).
* **Testing:** Pruebas de integración y API realizadas con Postman.

### Estado de la arquitectura
* ✅ Arquitectura definida.
* ✅ Microservicio de Inteligencia Artificial desarrollado.
* 🚧 Integración con Backend en desarrollo.

> *Nota: El diagrama de arquitectura se encuentra documentado en la Wiki del proyecto y será actualizado conforme avance el desarrollo.*

---

## 🚀 Estado actual del proyecto

### 📊 Ciencia de Datos ✅
El equipo de Ciencia de Datos completó todas las etapas planificadas para el desarrollo del modelo de Inteligencia Artificial.

* **CD1 – Análisis Exploratorio de Datos (EDA):** Exploración de datasets, evaluación de calidad de datos, análisis estadístico y detección de patrones relevantes. *(Finalizado)*
* **CD2 – Preparación de los Datos:** Limpieza, Feature Engineering, construcción del dataset consolidado y separación Train/Test. *(Finalizado)*
* **CD3 – Modelado:** Construcción del IEE, entrenamiento y comparación de modelos, evaluación y exportación del modelo seleccionado en `.pkl`. *(Finalizado)*
* **CD4 – Inteligencia de Negocio e Integración:** Desarrollo del motor de recomendaciones, simulaciones de consumo, cálculo de costos/ahorros y desarrollo del microservicio FastAPI. *(Finalizado)*

### 🧪 Testing y QA ✅
Se desarrolló y ejecutó un script de validación de integración que superó con un **100% de éxito** las pruebas sobre el modelo y las reglas de negocio, incluyendo:
* Validación del Contrato API v2.0 (entradas y salidas).
* Exactitud de los cálculos financieros (costos y ahorros).
* Respuesta ante Casos Extremos (Out of Domain) documentados.

### ⚙️ Backend 🚧
Actualmente el equipo de Backend se encuentra desarrollando la integración de la aplicación con el microservicio de Inteligencia Artificial.

* Integración de Spring Boot con el microservicio en FastAPI.
* Consumo de la API REST del modelo de IA.
* Integración de las respuestas dentro del flujo de la aplicación.
* Pruebas de integración y validación de la comunicación. *(En desarrollo)*

### 🎨 Frontend (Por definir)
* Diseño de interfaces de usuario.
* Consumo de APIs del backend.
* Visualización de datos y recomendaciones.

---

## 🛤️ Próximos pasos

1. Finalizar la integración entre Spring Boot y el microservicio de Inteligencia Artificial.
2. Validar el intercambio de datos mediante la API REST.
3. Realizar pruebas funcionales de extremo a extremo.
4. Desplegar los componentes en Oracle Cloud Infrastructure (OCI).
5. Preparar la solución para la demostración final del hackathon.

---

## 🔗 Enlaces del Proyecto

* 📂 **Repositorio:** [TEAM30-EnergiAI](https://github.com/No-Country-simulation/TEAM30-EnergiAI-Inteligencia-para-el-Consumo-Energeticoo)
* 📖 **Wiki del Proyecto:** [Documentación Oficial](https://github.com/No-Country-simulation/TEAM30-EnergiAI-Inteligencia-para-el-Consumo-Energetico/wiki)
* 📋 **Tablero Kanban:** [Gestión de Tareas](https://github.com/orgs/No-Country-simulation/projects/4499)

---

## 👥 El Equipo (TEAM30)

* **Julio Cesar Solano** - Data Scientist
* **Walter Cosme Tejerina** - QA Tester
* **Hernan Camoretti** - Full Stack Developer
* **Mabel Iris Esmeralda Cárdenas Fernández** - Backend Developer
* **Jorge Isaac Gongora Naranjo** - Data Scientist
* **Juan Esteban Rodríguez Aranda** - Data Analyst
* **Adriana Rodriguez** - Data Scientist
* **Geremy Quiñonez** - Backend Developer

<br>

<div align="center">
  <i>Última actualización: 10 de agosto de 2026</i><br>
  
