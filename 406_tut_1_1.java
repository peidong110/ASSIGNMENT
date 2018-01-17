import java.util.*;
public class TaxProgram {
    public static void main(String[] args) {
        double income, fedTax, provTax;
        int dependents;

        System.out.print("Please enter your taxable income: ");
        income = new Scanner(System.in).nextDouble();


        if (income == 59180. || income >59180.0){
            fedTax = 0.17 * 29590.0 + 0.26 *29590.0 + (0.29 * (income - 59180.0));
            System.out.println(fedTax);
        }
        else if(income <59179.99 || income > 29590.01){
            fedTax = 0.17 * 29590.0 + 0.26 * (income - 29590.0);
            System.out.println(String.format("%1.2f",fedTax));

        }
        else{
            fedTax = 0.17 * income;
            System.out.println((int)(fedTax));

        }
    }

    }
