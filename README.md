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
* **Frontend:** Interfaz de usuario intuitiva y responsiva para la interacción con el sistema.
* **Backend:** Desarrollado en **Java 21** con el framework **Spring Boot**. Implementa **Spring Security** para la protección y autenticación de la API, **Spring Data JPA** para la persistencia, **Flyway** para el control de versiones y migraciones de la base de datos, y **Lombok** para la optimización del código. El motor de base de datos utilizado es **PostgreSQL**.
* **Inteligencia Artificial:** Microservicio desarrollado con FastAPI (Python) y modelo de Machine Learning (Scikit-Learn) serializado en formato `.pkl`.
* **Infraestructura:** Despliegue sobre Oracle Cloud Infrastructure (OCI).
* **Testing:** Pruebas de integración y API realizadas con Postman y scripts automatizados de QA.

### Estado de la arquitectura
* ✅ Arquitectura general definida.
* ✅ Microservicio de Inteligencia Artificial implementado.
* ✅ Backend en Spring Boot finalizado.
* ✅ Frontend integrado y comunicando exitosamente.

> *Nota: El diagrama de arquitectura se encuentra documentado en la Wiki del proyecto.*

---

## 🚀 Estado actual del proyecto

### 📊 Ciencia de Datos ✅
El equipo de Ciencia de Datos completó todas las etapas planificadas para el desarrollo del modelo de Inteligencia Artificial.

* **CD1 – Análisis Exploratorio de Datos (EDA):** Exploración de datasets, evaluación de calidad de datos, análisis estadístico y detección de patrones relevantes. *(Finalizado)*
* **CD2 – Preparación de los Datos:** Limpieza, Feature Engineering, construcción del dataset consolidado y separación Train/Test. *(Finalizado)*
* **CD3 – Modelado:** Construcción del IEE, entrenamiento y comparación de modelos, evaluación y exportación del modelo seleccionado en `.pkl`. *(Finalizado)*
* **CD4 – Inteligencia de Negocio e Integración:** Desarrollo del motor de recomendaciones, simulaciones de consumo, cálculo de costos/ahorros y desarrollo del microservicio FastAPI. *(Finalizado)*

### ⚙️ Backend ✅
El equipo de Backend definió el dominio, las reglas de comunicación y finalizó la integración con el microservicio de Inteligencia Artificial.

**Modelo de Dominio y Entidades:**
* **AnalisisEnergetico:** Representa el resultado del análisis. Campos principales: `id`, `usuarioId`, `consumoKwh`, `usoHorarioPico`, `cantidadPersonas`, `cantidadEquipos`, `categoria`, `probabilidad`, `costoEstimadoMensual`, `fechaAnalisis`, `temperaturaExterior`.
* **Recomendacion:** Generada a partir del análisis. Cada recomendación pertenece a un único análisis. Campos: `id`, `descripcion`, `analisis_id`.
* **Categoria (Enum):** Valores de clasificación energética: `EFICIENTE`, `MODERADO`, `INEFICIENTE`.

**API REST y Base de Datos:**
* **Endpoints Completados:** `POST /analisis`, `GET /analisis/{id}`, y `GET /analisis/usuario/{usuarioId}`.
* **Persistencia:** Utiliza PostgreSQL con Spring Data JPA. El control de versiones se administra con Flyway (Migraciones V1 a V4 implementando tablas, claves foráneas e índices).

### 🎨 Frontend ✅
Se desarrolló una interfaz web funcional que permite al usuario interactuar fluidamente con el motor de predicción.
* **Ingreso de datos:** Formulario accesible para registrar las variables de consumo del hogar.
* **Integración API:** Consumo exitoso de los endpoints de Spring Boot para la creación y recuperación de análisis.
* **Visualización de resultados:** Presentación clara del perfil energético, nivel de confianza, impacto económico (ahorros estimados) y el listado de recomendaciones dinámicas.

### 🧪 Testing y Aseguramiento de Calidad (QA) ✅
La suite automatizada audita el sistema de forma modular y End-to-End, garantizando la fiabilidad técnica del producto:

* **Base de Datos (test_qa_database.py):** Verifica la aplicación estricta de migraciones Flyway, claves foráneas e índices en PostgreSQL. **(Éxito: 100.0%)**
* **Microservicio IA (test_qa_fastapi.py):** Valida exactitud de cálculos matemáticos, inyección de payloads y robustez ante datos inválidos. **(Éxito: 95.3%)**
* **Backend Spring (test_qa_backend.py):** Certifica operaciones CRUD, enrutamiento y manejo de caídas de servicios. **(Éxito: 92.0%)**
* **Flujo Completo E2E (test_qa_e2e.py):** Simula el viaje completo de la información, asegurando mutaciones correctas entre microservicios y consistencia en base de datos. **(Éxito: 100.0%)**

**Configuración del Entorno de Pruebas:**
Requiere dependencias de Python (`psycopg2-binary`, `pydantic-settings`), Java 21 y Docker. Se inicia PostgreSQL, luego FastAPI en el puerto 8000 y finalmente Spring Boot inyectando variables de entorno.

### 🐛 Registro y Resolución de Incidencias
Durante las pruebas de QA, se registraron observaciones (como el endpoint de salud del Backend y la raíz de FastAPI) que el equipo ha ido mitigando de cara al despliegue final en producción.

---

## 🛤️ Próximos pasos

1. Desplegar los componentes finales en Oracle Cloud Infrastructure (OCI).
2. Ensayo del pitch y grabación del video de demostración de la plataforma.
3. Presentación oficial de EnergiAI ante el jurado del hackathon.

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
  <i>Última actualización: 21 de agosto de 2026</i><br>

</div>
