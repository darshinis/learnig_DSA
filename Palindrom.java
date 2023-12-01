import java.util.*;
public class Palindrom {
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        String inputString = input.next();
        int inputStringLength = inputString.length();
        char a[] = inputString.toCharArray();
        int j=inputStringLength-1;
        System.out.println("inputStringLength : "+inputStringLength/2);
        for(int i=0;i<inputStringLength/2;i++){
            //System.out.print(a[i]+" "+a[j]);
            if(a[i]!=a[j]){
                System.out.println("Not Palindrom");
                //System.out.print(a[i]+" "+a[j]);
                return ;
            }
            j--;
            //System.out.println();
        }
        System.out.println("Palindrom");
    }
    
}
