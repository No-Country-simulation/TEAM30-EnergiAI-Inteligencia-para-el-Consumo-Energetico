package com.g9team30.energiai.domain.analisis.dto.response;

import com.g9team30.energiai.domain.common.enums.Categoria;
import lombok.Data;

import java.util.List;

@Data
public class AnalisisEnergeticoResponseDTO {

    private Categoria categoria;
    private Double probabilidad;
    private Double costoEstimadoMensual;
    private Double ahorroPotencialMensual;
    private Double ahorroPotencialAnual;
    private List<String> recomendaciones;
}
