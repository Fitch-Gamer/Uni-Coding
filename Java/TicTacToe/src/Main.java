import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Objects;

public class Main {
    public static JFrame frame = new JFrame("TicTacToe");
    public static JButton[][] Board = new JButton [3][3];
    public static boolean Xturn = true;
    public static void main(String[] args){


        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800,800);
        frame.setLayout(null);


        for (int x = 0;x<3;x++)
        {
            for (int y = 0; y < 3; y ++)
            {
                Board[x][y] = CreateButton("",50+(250*x),50 + (250*y),200,200);//,ButPress(Board[x][y]));
                Board[x][y].addActionListener(ButPress(Board[x][y]));
                frame.getContentPane().add(Board[x][y]);
            }
        }


        frame.update(frame.getGraphics());
        frame.setVisible(true);
    }
    public static ActionListener ButPress(JButton b){
        return new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (Xturn)
                {
                    b.setText("X");
                }
                else
                {
                    b.setText("O");
                }
                b.setEnabled(false);
                Xturn = !Xturn;
                b.setFont(new Font(Font.DIALOG,Font.PLAIN,100));

                CheckWin();
            }
        };

    }

    private static void CheckWin() {
        for (JButton[] Column : Board)
        {
            if(Objects.equals(Column[0].getText(), Column[1].getText()) && Objects.equals(Column[2].getText(), Column[1].getText()))
            {
                if (Objects.equals(Column[0].getText(), "X"))
                {
                    JOptionPane.showMessageDialog(frame, "X wins");
                    ResetFrame();
                }
                else if(Objects.equals(Column[0].getText(), "O"))
                {
                    JOptionPane.showMessageDialog(frame, "O wins");
                    ResetFrame();
                }

            }
        }
        for (int i = 0; i<3; i++)
        {
            if(Objects.equals(Board[0][i].getText(), Board[1][i].getText()) && Objects.equals(Board[2][i].getText(), Board[1][i].getText()))
            {
                if (Objects.equals(Board[0][i].getText(), "X"))
                {
                    JOptionPane.showMessageDialog(frame, "X wins");
                    ResetFrame();
                }
                else if(Objects.equals(Board[0][i].getText(), "O"))
                {
                    JOptionPane.showMessageDialog(frame, "O wins");
                    ResetFrame();
                }

            }
        }

        if(Objects.equals(Board[0][0].getText(), Board[1][1].getText()) && Objects.equals(Board[2][2].getText(), Board[1][1].getText())) {
            if (Objects.equals(Board[0][0].getText(), "X")) {
                JOptionPane.showMessageDialog(frame, "X wins");
                ResetFrame();
            } else if (Objects.equals(Board[0][0].getText(), "O")) {
                JOptionPane.showMessageDialog(frame, "O wins");
                ResetFrame();
            }
        }

        if(Objects.equals(Board[0][2].getText(), Board[1][1].getText()) && Objects.equals(Board[2][0].getText(), Board[1][1].getText())) {
            if (Objects.equals(Board[0][2].getText(), "X")) {
                JOptionPane.showMessageDialog(frame, "X wins");
                ResetFrame();
            } else if (Objects.equals(Board[0][2].getText(), "O")) {
                JOptionPane.showMessageDialog(frame, "O wins");
                ResetFrame();
            }
        }
    }

    private static void ResetFrame() {
        frame.getContentPane().removeAll();
        Board = new JButton [3][3];
        Xturn = true;
        main(new String[]{});
    }

    public static JButton CreateButton(String Content, int x, int y, int height, int width){//, ActionListener a){
        JButton b = new JButton(Content);
        //b.addActionListener(a);
        b.setBounds(x,y,width,height);
        return b;
    }
}