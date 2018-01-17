import java.util.*;
public class ChllengingFive {
    public static void main(String[] args) {
        int nums, sum;
        System.out.println("How many exam mark do you want to average?");
        nums = new Scanner(System.in).nextInt();
        sum = 0;
        int[] arr = new int[nums];

        for(int count = 0; count < nums; count++){
            System.out.println("Enter exam mark"+(count+1)+":");
            int temp = new Scanner(System.in).nextInt();
            sum += temp;
            arr[count] = temp;
        }
        System.out.println("The average is: "+(sum / nums));
        for(int z = 0; z < nums;z ++){
            System.out.print(arr[z]);
            for(int rep = 0;rep < arr[z];rep++){
                System.out.print("*");
            }
            System.out.println("");
        }
        System.out.println("The average is: "+(sum / nums));
    }
}
