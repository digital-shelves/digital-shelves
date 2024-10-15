using WebAPI.Shared;
using Microsoft.AspNetCore.Mvc;
using NetOceanDirect;

namespace DigitalShelves.Server.Controllers
{

    [ApiController]
    [Route("[controller]")]
    public class DatabaseController : ControllerBase
    {

        private readonly ILogger<DatabaseController> _logger;

        public DatabaseController(ILogger<DatabaseController> logger)
        {
            _logger = logger;
        }

        [HttpGet(Name = "GetItem")]
        public Item Get()  // Pass in any necessary search parameters
        {

            // Return the SpecReading Object
            return new Item
            {
                
            };
        }
    }
}
