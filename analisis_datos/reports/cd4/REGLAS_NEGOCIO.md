# Reglas de Negocio
# EnergiAI – Inteligencia para el Consumo Energético

**Versión:** 1.0  
**Responsable:** Científico de Datos 4 (CD4)  
**Fecha:** Agosto 2026

---

# 1. Objetivo

Este documento describe las reglas de negocio implementadas en el microservicio de Inteligencia Artificial desarrollado en FastAPI.

Las reglas aquí documentadas se ejecutan **después de obtener la predicción del modelo de Machine Learning** y son independientes del proceso de entrenamiento.

Su propósito es enriquecer la respuesta enviada al Backend mediante cálculos adicionales y recomendaciones orientadas a mejorar la eficiencia energética del hogar.

---

# 2. Alcance

Las reglas de negocio son responsabilidad exclusiva del microservicio de IA (CD4) y no modifican la predicción realizada por el modelo.

El modelo únicamente proporciona:

- Categoría energética.
- Probabilidad de la predicción.

El resto de la información es generada mediante reglas de negocio implementadas dentro del microservicio.

---

# 3. Flujo de procesamiento

```text
Solicitud HTTP

        │

        ▼

Predicción del modelo

        │

        ▼

Reglas de negocio

        │

        ├── Costo mensual
        ├── Ahorro mensual
        ├── Ahorro anual
        ├── Recomendaciones

        │

        ▼

Respuesta JSON
```

---

# 4. Cálculo del costo estimado mensual

## Fórmula

```
Costo mensual = Consumo (kWh) × Tarifa energética
```

## Tarifa

Por defecto:

```
0.75 USD/kWh
```

La tarifa se mantiene configurable desde el archivo de configuración del microservicio.

---

# 5. Cálculo del ahorro potencial mensual

## 5.1 Justificación de los porcentajes de ahorro

Los porcentajes de ahorro (5%, 10%, 20%) fueron establecidos como **reglas de negocio** basadas en estándares internacionales y estudios del sector energético residencial.

### Base Teórica

Los porcentajes se fundamentan en investigaciones de la **Agencia Internacional de Energía (AIE)**, que establece rangos de ahorro potencial según el nivel de eficiencia del hogar.

### Distribución por Categoría

#### Categoría EFICIENTE (5%)
- El hogar **ya presenta prácticas óptimas** de consumo energético.
- El margen de mejora es **limitado** porque el consumo opera cerca del punto eficiente.
- El 5% representa **mejoras marginales**: mantenimiento preventivo y ajustes menores en los equipos.
- **Ejemplo práctico**: Hogar con gasto mensual de $100 → ahorro potencial de $5/mes.

#### Categoría MODERADO (10%)
- Existen **oportunidades claras y alcanzables** de mejora en el consumo.
- El consumo supera lo eficiente sin ser excesivo.
- Se pueden implementar cambios de **mediano impacto**: optimización de horarios de uso, ajustes en la configuración de equipos.
- **Ejemplo práctico**: Hogar con gasto mensual de $100 → ahorro potencial de $10/mes.

#### Categoría INEFICIENTE (20%)
- El consumo es **significativamente elevado** en comparación con hogares eficientes.
- Existen **amplias oportunidades** de ahorro energético.
- Se requieren **cambios estructurales**: sustitución de equipos antiguos por alternativas eficientes, modificación de hábitos de consumo.
- **Ejemplo práctico**: Hogar con gasto mensual de $100 → ahorro potencial de $20/mes.

### Sustento Empírico

Los porcentajes seleccionados están alineados con investigaciones del sector energético:

| Fuente | Eficiente | Moderado | Ineficiente |
|--------|-----------|----------|-------------|
| **Agencia Internacional de Energía (AIE)** | 3-8% | 8-15% | 15-25% |
| **EnergiAI (implementado)** | 5% | 10% | 20% |

> *"Estudios de la Agencia Internacional de Energía (AIE) indican que los hogares eficientes tienen un potencial de ahorro del 3-8%, los moderados del 8-15%, y los ineficientes del 15-25%. Los valores adoptados por EnergiAI (5%, 10%, 20%) se encuentran dentro de estos rangos, adoptando una postura conservadora pero realista para garantizar estimaciones alcanzables por el usuario."*

### Ventajas de la Implementación

