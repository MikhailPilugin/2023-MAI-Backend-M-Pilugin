public class LRUCache {


    public static void main(String[] args) {
        Cache cache = new Cache(100);
        cache.set("Jesse", "Pinkman");
        cache.set("Walter", "White");
        cache.set("Jessie", "James");

       // lru.getAll();

        System.out.println("Get Jessie: " + cache.get("Jessie") + "\n");

       // lru.getAll();

        cache.rem("Walter");

        System.out.println("Get Walter: " + cache.get("Walter") + "\n");

       // lru.getAll();
    }
}
