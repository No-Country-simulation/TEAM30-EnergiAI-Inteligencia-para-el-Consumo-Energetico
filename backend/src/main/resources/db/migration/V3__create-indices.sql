CREATE INDEX idx_analisis_fecha ON analisis_energetico(fecha_analisis);
CREATE INDEX idx_analisis_categoria ON analisis_energetico(categoria);
CREATE INDEX idx_recomendacion_analisis_id ON recomendacion(analisis_id);