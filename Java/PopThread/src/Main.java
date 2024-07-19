import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Arrays;


public class Main {
    public static void main(String[] args) {


        ArrayList<String> filesOne = new ArrayList<>();
        filesOne.add("C:\\Users\\fitch\\Desktop\\Uni-Coding\\Uni-Coding\\Java\\PopThread\\src\\1831-06-01.txt");
        filesOne.add("C:\\Users\\fitch\\Desktop\\Uni-Coding\\Uni-Coding\\Java\\PopThread\\src\\2003-08-27.txt");

        ArrayList<String> filesTwo = new ArrayList<>();
        filesTwo.add("C:\\Users\\fitch\\Desktop\\Uni-Coding\\Uni-Coding\\Java\\PopThread\\src\\1961-04-12.txt");
        filesTwo.add("C:\\Users\\fitch\\Desktop\\Uni-Coding\\Uni-Coding\\Java\\PopThread\\src\\1972-12-11.txt");

        int numAttempts = 3;

        for(int i = 0; i < numAttempts; i++) {
            System.out.println("Run: " + (i+1));
            PopThread popRunnableOne = new PopThread(filesOne);
            PopThread popRunnableTwo = new PopThread(filesTwo);
            Thread threadOne = new Thread(popRunnableOne);
            Thread threadTwo = new Thread(popRunnableTwo);
            threadOne.start();
            threadTwo.start();
            try {
                threadOne.join();
                threadTwo.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }


    public static class PopThread implements Runnable
    {
        //public static int NumThreads = 0;
        //public static int PriorThreads = -1;
        private String[] args = null;
        public static int CurPage = 1;
        public PopThread(ArrayList<String> s)
        {

            CreateClear("result.txt");
            args = s.toArray(new String[0]);
            /*
            NumThreads++;
            if(PriorThreads<0)
            {
                PriorThreads = Thread.activeCount();
            }
             */
            CurPage = 1;

        }

        @java.lang.Override
        public void run() {
            /*
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }

            while((Thread.activeCount() - PriorThreads) != NumThreads){}
            try {
                Thread.sleep(3); // gives time for all the threads to finish the while loop before changing variables, set to 3 for safety but works with 1
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }


            NumThreads = 0;
            PriorThreads = -1;

             */

            String[][] tmp = new String[args.length][3];
            int iter = 0;

            for (String s : args)
            {
                tmp[iter][1] = s;
                tmp[iter][2] = ReadFile(s);
                tmp[iter][0] = GetLoc(tmp[iter][2]);
                iter++;
            }
            tmp = SortArrArr(tmp);
            int LastDelay = 0;
            for(String[] s : tmp)
            {
                /*try {
                    Thread.sleep((Long.parseLong((s[0]))-LastDelay)*3); // works without the multiplier but this adds safety

                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
                LastDelay = Integer.parseInt(s[0]);
                WriteFile("result.txt",s[2]);

                */
                while (true)
                {
                    if(Integer.parseInt(s[0]) == CurPage)
                    {
                        WriteFile("result.txt",s[2]);
                        CurPage++;
                        break;
                    }
                }

            }



        }


        private String[][] SortArrArr(String[][] s)
        {
            int[] tmp= new int[s.length];
            String[][] OutPut= new String[s.length][2];
            int iter = 0;
            for (String[] t : s)
            {
                tmp[iter] = Integer.parseInt(s[iter][0]);
                iter++;
            }
            Arrays.sort(tmp);
            iter = 0;
            for(int t : tmp)
            {

                for (String[] x : s)
                {
                    if(t == Integer.parseInt(x[0]))
                    {
                        OutPut[iter] = x;
                    }

                }

                iter++;
            }

            return OutPut;
        }
        private String GetLoc(String s)
        {
            return s.substring(s.length() -8 ,s.length()-5);
        }

        private void CreateClear(String FileName)
        {
            try {
                Path path= Path.of(FileName);
                Files.deleteIfExists(path);
                Files.write(path, "".getBytes(StandardCharsets.UTF_8), StandardOpenOption.CREATE);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        private void WriteFile(String FileName,String Input)
        {
            try {
                Files.writeString(Path.of(FileName), Input, StandardOpenOption.APPEND);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }

        }
        private String ReadFile(String FileName)
        {
            try {
                return Files.readString(Paths.get(FileName));
            } catch (IOException e) {
                throw new RuntimeException(e);
            }

        }
    }
}