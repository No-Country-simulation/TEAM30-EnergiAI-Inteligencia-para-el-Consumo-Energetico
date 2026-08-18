package com.g9team30.energiai.controller;

import com.g9team30.energiai.domain.analisis.dto.request.TestRequest;
import jakarta.persistence.EntityNotFoundException;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.web.bind.annotation.*;


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

    // Para probar EntityNotFoundException (404)
    @GetMapping("/not-found")
    public ResponseEntity<?> testNotFound() {
        throw new EntityNotFoundException("Recurso no encontrado");
    }

    // Para probar MethodArgumentNotValidException (400)
    @PostMapping("/validation")
    public ResponseEntity<?> testValidation(@Valid @RequestBody TestRequest request) {
        return ResponseEntity.ok("Validación exitosa");
    }

    // Para probar HttpMessageNotReadableException (400)
    @PostMapping("/not-readable")
    public ResponseEntity<?> testNotReadable(@RequestBody TestRequest request) {
        return ResponseEntity.ok("Body correcto");
    }

    // Para probar AccessDeniedException (403)
    @GetMapping("/access-denied")
    public ResponseEntity<?> testAccessDenied() {
        throw new AccessDeniedException("Acceso denegado");
    }


}
