package com.g9team30.energiai.domain.analisis.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;
import lombok.Data;

@Data
public class AnalisisEnergeticoRequestDTO {

    @JsonProperty("usuario_id")
    @NotNull
    @Positive
    private Integer usuarioId;

    @JsonProperty("consumo_kwh")
    @NotNull
    @Positive
    private Double consumoKwh;

    @JsonProperty("cantidad_personas")
    @NotNull
    @Positive
    private Integer cantidadPersonas;

    @JsonProperty("cantidad_equipos")
    @NotNull
    @Positive
    private Integer cantidadEquipos;

    @JsonProperty("temperatura_exterior")
    @NotNull
    private Float temperaturaExterior;

    @JsonProperty("uso_horario_pico")
    @NotNull
    private Boolean usoHorarioPico;
}