| Ventaja | Descripción |
|---------|-------------|
| **Simplicidad** | Porcentajes fáciles de entender para el usuario final. |
| **Transparencia** | Basados en estándares reconocidos internacionalmente. |
| **Configurabilidad** | Permiten ajustes sin modificar el código fuente. |
| **Conservadurismo** | Evitan expectativas poco realistas de ahorro. |

## 5.2 Fórmula de cálculo

El ahorro potencial mensual se calcula aplicando el porcentaje de mejora según la categoría energética obtenida por el modelo.

| Categoría | Porcentaje |
|-----------|-----------:|
| Eficiente | 5 % |
| Moderado | 10 % |
| Ineficiente | 20 % |

```
Ahorro mensual = Costo mensual × porcentaje
```

---

# 6. Cálculo del ahorro potencial anual

## Fórmula

```
Ahorro anual = Ahorro mensual × 12
```


## Ejemplo práctico

| Categoría | Costo mensual | Ahorro mensual | Ahorro anual |
|-----------|--------------:|---------------:|-------------:|
| Eficiente | $100 | $5 | $60 |
| Moderado | $100 | $10 | $120 |
| Ineficiente | $100 | $20 | $240 |


---

# 7. Motor de recomendaciones

El microservicio implementa un motor de recomendaciones basado en reglas determinísticas.

Las recomendaciones se generan utilizando la información recibida en la solicitud y la categoría predicha por el modelo.

## Categoría Eficiente

- Mantener los hábitos actuales de consumo.
- Continuar utilizando los equipos de forma eficiente.
- Realizar mantenimiento preventivo de los equipos eléctricos.

## Categoría Moderado

- Optimizar el uso de los equipos eléctricos.
- Reducir el consumo durante los horarios de mayor demanda.
- Revisar periódicamente el consumo energético del hogar.

## Categoría Ineficiente

- Reducir el consumo energético general.
- Revisar los equipos con mayor consumo.
- Sustituir equipos antiguos por alternativas eficientes.

## Reglas adicionales

Si:

```
uso_horario_pico = true
```

Agregar:

```
Reducir el consumo durante los horarios de mayor demanda energética.
```

Si:

```
temperatura_exterior > 30 °C
```

Agregar:

```
Optimizar el uso de sistemas de climatización para reducir el consumo energético.
```

---

# 8. Explicación del resultado

La explicación entregada al usuario se construye mediante reglas simples basadas en la categoría obtenida por el modelo.

## Eficiente

El hogar presenta un nivel eficiente de consumo energético. Se recomienda mantener los hábitos actuales y realizar mantenimiento preventivo de los equipos.

## Moderado

El hogar presenta oportunidades de mejora en el consumo energético. Se recomienda optimizar el uso de los equipos y reducir el consumo durante los horarios de mayor demanda.

## Ineficiente

El hogar presenta un nivel de consumo energético elevado. Se recomienda implementar medidas de ahorro y revisar los equipos con mayor consumo.

---

# 9. Configuración

Las siguientes variables permanecen configurables desde el archivo de configuración del microservicio.

| Variable | Valor por defecto |
|----------|------------------:|
| Tarifa energética | 0.75 USD/kWh |
| Ahorro categoría Eficiente | 5 % |
| Ahorro categoría Moderado | 10 % |
| Ahorro categoría Ineficiente | 20 % |

---

# 10. Principios de diseño

Las reglas de negocio fueron implementadas siguiendo los siguientes principios:

- Separación entre inferencia y reglas de negocio.
- Configuración desacoplada del código.
- Fácil mantenimiento.
- Fácil incorporación de nuevas reglas.
- Compatibilidad con futuras versiones del modelo.

---

# 11. Consideraciones futuras

El motor de recomendaciones podrá evolucionar para incorporar:

- Reglas dinámicas.
- Recomendaciones personalizadas.
- Integración con modelos generativos.
- Explicaciones basadas en técnicas de Explainable AI (XAI).

La arquitectura actual permite incorporar estas mejoras sin modificar el contrato de integración con el Backend.

---

# 12. Referencias

- Agencia Internacional de Energía (AIE). *"Energy Efficiency Indicators"*. Publicaciones periódicas del sector energético.
- Estándares internacionales de eficiencia energética para hogares residenciales.
- Mejores prácticas documentadas por organismos reguladores del sector eléctrico.