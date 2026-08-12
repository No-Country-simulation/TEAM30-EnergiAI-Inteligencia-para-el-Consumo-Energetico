package com.g9team30.energiai.domain.analisis.model;

import com.g9team30.energiai.domain.common.enums.Categoria;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Entity
@Table(name = "analisis_energetico")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class AnalisisEnergetico {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(name = "consumo_kwh")
    private Double consumoKwh;
    @Column(name = "uso_horario_pico")
    private Boolean usoHorarioPico;
    @Column(name = "cantidad_personas")
    private Integer cantidadPersonas;
    @Column(name = "cantidad_equipos")
    private Integer cantidadEquipos;
    @Enumerated(EnumType.STRING)
    @Column(name = "categoria")
    private Categoria categoria;
    @Column(name = "probabilidad")
    private Double probabilidad;
    @Column(name = "costo_estimado_mensual")
    private Double costoEstimadoMensual;
    @Column(name = "fecha_analisis")
    private LocalDateTime fechaAnalisis;
    @Column(name = "temperatura_exterior")
    private Float temperaturaExterior;
}
