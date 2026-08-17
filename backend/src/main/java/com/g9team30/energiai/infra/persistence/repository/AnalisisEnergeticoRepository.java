package com.g9team30.energiai.infra.persistence.repository;

import com.g9team30.energiai.domain.common.enums.Categoria;
import com.g9team30.energiai.infra.persistence.entity.AnalisisEnergetico;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AnalisisEnergeticoRepository extends JpaRepository<AnalisisEnergetico, Integer> {


    List<AnalisisEnergetico> findByUsuarioId(Integer usuarioId);

    List<AnalisisEnergetico> findByCategoria(Categoria categoria);

    List<AnalisisEnergetico> findByOrderByFechaAnalisisDesc();
}