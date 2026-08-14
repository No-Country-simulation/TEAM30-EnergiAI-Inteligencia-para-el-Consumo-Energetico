package com.g9team30.energiai.infra.persistence.repository;

import com.g9team30.energiai.domain.analisis.model.AnalisisEnergetico;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AnalisisEnergeticoRepository extends JpaRepository<AnalisisEnergetico, Integer> {
}