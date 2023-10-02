using Microsoft.Win32;
using System.Diagnostics;

namespace ParentalService
{
    public sealed class Worker : BackgroundService
    {
        private readonly IHostApplicationLifetime _hostApplicationLifetime;
        private readonly ILogger<Worker> _logger;

        public Worker(
        IHostApplicationLifetime hostApplicationLifetime, ILogger<Worker> logger) =>
        (_hostApplicationLifetime, _logger) = (hostApplicationLifetime, logger);

        private string GetRegistryValue()
        {
            try
            {
                string subkey = @"SOFTWARE\Align Position";
                string valueName = "Resource Folder";

                using (RegistryKey registryKey = Registry.CurrentUser.OpenSubKey(subkey))
                {
                    if (registryKey != null)
                    {
                        object value = registryKey.GetValue(valueName);
                        if (value != null)
                        {
                            _logger.LogInformation("Registry Path for Resource Folder founded: " + value.ToString());
                            return value.ToString();
                        }
                        else
                        {
                            _logger.LogInformation("Registry Value for Resource Folder not found...");
                        }
                    }
                    else
                    {
                        _logger.LogInformation("Registry Path for Resource Folder not found...");
                    }
                }
            }
            catch (Exception ex)
            {
                _logger.LogInformation(ex.ToString());
            }
            return null; // Handle if the registry value doesn't exist
        }

        private string GetParentalState()
        {
            string subkey = @"Software\Align Position";
            string valueName = "Parental State";
            string new_value = null;
            try
            {
                using (RegistryKey registryKey = Registry.CurrentUser.OpenSubKey(subkey))
                {
                    if (registryKey != null)
                    {
                        object value = registryKey.GetValue(valueName);
                        new_value = value.ToString();
                        if (new_value == "1")
                        {
                            _logger.LogInformation("Parental Control of AlignPosition is active");
                        }
                        else
                        {
                            _logger.LogInformation("Parental Control of AlignPosition is deactive");
                        }
                    }
                    else
                    {
                        _logger.LogInformation("Registry for Parental Control not found");
                    }
                }
                return new_value;
            }
            catch (Exception ex)
            {
                _logger.LogInformation(ex.ToString());
            }


            return "0"; // Default value if the registry value doesn't exist
        }

        private bool IsApplicationRunning(string processName)
        {
            Process[] processes = Process.GetProcessesByName(processName);
            return processes.Length > 3;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            try
            {
                while (!stoppingToken.IsCancellationRequested)
                {
                    string installPath = GetRegistryValue();
                    await Task.Delay(5000, stoppingToken);
                    _logger.LogInformation(installPath);
                }

                /*if (installPath != null){
                    //!stoppingToken.IsCancellationRequested
                    
                    while (!stoppingToken.IsCancellationRequested)
                    {
                        string exePath = Path.Combine(installPath, "AlignPosition.exe");
                        string arguments = "--background";
                        if (!IsApplicationRunning("AlignPosition"))
                        {
                            string parentalState = GetParentalState();
                            _logger.LogInformation("AlignPosition services is not running");
                            if (parentalState == "1")
                            {
                                Process.Start(new ProcessStartInfo
                                {
                                    FileName = exePath,
                                    Arguments = arguments,
                                    WorkingDirectory = installPath,
                                    UseShellExecute = true // Open in a separate process

                                });
                                _logger.LogInformation("AlignPosition services started by parental services");
                            }
                            else
                            {
                                break;
                            }
                        }
                        else
                        {
                            _logger.LogInformation("AlignPosition services is running");
                        }
                        await Task.Delay(5000, stoppingToken);
                    }
            }
                _logger.LogInformation("AlignPosition services stopped");
                _hostApplicationLifetime.StopApplication(); // Stop the service gracefully*/
            }
            catch (Exception ex)
            {
                _logger.LogInformation(ex.ToString());
            }
            _hostApplicationLifetime.StopApplication();
        }

    }
}