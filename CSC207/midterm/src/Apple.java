public class Apple extends Fruit{
    public String name;
    public static int numFruit = 2;
    private int numSeeds;
    private String variety;
    public Apple(int numSeeds, String variety){
        super("apple");
        this.numSeeds = numSeeds;
        this.variety = variety;
    }
    public int getNumSeeds(){
        return numSeeds;
    }
    public String getVariety(){
        return variety;
    }
    public static int getNumFruit(){
        return numFruit;
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    public String toString(){
        return "This is an apple";
    }
    public static Apple pickFruit(Fruit f){
        return new Apple(0, "new apple");
    } }