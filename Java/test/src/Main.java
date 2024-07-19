import java.io.IOException;
import java.time.LocalDateTime;

public class Main {
    public static void main(String[] args) {
        int lastsec = -1;
        String SecZero = "";
        String MinZero = "";
        String HourZero = "";
        while(true){

            var NowTime = LocalDateTime.now();
            if (NowTime.getSecond() != lastsec){
                ClearConsole();
                if (NowTime.getSecond()<10)
                {
                    SecZero = "0";
                }
                else
                {
                    SecZero = "";
                }
                if (NowTime.getMinute()<10)
                {
                    MinZero = "0";
                }
                else
                {
                    MinZero = "";
                }
                if (NowTime.getHour()<10)
                {
                    HourZero = "0";
                }
                else
                {
                    HourZero = "";
                }
                System.out.println(HourZero + NowTime.getHour() + ":" + MinZero + NowTime.getMinute() + ":" + SecZero + NowTime.getSecond());
                lastsec = NowTime.getSecond();
            }

        }
    }

    public static void ClearConsole()
    {
        /*
        try
        {
            final String os = System.getProperty("os.name");
            if (os.contains("Windows"))
            {
                Runtime.getRuntime().exec("cls");
            }
        }
        catch (final Exception e)
        {
            e.printStackTrace();
        }

         */
        /*
        for (int i = 0; i<50; i++)
        {
            System.out.println("");
        }
        */
        //System.out.print("\033[H\033[2J");
        //System.out.flush();
    }
}