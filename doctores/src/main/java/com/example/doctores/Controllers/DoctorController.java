package com.example.doctores.Controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.doctores.Models.Doctor;
import com.example.doctores.Repository.DoctorRepository;

@RestController
@RequestMapping("/doctores")
public class DoctorController {

    @Autowired
    private DoctorRepository doctorRepository;

    @GetMapping
    public List<Doctor> obtenerDoctores() {
        return doctorRepository.findAll();
    }

    @PostMapping
    public Doctor crearDoctor(@RequestBody Doctor doctor) {
        return doctorRepository.save(doctor);
    }
}