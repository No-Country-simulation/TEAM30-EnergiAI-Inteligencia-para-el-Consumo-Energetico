package com.g9team30.energiai.infra.persistence.repository;

import com.g9team30.energiai.domain.analisis.model.Recomendacion;
import org.springframework.data.jpa.repository.JpaRepository;

public interface RecomendacionRepository extends JpaRepository<Recomendacion, Integer> {
}