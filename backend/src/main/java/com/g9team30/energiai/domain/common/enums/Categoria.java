package com.g9team30.energiai.domain.common.enums;

import com.fasterxml.jackson.annotation.JsonCreator;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

import java.util.Arrays;

@Getter
@RequiredArgsConstructor
public enum Categoria {
    EFICIENTE,
    MODERADO,
    INEFICIENTE;

    @JsonCreator
    public static Categoria fromString(String value) {
        return Categoria.valueOf(value.toUpperCase());

    }

}


