using WebAPI.Shared;
using Microsoft.AspNetCore.Mvc;
<<<<<<< HEAD
using System.Net.Http;

=======
>>>>>>> ab2fe9b26d19a28ba3498bc4fe174eebc14a3284

namespace DigitalShelves.Server.Controllers
{

    [ApiController]
    [Route("api/[controller]")]
    public class ItemsController : ControllerBase
    {

        private readonly ILogger<ItemsController> _logger;
        private readonly HttpClient _httpClient;

        public ItemsController(ILogger<ItemsController> logger, HttpClient httpClient)
        {
            _logger = logger;
            _httpClient = httpClient;
        }

        [HttpGet(Name = "search")]
        public async Task<ActionResult<Item>> Get([FromQuery] string searchQuery) // Pass in any necessary search parameters
        {
            try
            {
                // Make a request to your Django REST API
                var apiUrl = $"http://localhost:8000/api/items/search/?query={searchQuery}"; // Update this URL as needed
                var item = await _httpClient.GetFromJsonAsync<Item>(apiUrl);

                if (item == null)
                {
                    return NotFound(); // Return 404 if item is not found
                }

                return Ok(item); // Return the item if found
            }
            catch (HttpRequestException e)
            {
                _logger.LogError(e, "Error fetching item from the API.");
                return StatusCode(500, "Internal server error while contacting the API.");
            }
        }
    }
}
