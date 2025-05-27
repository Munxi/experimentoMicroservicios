package com.example.doctores.Models;


import jakarta.persistence.*;

@Entity
public class Doctor {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // Id por defecto auto generado

    private String nombre; // 
    private String ocupacion; // Restricción? en la noche

    // Constructores
    public Doctor() {}
    public Doctor(String nombre, String ocupacion) {
        this.nombre = nombre;
        this.ocupacion = ocupacion;
    }

    // Getters y setters
    public Long getId() { return id; }
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getOcupacion() { return ocupacion; }
    public void setOcupacion(String ocupacion) { this.ocupacion = ocupacion; }
}