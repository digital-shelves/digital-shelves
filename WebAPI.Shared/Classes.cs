
// Store classes that are shared across pages here

namespace WebAPI.Shared
{

    public class Item
    {
        public string name { get; set; }
        public string description { get; set; }
        public uint ID { get; set; }
        public uint amountAvailable { get; set; }

        // Image attribute here
        // Somehow link an image of the item, or the directory to the .png/.jpeg file
    }

}

