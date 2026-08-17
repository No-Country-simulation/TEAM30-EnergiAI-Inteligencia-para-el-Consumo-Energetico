package com.g9team30.energiai.domain.analisis.service;

import com.g9team30.energiai.domain.analisis.dto.request.AnalisisEnergeticoRequestDTO;
import com.g9team30.energiai.domain.analisis.dto.response.AnalisisEnergeticoResponseDTO;
import com.g9team30.energiai.domain.common.validators.ValidarRequest;
import com.g9team30.energiai.infra.ai.client.FastApiClient;
import com.g9team30.energiai.infra.persistence.entity.AnalisisEnergetico;
import com.g9team30.energiai.infra.persistence.repository.AnalisisEnergeticoRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;

@Service
@RequiredArgsConstructor
@Slf4j
public class AnalisisService {

    private final AnalisisEnergeticoRepository analisisEnergeticoRepository;
    private final FastApiClient fastApiClient;
    private final ValidarRequest validar;

    @Transactional
    public AnalisisEnergeticoResponseDTO createAnalysis(AnalisisEnergeticoRequestDTO request){

        validar.validateRequest(request);

        AnalisisEnergeticoResponseDTO fastApiResponse = fastApiClient.enviarAnalisis(request);
        AnalisisEnergetico analisis = convertToEntity(request, fastApiResponse);
        analisisEnergeticoRepository.save(analisis);

        return fastApiResponse;
    }

    private AnalisisEnergetico convertToEntity(AnalisisEnergeticoRequestDTO request,
                                               AnalisisEnergeticoResponseDTO analisisEnergeticoResponse) {

        return AnalisisEnergetico.builder()

                .usuarioId(request.getUsuarioId())
                .consumoKwh(request.getConsumoKwh())
                .usoHorarioPico(request.getUsoHorarioPico())
                .cantidadPersonas(request.getCantidadPersonas())
                .cantidadEquipos(request.getCantidadEquipos())
                .temperaturaExterior(request.getTemperaturaExterior())
                .categoria(analisisEnergeticoResponse.getCategoria())
                .probabilidad(analisisEnergeticoResponse.getProbabilidad())
                .costoEstimadoMensual(analisisEnergeticoResponse.getCostoEstimadoMensual())
                .fechaAnalisis(LocalDateTime.now())
                .build();
    }

    private void handleFastApiError(Exception e) {
        log.error("Error al procesar con FastAPI: {}", e.getMessage());
        throw new RuntimeException("Error en el análisis energético: " + e.getMessage(), e);
    }
}
