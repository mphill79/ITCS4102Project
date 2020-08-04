/**
 * Author: Bryson Parker
 * Class: ITCS 4102
 */

import java.util.*;

public class Retirement {
    public static void main(String[] args){

        // code for testing with manual input from console
        Scanner input = new Scanner(System.in);

        /**
        System.out.println("Enter Age: ");
        int ageNow = input.nextInt();
        System.out.println("Enter current salary: ");
        double currentSalary = input.nextDouble();
        System.out.println("Enter current savings: ");
        double currentSavings = input.nextDouble();
        System.out.println("Enter average annual expenses: ");
        double avgExpenses = input.nextDouble();
        */
        // code for taking user input from the GUI


        int ageNow = Integer.parseInt(args[0]);
        double currentSalary =  Double.parseDouble(args[1]);
        double currentSavings = Double.parseDouble(args[2]);
        double avgExpenses = Double.parseDouble(args[3]);


        double[] goals;

        RetirementReport myRetirement = new RetirementReport(ageNow, currentSalary, currentSavings, avgExpenses);

        goals = myRetirement.calculateRetirement();

        for(double i : goals){
            System.out.print(String.format("%.2f", i) + " ");
        }

    }
}
