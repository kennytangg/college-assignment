import java.util.*;

public class Main {
    // method to reverse a sentence
    static void reverseSentence(String input){
        Stack<String> stack = new Stack<>();
        String[] sentence = input.split(" ");
        for(String word: sentence) {
            stack.push(word);
        }
        ArrayList<String>  reverseSentence = new ArrayList<>();
        while(!stack.isEmpty()){
            String word = stack.pop();
            reverseSentence.add(word);
        }
        String reversedSentence = String.join(" ", reverseSentence);
        System.out.println(reversedSentence);
    }
    // method to queue name and remove if it is called
    static void callCenter(Queue<String> queue ,String name){
        if (queue.peek() == name){
            String Name = queue.remove();
            System.out.println(Name + " will be called");
        } else{
            queue.add(name);
            System.out.println(name + " has been added to the queue");
        }
    }

    // main method to test the methods
    public static void main(String[] args) {
        String sentence = "Hello World Java Python C";
        reverseSentence(sentence);

        Queue<String> queue = new LinkedList<>();
        queue.add("Alex");
        queue.add("John");
        queue.add("Jessica");
        System.out.println(queue);
        callCenter(queue, "Max");
        System.out.println(queue);
        callCenter(queue, "Alex");
        System.out.println(queue);
    }
}