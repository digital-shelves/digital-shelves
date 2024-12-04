using WebAPI.Shared;
using Microsoft.AspNetCore.Mvc;

namespace DigitalShelves.Server.Controllers
{

    [ApiController]
    // Controller name of "admin"
    [Route("[controller]")]
    public class AdminController : ControllerBase
    {

        private readonly ILogger<AdminController> _logger;
        private readonly HttpClient _httpClient;

        public AdminController(ILogger<AdminController> logger, HttpClient httpClient)
        {
            _logger = logger;
            _httpClient = httpClient;
        }

        [HttpPost(Name = "login")]
        public async Task<ActionResult<User>> Post([FromQuery] string username, string password) // Pass in any necessary search parameters
        {
            try
            {
                var loginData = new {username, password };

                // Make a request to Django REST API
                // THIS IS WHERE WE WILL NEED TO UPDATE BASED ON NATIVE DJANGO LOGIN API
                var apiUrl = $"http://127.0.0.1:8000/admin/login/";
                var response = await _httpClient.PostAsJsonAsync(apiUrl, loginData);

                if (!response.IsSuccessStatusCode)
                {
                    return Unauthorized(); // Return 401 if authentication fails
                }

                // Read and deserialize the response content if authentication is successful
                var user = await response.Content.ReadFromJsonAsync<User>();
                return Ok(user); // Return the user if found
            }
            catch (HttpRequestException e)
            {
                _logger.LogError(e, "Error fetching user from the API.");
                return StatusCode(500, "Internal server error while contacting the API.");
            }
        }
    }
}
