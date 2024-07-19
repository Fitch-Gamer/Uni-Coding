

public class Main {
    public static void main(String[] args) {
        start();
    }

    public static  void start()
    {
        SortedLinkedList test = new SortedLinkedList();
        test.add("zx");
        test.add("aa");
        test.add("ab");
        test.add("aa");
        test.add("ac");


        test.print();

        System.out.println("");
        System.out.println(test.getFirst().getString());
        System.out.println("");
        System.out.println(test.getLast().getString());


    }

    /**
     * Node class for use with the CM10228: Principles of Programming 2 coursework.
     *
     * This should not be modified by the student.
     *
     * @author		Christopher Clarke
     * @version		1.0
     */

    public interface SortedList {

        /**
         * Returns the number of Nodes in the linked list.
         *
         * @return      the number of Nodes in the linked list
         */
        public int size();

        /**
         * Adds a Node with the specified string to the linked list in
         * the appropriate position given the specified alphabetical order
         * (i.e., ascending/descending).
         *
         * @param  string  a String to be added to the linked list
         */
        public void add(String string);

        /**
         * Adds a Node to the linked list in the appropriate position
         * given the specified alphabetical order (i.e., ascending/descending).
         *
         * @param  node  a Node to be added to the linked list
         */
        public void add(Node node);

        /**
         * Returns the first Node of the linked list given the specified
         * alphabetical order (i.e., ascending/descending).
         *
         * @return      the first Node in the linked list
         */
        public Node getFirst();

        /**
         * Returns the last Node of the linked list given the specified
         * alphabetical order (i.e., ascending/descending).
         *
         * @return      the last Node in the linked list
         */
        public Node getLast();

        /**
         * Returns the Node at the specified index assuming indices start
         * at 0 and end with size-1 given the specified alphabetical order
         * (i.e., ascending/descending).
         *
         * @param  index  the index of the Node in the linked list to be retrieved
         * @return      the Node in the linked list at the specified index
         */
        public Node get(int index);

        /**
         * Checks to see if the list contains a Node with the specified
         * string.
         *
         * @param  string  the String to be searched for in the linked list
         * @return       True if the string is present or false if not
         */
        public boolean isPresent(String string);

        /**
         * Removes the first Node from the list given the specified
         * alphabetical order (i.e., ascending/descending).
         *
         * @return      Returns true if successful or false if unsuccessful
         */
        public boolean removeFirst();

        /**
         * Removes the last Node from the list given the specified
         * alphabetical order (i.e., ascending/descending).
         *
         * @return      Returns true if successful or false if unsuccessful
         */
        public boolean removeLast();

        /**
         * Removes the Node at the specified index from the list assuming indices
         * start at 0 and end with size-1 given the specified alphabetical order
         * (i.e., ascending/descending)
         *
         * @param  index  the index of the Node in the linked list to be removed
         * @return      Returns true if successful or false if unsuccessful
         */
        public boolean remove(int index);

        /**
         * Removes the Node from the list that contains the specified string.
         *
         * @param  string  the string to be removed from the linked list
         * @return      Returns true if successful or false if unsuccessful
         */
        public boolean remove(String string);

        /**
         * Orders the linked list in ascending alphabetical order.
         *
         */
        public void orderAscending();

        /**
         * Orders the linked list in descending alphabetical order.
         *
         */
        public void orderDescending();

        /**
         * Prints the contents of the linked list in the specified alphabetical order
         * (i.e., ascending/descending) to System.out with each node's string on
         * a new line.
         *
         */
        public void print();
    }

    public static class Node {
        private String name;
        private Node prev;
        private Node next;

        public Node(String name) {
            this.prev = null;
            this.name = name;
            this.next = null;
        }

        public Node(String name, Node next) {
            this.prev = null;
            this.name = name;
            this.next = next;
        }

        public Node(Node prev, String name) {
            this.prev = prev;
            this.name = name;
            this.next = null;
        }

        public Node(Node prev, String name, Node next) {
            this.prev = prev;
            this.name = name;
            this.next = next;
        }

        public void setString(String name) {
            this.name = name;
        }

        public String getString() {
            return this.name;
        }

        public void setNext(Node next) {
            this.next = next;
        }

        public Node getNext() {
            return this.next;
        }

        public void setPrev(Node prev) {
            this.prev = prev;
        }

        public Node getPrev() {
            return this.prev;
        }
    }
    public static class SortedLinkedList implements SortedList
    {
        private Node StartNode = null;
        private int Direction = 1;

