package BRONZE;
import java.util.Scanner;

public class BigNum {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String inputNum = sc.next();
        Integer num = Integer.valueOf(inputNum);
        Integer answer = num / 20000303;
        System.out.println(answer);
    }
}
