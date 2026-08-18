package com.g9team30.energiai.infra.persistence.repository;

import com.g9team30.energiai.infra.persistence.entity.Recomendacion;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface RecomendacionRepository extends JpaRepository<Recomendacion, Integer> {

    List<Recomendacion> findByAnalisisId(Integer analisisId);
}