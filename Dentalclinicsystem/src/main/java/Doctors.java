/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author OsamaAyman
 */
public class Doctors extends User {

    private String specialize;
    private String gender;

    public Doctors(String specialize, String gender, int id, String name, String phone, String address, String email, String username, String password) {
        super(id, name, phone, address, email, username, password);
        this.specialize = specialize;
        this.gender = gender;
    }
    
    
    public String getSpecialize() {
        return specialize;
    }

    public void setSpecialize(String specialize) {
        this.specialize = specialize;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    
    
}
