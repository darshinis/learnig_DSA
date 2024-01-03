import java.util.*;
public class StringMethods {
    public static void main(String args[]){
        StringBuffer sb = new StringBuffer("Hello how are you");
        String sample4 = new String (sb);

        System.out.println(sample4);

        //different methods in strings
        System.out.println("length of "+sample4+" is : "+sample4.length());
        System.out.println("character 5th index of "+sample4+" string is : "+sample4.charAt(5));
        System.out.println("index of 'o' in "+sample4+" string is : "+sample4.indexOf('o'));
        System.out.println("index of 'o' in "+sample4+" string from 11 - 16 indexes is : "+sample4.indexOf('o',11,16));
        System.out.println("last index of 'o' in "+sample4+" string is : "+sample4.lastIndexOf('o'));

        String s1 = "Hello";
        String s2 = "hello";

        System.out.println(s1.equals(s2));
        System.out.println(s1.equalsIgnoreCase(s2));

        System.out.println(s1.compareTo(s2));
        System.out.println(s1.compareToIgnoreCase(s2));

        String capital_string = new String("capital : hello how are you ?".toUpperCase());
        System.out.println(capital_string);
        System.out.println("LOWER : "+capital_string.toLowerCase());

        System.out.println("TRIM : hello how are you ?  ".trim());

        System.out.println("REPLACE (a with x) :"+" apples are acidic fruits, so dont take it first in the morning".replace('a','x'));
        String str_literal = "hello how are you";
        char arr [] = str_literal.toCharArray();
        System.out.println(arr);
        for (int i=0;i<str_literal.length();i++){
            System.out.println(arr[i]);
        }
    }
}
