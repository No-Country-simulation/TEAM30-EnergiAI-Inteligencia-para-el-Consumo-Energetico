ALTER TABLE analisis_energetico
    ADD COLUMN usuario_id INTEGER;

CREATE INDEX idx_analisis_usuario_id
    ON analisis_energetico(usuario_id);