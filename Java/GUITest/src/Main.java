import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


class gui{
    public static void main(String args[]){
        JFrame frame = new JFrame("Test GUI");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1000,1000);
        frame.setLayout(null);
        JButton button = CreateButton("hi", 200,100,100,200,ButPress());
        frame.getContentPane().add(button); // Adds Button to content pane of frame
        frame.setVisible(true);
    }
    public static ActionListener ButPress(){
        return new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("This");
            }
        };

    }

    public static JButton CreateButton(String Content, int x, int y, int height, int width, ActionListener a){
        JButton b = new JButton(Content);
        b.addActionListener(a);
        b.setBounds(x,y,width,height);
        return b;
    }
}

