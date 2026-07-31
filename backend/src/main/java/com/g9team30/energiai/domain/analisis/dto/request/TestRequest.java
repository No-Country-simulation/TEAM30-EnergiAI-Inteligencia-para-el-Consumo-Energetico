package com.g9team30.energiai.domain.analisis.dto.request;

import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import lombok.Data;

@Data
public class TestRequest {
    @NotBlank(message = "El nombre no puede estar vacío")
    @Size(min = 3, max = 20, message = "El nombre debe tener entre 3 y 20 caracteres")
    private String nombre;

    @Min(value = 18, message = "La edad debe ser mayor o igual a 18")
    @Max(value = 100, message = "La edad debe ser menor o igual a 100")
    private Integer edad;
}