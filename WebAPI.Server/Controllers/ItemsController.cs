using WebAPI.Shared;
using Microsoft.AspNetCore.Mvc;
using NetOceanDirect;

namespace DigitalShelves.Server.Controllers
{

    [ApiController]
    [Route("api/[controller]")]
    public class ItemsController : ControllerBase
    {

        private readonly ILogger<ItemsController> _logger;

        public ItemsController(ILogger<ItemsController> logger)
        {
            _logger = logger;
        }

        [HttpGet(Name = "search")]
        public Item Get()  // Pass in any necessary search parameters
        {

            // Return the SpecReading Object
            return new Item
            {
                
            };
        }
    }
}
