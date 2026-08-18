package com.g9team30.energiai.infra.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class OpenApiConfig {

    @Bean
    public OpenAPI energiaiOpenAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("EnergiAI API")
                        .description("API para análisis inteligente del consumo energético.")
                        .version("1.0.0"));
    }
}