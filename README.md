<div align="center">
  
  # ⚡ EnergiAI 
  ### *Inteligencia para el Consumo Energético*

  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
  ![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
  ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
  ![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
  ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
  ![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
  ![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
  ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

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
* **Frontend:** Desarrollado con **JavaScript**, **Vite** y **Tailwind CSS**, ofreciendo una interfaz responsiva y ágil.
* **Backend:** Desarrollado en **Java 21** con el framework **Spring Boot**. Implementa **Spring Security**, **Spring Data JPA** para la persistencia, **Flyway** para migraciones y **Lombok**. El motor de base de datos es **PostgreSQL**. Se configuró **Swagger/OpenAPI** para la documentación de los endpoints.
* **Inteligencia Artificial:** Microservicio desarrollado con FastAPI (Python) y modelo de Machine Learning (Scikit-Learn) serializado en formato `.pkl`.
* **Infraestructura:** Despliegue sobre Oracle Cloud Infrastructure (OCI).
* **Testing:** Pruebas de integración, validación de base de datos y scripts automatizados de QA.

### Estado de la arquitectura
* ✅ Arquitectura general definida.
* ✅ Microservicio de Inteligencia Artificial implementado.
* ✅ Backend en Spring Boot finalizado.
* ✅ Frontend integrado y comunicando exitosamente.

---

## 🚀 Estado actual del proyecto

### 📊 Ciencia de Datos ✅
* **CD1 – Análisis Exploratorio de Datos (EDA):** Exploración de datasets, evaluación de calidad de datos y detección de patrones relevantes. *(Finalizado)*
* **CD2 – Preparación de los Datos:** Limpieza, Feature Engineering, construcción del dataset consolidado y separación Train/Test. *(Finalizado)*
* **CD3 – Modelado:** Construcción del IEE, entrenamiento y evaluación de modelos, exportación en `.pkl`. *(Finalizado)*
* **CD4 – Inteligencia de Negocio e Integración:** Desarrollo del motor de recomendaciones, simulaciones de consumo y desarrollo del microservicio FastAPI. *(Finalizado)*

### ⚙️ Backend ✅
El equipo de Backend definió el dominio, configuró el manejo global de excepciones y finalizó la integración bidireccional.

**Modelo de Dominio y Entidades:**
* **AnalisisEnergetico:** Representa el resultado del análisis (`id`, `usuarioId`, `consumoKwh`, `usoHorarioPico`, `cantidadPersonas`, `cantidadEquipos`, `categoria`, `probabilidad`, `costoEstimadoMensual`, `fechaAnalisis`, `temperaturaExterior`).
* **Recomendacion:** Generada a partir del análisis (`id`, `descripcion`, `analisis_id`).
* **Categoria (Enum):** `EFICIENTE`, `MODERADO`, `INEFICIENTE`.

**API REST y Persistencia:**
* **Endpoints Completados:** `POST /analisis`, `GET /analisis/{id}`, y `GET /analisis/usuario/{usuarioId}`.
* **Persistencia:** PostgreSQL con Spring Data JPA. Control de versiones con Flyway (Migraciones V1 a V4 implementando tablas, claves foráneas e índices).
* **Integración:** Flujo completo validado con el microservicio FastAPI.

### 🎨 Frontend ✅
La aplicación web permite al usuario ingresar datos de consumo, ejecutar análisis y visualizar sus resultados dinámicamente.
* **Ingreso de datos:** Formulario accesible para registrar las variables de consumo del hogar (con opción de limpieza).
* **Integración API:** Consumo exitoso de los endpoints de Spring Boot.
* **Visualización:** Presentación clara del perfil energético, nivel de confianza, ahorros estimados y listado de recomendaciones. Historial de consultas implementado.

### 🧪 Testing y Aseguramiento de Calidad (QA) ✅
La suite automatizada audita el sistema de forma modular y End-to-End, garantizando la fiabilidad técnica del producto:

* **Base de Datos (test_qa_database.py):** Verifica la aplicación estricta de migraciones Flyway y claves foráneas en PostgreSQL. **(Éxito: 100.0%)**
* **Microservicio IA (test_qa_fastapi.py):** Valida exactitud de cálculos matemáticos y robustez ante datos inválidos. **(Éxito: 95.3%)**
* **Backend Spring (test_qa_backend.py):** Certifica operaciones CRUD, enrutamiento y manejo de caídas de servicios. **(Éxito: 92.0%)**
* **Flujo Completo E2E (test_qa_e2e.py):** Simula el viaje completo de la información, asegurando mutaciones correctas entre microservicios. **(Éxito: 100.0%)**

**Registro de Incidencias:**
El equipo monitorea observaciones activas (como el comportamiento del endpoint de salud del Backend [BACK-01] y la raíz de FastAPI [API-01]) priorizadas para su resolución previa al despliegue en producción.

---

## 🛤️ Próximos pasos

1. Desplegar los componentes finales en Oracle Cloud Infrastructure (OCI).
2. Ensayo del pitch y grabación del video de demostración de la plataforma.

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
  <i>Última actualización: 22 de agosto de 2026</i><br>
  
</div>
