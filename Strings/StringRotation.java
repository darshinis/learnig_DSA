import java.util.*;
public class StringRotation {

    public static void rotate(char[] a, int arlength){
        char temp = a[0];
        int i = 0;
        for(i=0;i<arlength-1;i++){
            a[i] = a[i+1];
        }
        a[i] = temp;
        /* 
        for (int j=0;j<arlength;j++){
            System.out.print(a[j]);
        }
        System.out.println("");
        */
    }
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the how many times you want to rotate : ");
        int numRotations = input.nextInt();
        System.out.println("Enter the String you want to rotate : ");
        String inString = input.next();
        char inputString[] = inString.toCharArray();
        int strLength = inString.length();
        for (int i=0;i<numRotations;i++){
            rotate(inputString,strLength);

        }
        System.out.println("###################");
        for (int i=0;i<strLength;i++){
            System.out.print(inputString[i]);
        }

    }
}
