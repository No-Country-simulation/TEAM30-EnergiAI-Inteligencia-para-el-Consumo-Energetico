package com.g9team30.energiai.infra.persistence.repository;

import com.g9team30.energiai.infra.persistence.entity.AnalisisEnergetico;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface AnalisisEnergeticoRepository extends JpaRepository<AnalisisEnergetico, Integer> {

    List<AnalisisEnergetico> findByUsuarioId(Integer usuarioId);
}