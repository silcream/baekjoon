package b2475;

import java.io.IOException;
import java.util.Scanner;

public class b2475 {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        int sum = 0;
        for (int i = 0; i<5; i++){
            int temp = sc.nextInt();
            sum += temp * temp;
        }
        int result = sum % 10;
        System.out.println(result);
    }
}

