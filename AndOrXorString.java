import java.util.Scanner;

public class AndOrXorString {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String str = scanner.nextLine();

        System.out.println("Original String: " + str);

        // AND each character with 127
        char[] andCharArray = str.toCharArray();
        for (int i = 0; i < andCharArray.length; i++) {
            andCharArray[i] = (char) (andCharArray[i] & 127);
        }
        String andResult = new String(andCharArray);
        System.out.println("AND Result: " + andResult);

        // OR each character with 127
        char[] orCharArray = str.toCharArray();
        for (int i = 0; i < orCharArray.length; i++) {
            orCharArray[i] = (char) (orCharArray[i] | 127);
        }
        String orResult = new String(orCharArray);
        System.out.println("OR Result: " + orResult);

        // XOR each character with 127
        char[] xorCharArray = str.toCharArray();
        for (int i = 0; i < xorCharArray.length; i++) {
            xorCharArray[i] = (char) (xorCharArray[i] ^ 127);
        }
        String xorResult = new String(xorCharArray);
        System.out.println("XOR Result: " + xorResult);
    }
}
