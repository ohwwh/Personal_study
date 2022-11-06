package AbstractandInterface;

public class Runner {
    public static void main(String[] args){
        Flyable[] flyingObjects = {new Bird(), new Plane()};
        for(Flyable object:flyingObjects){
            object.fly();
        }
        
        //Flyable.fly();

        AbstractAnimal animal = new Cat();
        Cat cat = new Cat();
        Dog dog = new Dog();
        cat.bark();
        dog.bark();
        animal.bark(); //추상클래스의 경우 그 자식 클래스에서 필연적으로 함수의 오버라이딩이 일어나기 때문에 
        //다음과 같이 부모클래스로 형변환이 되어도 bark()함수를 정상적으로 쓸 수 있다.
    }
}