        public int size() {
            if(StartNode == null)
            {
                return 0;
            }
            else
            {
                Node CurNode = StartNode;
                int Iter = 1;
                while(true)
                {

                    if(CurNode.getNext() == null)
                    {
                        return Iter;
                    }
                    else
                    {
                        CurNode = CurNode.getNext();
                        Iter++;
                    }
                }
            }
        }

        public void add(Node node) {

            if(StartNode == null)
            {
                StartNode = node;
            }
            else if (StartNode.getString().compareToIgnoreCase(node.getString())*Direction >0)
            {
                StartNode.setPrev(node);
                node.setNext(StartNode);
                StartNode = node;
            }
            else
            {
                Node CurNode = StartNode;
                while(true)
                {
                    if(CurNode.getString().equalsIgnoreCase(node.getString()))
                    {
                        return;
                    }
                    if( CurNode.getString().compareToIgnoreCase(node.getString())*Direction > 0 )
                    {
                        if(CurNode.getPrev() != null)
                        {
                            CurNode.getPrev().setNext(node);
                        }

                        node.setNext(CurNode);
                        node.setPrev(CurNode.getPrev());
                        CurNode.setPrev(node);
                        return;
                    }
                    if(CurNode.getNext()==null)
                    {
                        node.setPrev(CurNode);
                        CurNode.setNext(node);
                        return;
                    }
                    CurNode = CurNode.getNext();
                }
            }

        }

        public Node getFirst() {
            return StartNode;
        }

        public Node getLast() {
            if(StartNode == null)
            {
                return null;
            }
            Node tmp = StartNode;
            while(tmp.getNext()!=null)
            {
                tmp = tmp.getNext();
            }
            return tmp;


        }

        public Node get(int index) {
            if(StartNode == null)
            {
                return null;
            }
            Node tmp = StartNode;
            for (int i = 0; i<index; i++)
            {
                if(tmp.getNext() != null)
                {
                    tmp = tmp.getNext();
                }
                else
                {
                    return null;
                }
            }
            return tmp;
        }

        public boolean removeFirst() {
            try
            {
                StartNode.getNext().setPrev(null);
                StartNode = StartNode.getNext();
                return true;
            }
            catch(Exception e)
            {
                return false;
            }

        }

        public boolean removeLast() {
            try
            {
                Node tmp = getLast();
                tmp.getPrev().setNext(null);
                return true;
            }
            catch(Exception e)
            {
                return false;
            }
        }

        public boolean remove(int index) {
            try
            {
                Node tmp = get(index);

                tmp.getPrev().setNext(tmp.getNext());
                tmp.getNext().setPrev(tmp.getPrev());
                return true;
            }
            catch(Exception e)
            {
                return false;
            }
        }

        public void orderAscending() {
            if(Direction!=-1)
            {
                Direction = 1;
                inverse();
            }
        }

        public void orderDescending() {
            if(Direction!=1)
            {
                Direction = -1;
                inverse();
            }
        }

        private void inverse()
        {
            Node tmp = getLast();
            Node Switch = tmp.getNext();
            tmp.setNext(tmp.getPrev());
            tmp.setPrev(Switch);
            StartNode = tmp;
            if(tmp.getNext()!=null)
            {
                tmp = tmp.getNext();
            }
            else
            {
                return;
            }
            while(true)
            {
                Switch = tmp.getNext();
                tmp.setNext(tmp.getPrev());
                tmp.setPrev(Switch);
                if(tmp.getNext() == null)
                {
                    return;
                }
                tmp = tmp.getNext();
            }
        }

        public void print() {
            Node tmp = StartNode;
            while(true)
            {
                System.out.println(tmp.getString());
                if(tmp.getNext() == null)
                {
                    break;
                }
                tmp = tmp.getNext();
            }
        }

        public boolean remove(String string) {
            Node tmp = StartNode;
            while(true)
            {
                if(tmp.getString().equalsIgnoreCase(string))
                {
                    tmp.getPrev().setNext(tmp.getNext());
                    tmp.getNext().setPrev(tmp.getPrev());
                    return true;
                }
                if(tmp.getNext() == null)
                {
                    return false;
                }
                tmp = tmp.getNext();
            }
        }

        public boolean isPresent(String string) {
            Node tmp = StartNode;
            while(true)
            {
                if(tmp.getString().equalsIgnoreCase(string))
                {
                    return true;
                }
                if(tmp.getNext() == null)
                {
                    return false;
                }
                tmp = tmp.getNext();
            }
        }

        public void add(String string) {
            add(new Node(string));

        }
    }
}