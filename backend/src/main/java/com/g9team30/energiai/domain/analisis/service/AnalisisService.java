package com.g9team30.energiai.domain.analisis.service;

import com.g9team30.energiai.domain.analisis.dto.request.AnalisisEnergeticoRequestDTO;
import com.g9team30.energiai.domain.analisis.dto.response.AnalisisEnergeticoResponseDTO;
import com.g9team30.energiai.domain.common.validators.ValidarRequest;
import com.g9team30.energiai.infra.ai.client.FastApiClient;
import com.g9team30.energiai.infra.persistence.entity.AnalisisEnergetico;
import com.g9team30.energiai.infra.persistence.entity.Recomendacion;
import com.g9team30.energiai.infra.persistence.repository.AnalisisEnergeticoRepository;
import com.g9team30.energiai.infra.persistence.repository.RecomendacionRepository;
import jakarta.persistence.EntityNotFoundException;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
@Slf4j
public class AnalisisService {

    private final AnalisisEnergeticoRepository analisisEnergeticoRepository;
    private final RecomendacionRepository recomendacionRepository;
    private final FastApiClient fastApiClient;
    private final ValidarRequest validar;

    @Transactional
    public AnalisisEnergeticoResponseDTO createAnalysis(AnalisisEnergeticoRequestDTO request){

        validar.validateRequest(request);

        AnalisisEnergeticoResponseDTO fastApiResponse = fastApiClient.enviarAnalisis(request);
        AnalisisEnergetico analisis = convertToEntity(request, fastApiResponse);
        analisisEnergeticoRepository.save(analisis);
        var recomendaciones= fastApiResponse.getRecomendaciones()
                .stream()
                .map(a-> Recomendacion.builder()
                        .descripcion(a)
                        .analisis(analisis)
                        .build())
                .collect(Collectors.toList());

        recomendacionRepository.saveAll(recomendaciones);

        var descripcionesRecomendaciones = recomendaciones.stream()
                .map(r->r.getDescripcion())
                .collect(Collectors.toList());


        return convertToResponseDTO(analisis,descripcionesRecomendaciones);
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
                .ahorroPotencialMensual(analisisEnergeticoResponse.getAhorroPotencialMensual())
                .ahorroPotencialAnual(analisisEnergeticoResponse.getAhorroPotencialAnual())
                .fechaAnalisis(LocalDateTime.now())
                .build();
    }

    private void handleFastApiError(Exception e) {
        log.error("Error al procesar con FastAPI: {}", e.getMessage());
        throw new RuntimeException("Error en el análisis energético: " + e.getMessage(), e);
    }

    public AnalisisEnergeticoResponseDTO getAnalysisById(Integer id) {
      var optionalAnalisis =  analisisEnergeticoRepository.findById(id);
      if (optionalAnalisis.isPresent()){
          var analisis= optionalAnalisis.get();
         var recomendacionReferenceAnalisis= recomendacionRepository.findByAnalisisId(analisis.getId())
                  .stream()
                  .map(r->r.getDescripcion())
                  .collect(Collectors.toList());
          return convertToResponseDTO(analisis, recomendacionReferenceAnalisis);

      }
        throw new EntityNotFoundException();
    }

    private AnalisisEnergeticoResponseDTO convertToResponseDTO(AnalisisEnergetico analisis,
                                                               List<String> recomendaciones){
        return AnalisisEnergeticoResponseDTO.builder()
                .id(analisis.getId())
                .categoria(analisis.getCategoria())
                .probabilidad(analisis.getProbabilidad())
                .costoEstimadoMensual(analisis.getCostoEstimadoMensual())
                .ahorroPotencialMensual(analisis.getAhorroPotencialMensual())
                .ahorroPotencialAnual(analisis.getAhorroPotencialAnual())
                .recomendaciones(recomendaciones)
                .build();
    }

    public List<AnalisisEnergeticoResponseDTO> getAnalisisListUserId (Integer usuarioId){
        var analisisList= analisisEnergeticoRepository.findByUsuarioId(usuarioId);

        return analisisList.stream()
                .map(analisis -> {
                    var recomendaciones = recomendacionRepository.findByAnalisisId(analisis.getId())
                            .stream()
                            .map(Recomendacion::getDescripcion)
                            .collect(Collectors.toList());
                    return convertToResponseDTO(analisis, recomendaciones);
                })
                .collect(Collectors.toList());
    }
}
