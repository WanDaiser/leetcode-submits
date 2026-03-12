# Her kutu (node) anahtar, değer ve sağ-sol bağlantı tutuyor
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None  # soldaki
        self.next = None  # sağdaki


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # KEY -> NODE

        # Sahte baş ve kuyruk node'ları (listeyi kolay yönetmek için)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # Baş ve son birbirine bağlı
        self.head.next = self.tail
        self.tail.prev = self.head


    # ----------------------------------------------------------
    # Yardımcı Fonksiyon 1: Listedeki bir node'u çıkar
    # ----------------------------------------------------------
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    # ----------------------------------------------------------
    # Yardımcı Fonksiyon 2: node'u başa ekle (en yeni yap)
    # ----------------------------------------------------------
    def _add_to_front(self, node):
        node.next = self.head.next   # eskiden başta olan kimse
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node


    # ----------------------------------------------------------
    # GET: anahtar varsa değerini döndür + node'u başa taşı
    # ----------------------------------------------------------
    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # kullanıldığı için başa taşınıyor
        self._remove(node)
        self._add_to_front(node)

        return node.value


    # ----------------------------------------------------------
    # PUT: anahtar varsa güncelle + başa taşı
    # Yoksa yeni ekle; kapasite doluysa en eskisini sil
    # ----------------------------------------------------------
    def put(self, key, value):
        # Anahtar zaten varsa: node'u güncelle ve başa taşı
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            # eski yerinden çıkarıp başa koyuyoruz
            self._remove(node)
            self._add_to_front(node)
            return

        # Yeni anahtar-ekleme durumu
        # Kapasite doluysa en eski olanı (tail.prev) sil
        if len(self.cache) == self.capacity:
            lru = self.tail.prev             # en eski node
            self._remove(lru)                # listeden çıkar
            del self.cache[lru.key]          # dictionary'den çıkar

        # yeni node oluştur
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)
