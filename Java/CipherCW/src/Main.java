import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) {
        VigenereCipher test = new VigenereCipher();
        String Test = test.encrypt("C:\\Users\\fitch\\Desktop\\Uni-Coding\\Uni-Coding\\Java\\CipherCW\\src\\encrypt_check.txt","C:\\Users\\fitch\\Desktop\\Uni-Coding\\Uni-Coding\\Java\\CipherCW\\src\\key_check.txt");
        System.out.println(Test);
        System.out.println();
        System.out.println(test.decrypt("C:\\Users\\fitch\\Desktop\\Uni-Coding\\Uni-Coding\\Java\\CipherCW\\src\\decrypt_check.txt", "C:\\Users\\fitch\\Desktop\\Uni-Coding\\Uni-Coding\\Java\\CipherCW\\src\\key_check.txt"));
    }
    /**
     * Cipher interface for use with the CM10228: Principles of Programming 2 coursework.
     *
     * This should not be modified by the student.
     *
     * @author		Christopher Clarke
     * @version		1.0
     */
    public interface Cipher {

        /**
         * Encrypts a message using a key.
         *
         * @param  message_filename		the filename of the message to be encrypted
         * @param  key_filename			the filename of the key to be used to encrypt the message
         * @return       The encrypted message
         */
        public String encrypt(String message_filename, String key_filename);

        /**
         * Decrypts a message using a key.
         *
         * @param  message_filename		the filename of the message to be decrypted
         * @param  key_filename			the filename of the key to be used to decrypt the message
         * @return       The decrypted message
         */
        public String decrypt(String message_filename, String key_filename);
    }

    public static class VigenereCipher implements Cipher
    {
        public String encrypt(String message_filename, String key_filename)
        {

            char[][] VigenereSquare = GenVigSquare();
            String MessageRaw = ReadFile(message_filename);
            String KeyRaw = ReadFile(key_filename);
            int KeyIterator = 0;
            int KeyLen = KeyRaw.length();
            String OutPut = "";
            for (char c : MessageRaw.toUpperCase().toCharArray())
            {
                if((int)c>= 65 && (int)c <= 90)
                {
                    int testX = ((int) c) - 65;
                    int testY = (int) KeyRaw.toUpperCase().toCharArray()[KeyIterator%(KeyLen)]-65;
                    OutPut += VigenereSquare[testY][testX];
                    KeyIterator++;
                }
                else if((int)c != 13)
                {
                    OutPut += c;
                    KeyIterator++;
                }
                else
                {
                    OutPut += c;
                }


            }
            return OutPut;


        }
        public String decrypt(String message_filename, String key_filename)
        {
            char[][] VigenereSquare = GenVigSquare();
            String MessageRaw = ReadFile(message_filename);
            String KeyRaw = ReadFile(key_filename);
            int KeyIterator = 0;
            int KeyLen = KeyRaw.length();
            String OutPut = "";
            for (char c : MessageRaw.toUpperCase().toCharArray())
            {
                if((int)c>= 65 && (int)c <= 90)
                {
                    int testX = ((int) c) - 65;
                    int testY = (int) KeyRaw.toUpperCase().toCharArray()[KeyIterator%(KeyLen)]-65;
                    int DecryptIter = 0;
                    for(char k : VigenereSquare[testY])
                    {
                        if (k == c)
                        {
                            OutPut += (char) (DecryptIter + 65);
                            break;
                        }
                        DecryptIter++;
                    }
                    KeyIterator++;

                }
                else if((int)c != 13)
                {
                    OutPut += c;
                    KeyIterator++;
                }
                else
                {
                    OutPut += c;
                }

            }
            return OutPut;

        }

        private char[][] GenVigSquare(){
            char[][] OutPut = new char[26][26];
            for (int x = 0; x < 26; x++)
            {
                for(int y = 0; y< 26; y++)
                {
                    OutPut[x][y] = (char) (65 + ((x+y)%26));
                }
            }

            return OutPut;
        }

        public static String ReadFile(String FileName)
        {
            try {
                return Files.readString(Paths.get(FileName));
            } catch (IOException e) {
                throw new RuntimeException(e);
            }

        }
    }


}