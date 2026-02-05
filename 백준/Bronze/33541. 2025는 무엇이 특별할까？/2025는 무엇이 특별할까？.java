import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String str = br.readLine(); 
        int x = Integer.parseInt(str);
        int i;

        for(i=x+1 ; i < 10000; i++){
            String num = String.valueOf(i);
            int a = Integer.parseInt(num.substring(0, 2));
            int b = Integer.parseInt(num.substring(2));

            if( (a+b)*(a+b) == i){
                sb.append(i);
                break;
            }
        }
        if (i==10000)
            sb.append(-1);

        System.out.println(sb);
    }
}