import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int[] arr = new int[N];
        for(int i = 0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        for(int M : arr){
            if(M == 300){
                sb.append("1");
            }
            else if(275<=M){
                sb.append("2");
            }
            else if(250<=M){
                sb.append("3");
            }
            else{
                sb.append("4");
            }
            sb.append(" ");
        }
        
        System.out.print(sb);
    }
}