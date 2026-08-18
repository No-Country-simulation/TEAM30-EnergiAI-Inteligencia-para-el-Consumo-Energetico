package com.g9team30.energiai.domain.analisis.port;

import com.g9team30.energiai.domain.analisis.dto.request.AnalisisEnergeticoRequestDTO;
import com.g9team30.energiai.domain.analisis.dto.response.AnalisisEnergeticoResponseDTO;

public interface FastClientPort {

    AnalisisEnergeticoResponseDTO enviarAnalisis (AnalisisEnergeticoRequestDTO analisisRequest);
}
