/**
 * Author: Bryson Parker
 * Class: ITCS 4102
 */

public class RetirementReport {
    // private fields, mostly assigned values from user input
    private int currentAge;
    private double currentIncome;
    private double totalCurrentSavings;
    private double avgAnnualExpenses;
    private final double retirementGoal = 1700000;
    private final double interest = .1;

    /**
     * Default constructor
     */
    public RetirementReport(){
        this(18, 40000, 0, 46000);
    }

    /**
     * Constructor which takes values
     * @param ageNow
     * @param currentSalary
     * @param currentSavings
     * @param avgExpenses
     */
    public RetirementReport(int ageNow, double currentSalary, double currentSavings, double avgExpenses){
        currentAge = ageNow;
        currentIncome = currentSalary;
        totalCurrentSavings = currentSavings;
        avgAnnualExpenses = avgExpenses;
    }

    /**
     * Calculates the retirement age as well as savings accumulated at the end of each year.
     * Places the savings in an array and the retirement age at the last index of the array.
     * @return double[]
     */
    public double[] calculateRetirement(){

        int time = 0;
        int retirementAge = currentAge;
        double retirement;
        double netIncome = currentIncome - avgAnnualExpenses;

        for(int i = 0; i < 100; i++){
            retirement = (totalCurrentSavings + netIncome * i) * (1 + .1 * i);
            if(retirement >= retirementGoal){
                time = i;
                break;
            }
        }

        retirementAge += time;


        double[] myGoals = new double[time + 1];

        for(int i = 0; i < myGoals.length - 1; i++){
            retirement = (totalCurrentSavings + netIncome * i) * (1 + .1 * i);
            myGoals[i] = retirement;
        }

        myGoals[time] = retirementAge;


        return myGoals;
    }


}
