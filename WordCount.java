import java.util.Scanner;
class WordCount{
    public static void main(String args[]){
        System.out.println("hello hai");
        Scanner input = new Scanner(System.in);
        String st = input.nextLine();
        int count = 0;
        System.out.println(st);
        System.out.println("###################");
        for (String x : st.split(" ")){
                count ++;
                System.out.println(x);
        }
        System.out.println("No of words = "+count);
    }
}