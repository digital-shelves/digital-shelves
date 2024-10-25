
// Store classes that are shared across pages here

namespace WebAPI.Shared
{

    public class Item
    {
        public string Name { get; set; }
        public string Description { get; set; }
        public uint ID { get; set; }
        public uint AmountAvailable { get; set; }
        public string ImageURL { get; set; }
    }
}

