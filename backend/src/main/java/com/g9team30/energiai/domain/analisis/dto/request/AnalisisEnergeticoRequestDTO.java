package com.g9team30.energiai.domain.analisis.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

@Data
public class AnalisisEnergeticoRequestDTO {

    @JsonProperty("consumo_kwh")
    private Double consumoKwh;
    @JsonProperty("cantidad_personas")
    private Integer cantidadPersonas;
    @JsonProperty("cantidad_equipos")
    private Integer cantidadEquipos;
    @JsonProperty("temperatura_exterior")
    private Integer temperaturaExterior;
    @JsonProperty("uso_horario_pico")
    private Boolean usoHorarioPico;
}
