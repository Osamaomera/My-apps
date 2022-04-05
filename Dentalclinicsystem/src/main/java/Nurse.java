/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author OsamaAyman
 */
public class Nurse extends User {

    private String shift_time;
    private String gender;

    public Nurse(String shift_time, String gender, int id, String name, String phone, String address, String email, String username, String password) {
        super(id, name, phone, address, email, username, password);
        this.shift_time = shift_time;
        this.gender = gender;
    }


    public String getShift_time() {
        return shift_time;
    }

    public void setShift_time(String shift_time) {
        this.shift_time = shift_time;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    
    
    
    
}
