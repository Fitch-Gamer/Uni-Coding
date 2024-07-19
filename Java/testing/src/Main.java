import static java.lang.System.in;

public class Main {

    public static void main(String[] args) {

        String x = encode("AAAABBBCCDAA");
        System.out.println(x);
        System.out.println(decode(x));

    }

    private static String decode(String x) {
        String Out = "";
        char[] Input = x.toCharArray();
        int InLen = Input.length;
        for(int i=0; i<InLen/2;i++)
        {
            for (int j = 0; j< Integer.parseInt(String.valueOf(Input[(2*i)])); j++)
            {
                Out += Input[(2*i)+1];
            }
        }
        String FinalOut = "Input: " + x + " Output: " + Out;
        System.out.println(FinalOut);
        return Out;
    }

    private static String encode(String x) {
        char LastChar = ' ';
        int CurChars = 0;
        String Output = "";
        for(char c : x.toCharArray())
        {
            if(c == LastChar)
            {
                CurChars +=1;
            }
            else
            {
                if(CurChars != 0)
                {
                    Output += CurChars;
                    Output += LastChar;
                }

                LastChar = c;
                CurChars = 1;
            }
        }
        Output += CurChars;
        Output += LastChar;
        String FinalOut = "Input: " + x + " Output: " + Output;
        System.out.println(FinalOut);
        return Output;
    }


}