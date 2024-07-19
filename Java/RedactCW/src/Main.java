
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
       System.out.println(redact("The quick brown fox jumps over the lazy dog123!", new String[]{"Fox", "jUmps", "doG","he","dog123","lazy"}));
    }

    /*public static String redact(String content, String[] redactWords) {
        char[] Raw = content.toCharArray();
        String UpperRaw = content.toUpperCase();
        int Iter = 0;
        for (String s : redactWords)
        {
            Iter = 0;
            for (char c : UpperRaw.toCharArray())
            {
                if(c == s.toUpperCase().toCharArray()[0])
                {
                    boolean temp = true;
                    for(int i = 0; i<s.length(); i++)
                    {
                        if(UpperRaw.toCharArray()[Iter + i] != s.toUpperCase().toCharArray()[i])
                        {
                            temp = false;
                            break;
                        }
                    }
                    if(temp)
                    {
                        for (int j = 0;j<s.length(); j++)
                        {
                            Raw[j+Iter] = '*';
                        }
                    }
                }
                Iter ++;

            }
        }
        String OutPut = "";
        for (char t : Raw)
        {
            OutPut +=t;
        }
        return OutPut;
    }*/

    public static String redact(String content, String[] redactWords) {
        String Raw = content;
        String[] SplitRaw = Raw.split(" ");


        for (String s :redactWords)
        {
            int Iter = 0;
            for (String k :SplitRaw)
            {
                String TempStage = "";
                for (String j : SplitGrammer(k))
                {
                    if(j.equalsIgnoreCase(s))
                    {
                        String Tmp = "";
                        for (char t : j.toCharArray())
                        {
                            Tmp += "*";
                        }

                        TempStage += Tmp;
                    }
                    else
                    {
                        TempStage += j;
                    }
                }
                SplitRaw[Iter] = TempStage;

                Iter ++;
            }
        }
        String OutPut = "";
        for (String s : SplitRaw)
        {
            OutPut+= s + " ";

        }
        return OutPut.trim();

    }

    public static String[] SplitGrammer(String s)
    {
        String[] OutPut = new String[s.length()];
        String temp = "";
        int ListLen = 0;

        for (char c : s.toCharArray())
        {
            if(!(((int) c <= 90 && (int) c>=65) || ((int) c <= 122 && (int) c >=97) || ((int) c <= 57 && (int) c >=48)))
            {
                if (temp != "")
                {
                    OutPut[ListLen] = temp;
                    ListLen++;
                }
                OutPut[ListLen] = String.valueOf(c);
                ListLen++;
                temp = "";
            }
            else
            {
                temp += c;
            }
        }

        if(temp != "")
        {
            OutPut[ListLen] = temp;
            ListLen++;
        }

        String[] TempOut = new String[ListLen];
        int Iter = 0;
        for (String k : OutPut)
        {
            if (k != null)
            {
                TempOut[Iter] = k;

            }
            else
            {
                break;
            }
            Iter ++;

        }
        for (String h : TempOut)
        {
            System.out.println(h);
        }
        System.out.println(" ");
        return TempOut;
    }
}