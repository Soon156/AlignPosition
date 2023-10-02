using ParentalService;
using Serilog;
using Serilog.Events;

string appDataFolderPath = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
string relativePath = "AlignPosition\\logs\\AppStatus.txt";
string fullPath = Path.Combine(appDataFolderPath, relativePath);


Log.Logger = new LoggerConfiguration()
    .MinimumLevel.Debug()
    .MinimumLevel.Override("ParentalService.Worker", LogEventLevel.Information)
    .Enrich.FromLogContext()
    .WriteTo.File(fullPath)
    .CreateLogger();

IHost host = Host.CreateDefaultBuilder(args)
    .ConfigureServices(services =>
    {
        services.AddHostedService<Worker>();
    })
    .UseWindowsService()
    .UseSerilog()
    .Build();

await host.RunAsync();