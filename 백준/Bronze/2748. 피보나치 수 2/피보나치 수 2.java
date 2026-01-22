import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        
        if (n == 0) {
            System.out.print(0);
            return;
        } else if (n == 1) {
            System.out.print(1);
            return;
        }
        
        long[] arr = new long[n+1];
        arr[0] = 0;
        arr[1] = 1;
        for(int i = 2; i<=n; i++){
            arr[i] = arr[i-1] + arr[i-2];
        }
        System.out.print(arr[n]);
    }
}