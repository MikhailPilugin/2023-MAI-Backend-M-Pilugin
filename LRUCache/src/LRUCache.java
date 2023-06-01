import java.util.LinkedHashMap;
import java.util.Map;

class LRUCache {
    private int capacity;
    private Map<String, String> cache;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        cache = new LinkedHashMap<>();
    }

    public String get(String key) {
        if (cache.containsKey(key)) {
            String value = cache.get(key);
            cache.remove(key);
            cache.put(key, value);
            return value;
        }
        return "";
    }

    public void put(String key, String value) {
        if (cache.size() >= capacity && !cache.containsKey(key))
            cache.remove(cache.entrySet().iterator().next().getKey());

        if (cache.containsKey(key))
            cache.remove(key);

        cache.put(key, value);
    }

    public void rem(String key) {
        if (cache.containsKey(key)) {
            cache.remove(key);
        }
    }

    public static void main(String[] args) {
        LRUCache lruCache = new LRUCache(10);

        lruCache.put("Jesse", "Pinkman");
        lruCache.put("Walter", "White");
        lruCache.put("Jesse", "James");

        System.out.println("Get Jesse: " + lruCache.get("Jesse"));
        lruCache.rem("Walter");
        System.out.println("Get Walter: " + lruCache.get("Walter"));
    }
}