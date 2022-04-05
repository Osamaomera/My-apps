/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author OsamaAyman
 */
public class Patient extends User { 
        
    private String gender;
    private String insurance;
    private String first_visit;
    private String last_visit;

    public Patient(String gender, String insurance, String first_visit, String last_visit, int id, String name, String phone, String address, String email, String username, String password) {
        super(id, name, phone, address, email, username, password);
        this.gender = gender;
        this.insurance = insurance;
        this.first_visit = first_visit;
        this.last_visit = last_visit;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getInsurance() {
        return insurance;
    }

    public void setInsurance(String insurance) {
        this.insurance = insurance;
    }

    public String getFirst_visit() {
        return first_visit;
    }

    public void setFirst_visit(String first_visit) {
        this.first_visit = first_visit;
    }

    public String getLast_visit() {
        return last_visit;
    }

    public void setLast_visit(String last_visit) {
        this.last_visit = last_visit;
    }

    
    
    
}
