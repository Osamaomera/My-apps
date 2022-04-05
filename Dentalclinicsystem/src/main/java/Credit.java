/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author OsamaAyman
 */
public class Credit extends Payment {
    
    private int visa_num;
    private int visa_pass;

    public Credit(int visa_num, int visa_pass, float amount) {
        super(amount);
        this.visa_num = visa_num;
        this.visa_pass = visa_pass;
    }

    public int getVisa_num() {
        return visa_num;
    }

    public void setVisa_num(int visa_num) {
        this.visa_num = visa_num;
    }

    public int getVisa_pass() {
        return visa_pass;
    }

    public void setVisa_pass(int visa_pass) {
        this.visa_pass = visa_pass;
    }

    
    
    
}
