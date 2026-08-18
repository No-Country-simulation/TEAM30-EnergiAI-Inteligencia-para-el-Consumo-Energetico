CREATE TABLE IF NOT EXISTS recomendacion (
    id SERIAL PRIMARY KEY,
    descripcion TEXT NOT NULL,
    analisis_id INTEGER NOT NULL,
    CONSTRAINT fk_recomendacion_analisis
        FOREIGN KEY (analisis_id)
        REFERENCES analisis_energetico(id)
        ON DELETE CASCADE
    );

COMMENT ON TABLE recomendacion IS 'Tabla que almacena las recomendaciones asociadas a los análisis';
COMMENT ON COLUMN recomendacion.analisis_id IS 'ID del análisis al que pertenece esta recomendación';