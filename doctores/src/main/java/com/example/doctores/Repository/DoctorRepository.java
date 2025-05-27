package com.example.doctores.Repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.doctores.Models.Doctor;

public interface DoctorRepository extends JpaRepository<Doctor, Long> {}
