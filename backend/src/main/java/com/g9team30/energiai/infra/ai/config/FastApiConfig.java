package com.g9team30.energiai.infra.ai.config;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestClient;

@Configuration
public class FastApiConfig {



    @Bean
   public RestClient clientEnergiai(@Value("${fastapi.base-url}")String baseUrl){
       return  RestClient.builder()
               .baseUrl(baseUrl)
               .defaultHeader("Content-Type", "application/json")
               .build();


   }

}
