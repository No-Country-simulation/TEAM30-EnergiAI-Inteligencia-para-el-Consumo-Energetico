CREATE TABLE IF NOT EXISTS analisis_energetico (
    id SERIAL PRIMARY KEY,
    consumo_kwh DOUBLE PRECISION NOT NULL,
    uso_horario_pico BOOLEAN NOT NULL,
    cantidad_personas INTEGER NOT NULL,
    cantidad_equipos INTEGER NOT NULL,
    categoria VARCHAR(20) NOT NULL,
    probabilidad DOUBLE PRECISION NOT NULL,
    costo_estimado_mensual DOUBLE PRECISION NOT NULL,
    fecha_analisis TIMESTAMP NOT NULL,
    temperatura_exterior DECIMAL NOT NULL
    );

COMMENT ON TABLE analisis_energetico IS 'Tabla que almacena los análisis energéticos realizados';
COMMENT ON COLUMN analisis_energetico.categoria IS 'Categoría de eficiencia: EFICIENTE, MODERADO, INEFICIENTE';