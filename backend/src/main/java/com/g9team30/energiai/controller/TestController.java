package com.g9team30.energiai.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/test")
public class TestController {

    @Value("${mensaje}")
    private String mensaje;

    @GetMapping("/perfil")
    public String perfil(){
        return mensaje;
    }

    @GetMapping("/swagger")
    public String doc(){
        return "Api funcionando en Swagger";
    }

    @GetMapping("/error")
    public String error(){
        throw new RuntimeException("error de prueba API");
    }



}
