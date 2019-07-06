public class Fruit {
    public String name;
    public static int numFruit = 1;
    private boolean canGrow = true;

    public Fruit(String name){
        this.name = name;
    }
    public boolean getCanGrow(){
        return canGrow;
    }
    public static int getNumFruit(){
        return numFruit;
    }
    public String getName(){
        return name;
    }
    public static Fruit pick(Apple a){
        return a;
    }
    public boolean equals(Fruit f){
        return this.name.equals(f.name) && this.numFruit==f.numFruit;
    }
    public String toString(){
        return "This is a fruit.";
    } }