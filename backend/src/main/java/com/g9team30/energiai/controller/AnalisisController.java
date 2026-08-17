package com.g9team30.energiai.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

@Validated
@RestController
@RequestMapping("/analisis")
@RequiredArgsConstructor
public class AnalisisController {

    @PostMapping
    public void createAnalysis() {
        // TODO: conectar con el Service
    }

    @GetMapping("/{id}")
    public void getAnalysisById(@PathVariable Integer id) {
        // TODO: conectar con el Service
    }

    @GetMapping
    public void getAllAnalysis() {
        // TODO: conectar con el Service
    }
}