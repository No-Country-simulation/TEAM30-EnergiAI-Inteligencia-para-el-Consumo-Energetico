package com.g9team30.energiai.infra.ai.client;


import com.g9team30.energiai.domain.analisis.dto.request.AnalisisEnergeticoRequestDTO;
import com.g9team30.energiai.domain.analisis.dto.response.AnalisisEnergeticoResponseDTO;
import com.g9team30.energiai.domain.analisis.port.FastClientPort;
import com.g9team30.energiai.infra.ai.client.exception.FastCommunicationException;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatusCode;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClient;
import org.springframework.web.client.RestClientException;

@Component
@RequiredArgsConstructor
public class FastApiClient implements FastClientPort {

    private final RestClient restClient;

    @Override
    public AnalisisEnergeticoResponseDTO enviarAnalisis(AnalisisEnergeticoRequestDTO analisisRequest){

        try {
            return restClient.post()
                    .uri("/analisis-energetico")
                    .body(analisisRequest)
                    .retrieve()
                    .onStatus(HttpStatusCode::is4xxClientError, (request, response) -> {

                        throw new FastCommunicationException(
                                "Error de validación de Api de Datos: " + response.getStatusCode());
                    })
                    .onStatus(HttpStatusCode::is5xxServerError, (request, response) -> {

                        throw new FastCommunicationException(
                                "Error interno en API de datos: " + response.getStatusCode());
                    })
                    .body(AnalisisEnergeticoResponseDTO.class);

        } catch (RestClientException e) {

            throw new FastCommunicationException(
                    "No se pudo establecer comunicación con FastAPI", e);
        }




    }

}
