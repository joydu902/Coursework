abstract class Bag {
    private String color;
    private int capacity;
    private int numberOfContents;
    private String[] contents;

    public Bag(String color, int capacity) {
        this.color = color;
        this.capacity = capacity;
        this.contents = new String[capacity];
        this.numberOfContents = 0;

    }
    public String getColor() {
        return this.color;
    }

    public int getNumberOfContents() {
        return this.numberOfContents;
    }

    public int getCapacity() {
        return this.capacity;
    }

    public void setColor(String newco) {
        this.color = newco;
    }

    public String addItem(String item) {
        if (this.numberOfContents >= this.capacity) {
            return item;
        }
        else {
            this.contents[numberOfContents] = item;
            this.numberOfContents++;
            return null;
        }

    }

    public String popItem() {
        if (this.capacity == 0) {
            return null;
        }
        else{
            String removed = this.contents[this.numberOfContents-1];
            this.contents[this.numberOfContents-1] = "";
            this.numberOfContents--;
            return removed;
        }
    }
    public void enhance() {
        this.capacity += 1;
    }
    protected void update(int extraCapacity) {
        this.capacity += extraCapacity;

    }
}
