import java.nio.charset.Charset;
import java.util.*;
public class StringCreation {
    public static void main(String args[]){
        //string literal way of creating string
        //static memory allocation will happen in STACK
        String sample = "welcome to starting java programme";
        System.out.println(sample);

        // when ever we use new keyword it is dynamic memory allocation
        //string will be stored in HEAP memory
        String sample1 = new String("hello java");
        System.out.println(sample1);

        byte byt[] = {66,67,68,69};
        Charset cs = Charset.defaultCharset();
        String sample2 = new String(byt,cs);

        //String sample2_1 = new String(byt,"US-ASCII");
        //System.out.println(sample2_1);

        System.out.println(sample2);

        String sample3 = new String (byt,1,2);
        System.out.println(sample3);

        

        
    }
}
