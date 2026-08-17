package com.g9team30.energiai.controller;

import com.g9team30.energiai.domain.analisis.dto.request.AnalisisEnergeticoRequestDTO;
import com.g9team30.energiai.domain.analisis.dto.response.AnalisisEnergeticoResponseDTO;
import com.g9team30.energiai.domain.analisis.service.AnalisisService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Validated
@RestController
@RequestMapping("/analisis")
@RequiredArgsConstructor
public class AnalisisController {

    private final AnalisisService analisisService;

    @PostMapping
    public ResponseEntity<AnalisisEnergeticoResponseDTO> createAnalysis(
            @Valid @RequestBody AnalisisEnergeticoRequestDTO request) {

        return ResponseEntity.ok(
                analisisService.createAnalysis(request)
        );
    }

    /*
    @GetMapping("/{id}")
    public ResponseEntity<AnalisisEnergeticoResponseDTO> getAnalysisById(
            @PathVariable Integer id) {

        return ResponseEntity.ok(
                analisisService.getAnalysisById(id)
        );
    }

    @GetMapping
    public ResponseEntity<List<AnalisisEnergeticoResponseDTO>> getAllAnalysis(
            @RequestParam Integer usuarioId) {

        return ResponseEntity.ok(
                analisisService.getAllAnalysis(usuarioId)
        );
    }
    */
}