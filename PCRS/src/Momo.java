class Momo implements AlienAnimal, Tradable {
    private double alien_price;

    public Momo(double alien_price) {
        this.alien_price = alien_price;
    }

    public String sound() {
        return "momo momo";
    }

    public double getHumanPrice() {
        return this.alien_price * 1/100;
    }
    public double getAlienPrice() {
        return this.alien_price;
    }


}
