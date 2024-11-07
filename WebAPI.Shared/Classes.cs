
// Store classes that are shared across pages here

namespace WebAPI.Shared
{

    public class Item
    {
        public int ID { get; set; }
        public string Name { get; set; } = string.Empty;
        public string CheckoutDate { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
        public int AmountAvailable { get; set; }
        public string ImageURL { get; set; } = string.Empty;
    }

    public class User
    {
        public uint ID { get; set; }
        public string Username { get; set; } = string.Empty;
        public string Password { get; set; } = string.Empty;
        public string FirstName { get; set; } = string.Empty;
        public string LastName { get; set; } = string.Empty;
    }
}

