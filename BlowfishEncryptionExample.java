import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.security.Key;
import java.security.KeyStore;
import java.security.SecureRandom;
import java.io.FileInputStream;

public class BlowfishEncryptionExample {

    public static void main(String[] args) throws Exception {
        // Load the keystore
        KeyStore keystore = KeyStore.getInstance("JCEKS");
        FileInputStream fis = new FileInputStream("blowfish.keystore");
        keystore.load(fis, "password".toCharArray());
        fis.close();

        // Get the Blowfish key from the keystore
        Key key = keystore.getKey("blowfishkey", "password".toCharArray());

        // Encrypt the text "Hello world"
        String plaintext = "Hello world";
        byte[] ciphertext = encrypt(plaintext, key);

        // Print the ciphertext
        System.out.println("Ciphertext: " + bytesToHex(ciphertext));
    }

    public static byte[] encrypt(String plaintext, Key key) throws Exception {
        Cipher cipher = Cipher.getInstance("Blowfish");
        cipher.init(Cipher.ENCRYPT_MODE, key);
        return cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));
    }

    public static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02X", b));
        }
        return sb.toString();
    }
}
