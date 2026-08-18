package com.g9team30.energiai.domain.common.validators;

import com.g9team30.energiai.domain.analisis.dto.request.AnalisisEnergeticoRequestDTO;
import org.springframework.stereotype.Component;

@Component
public class ValidarRequest {

    public void validateRequest(AnalisisEnergeticoRequestDTO requestDTO) {
        if (requestDTO == null) {
            throw new IllegalArgumentException("El request no puede ser nulo");
        }

        if (requestDTO.getConsumoKwh() == null || requestDTO.getConsumoKwh() <= 0) {
            throw new IllegalArgumentException("El consumo KWH debe ser mayor a 0");
        }

        if (requestDTO.getCantidadPersonas() == null || requestDTO.getCantidadPersonas() <= 0) {
            throw new IllegalArgumentException("La cantidad de personas debe ser mayor a 0");
        }

        if (requestDTO.getCantidadEquipos() == null || requestDTO.getCantidadEquipos() < 0) {
            throw new IllegalArgumentException("La cantidad de equipos no puede ser negativa");
        }

        if (requestDTO.getTemperaturaExterior() == null) {
            throw new IllegalArgumentException("La temperatura exterior es requerida");
        }

        if (requestDTO.getUsoHorarioPico() == null) {
            throw new IllegalArgumentException("El uso horario pico es requerido");
        }
    }
}
