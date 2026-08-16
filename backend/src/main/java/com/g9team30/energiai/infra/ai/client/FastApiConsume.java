package com.g9team30.energiai.infra.ai.client;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.web.client.RestClient;

@Configuration
public class FastApiConsume {

    @Bean
   public RestClient clientEnergiai(){
       return  RestClient.builder()
               .baseUrl("https://.com")
               .defaultHeader("Content-Type", "application/json")
               .build();

   }






}
