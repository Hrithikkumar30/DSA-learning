public class MainOverload {
    public static void main(String args[])
    {
        main (2);
        System.out.println (main ("Cloud") + " - " + main ("Rain")); 
        main (4);
    }
    
    public static void main(Integer intvalue)
    {
        int total = intvalue++ - --intvalue + ++intvalue
        System.out.println("Total: " + total);
    }
    
    public static String main(String args)
    {
        return (10 *5 + args + 10 / 5);
    }
    }
