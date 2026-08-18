package com.g9team30.energiai.domain.analisis.dto.response;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.g9team30.energiai.domain.common.enums.Categoria;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class AnalisisEnergeticoResponseDTO {


    private Integer id;
    private Categoria categoria;
    private Double probabilidad;

    @JsonProperty("costo_estimado_mensual")
    @NotNull
    @Positive
    private Double costoEstimadoMensual;

    @JsonProperty("ahorro_potencial_mensual")
    @NotNull
    @Positive
    private Double ahorroPotencialMensual;

    @JsonProperty("ahorro_potencial_anual")
    @NotNull
    @Positive
    private Double ahorroPotencialAnual;
    private List<String> recomendaciones;
}
