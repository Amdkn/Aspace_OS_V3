using System.Buffers.Binary;
using System.Diagnostics;
using System.Net.Http;
using System.Text;
using System.Text.Json;

static void Log(object payload) {
    var path = Environment.GetEnvironmentVariable("ASPACE_NATIVE_LOG");
    if (String.IsNullOrWhiteSpace(path)) return;
    try {
        File.AppendAllText(path, JsonSerializer.Serialize(payload) + Environment.NewLine);
    } catch {}
}


var input = Console.OpenStandardInput();
var output = Console.OpenStandardOutput();
using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(5) };
Log(new { evt = "start", pid = Environment.ProcessId });

while (true) {
    var header = new byte[4];
    var got = await input.ReadAsync(header, 0, 4);
    if (got == 0) break;
    while (got < 4) {
        var n = await input.ReadAsync(header, got, 4 - got);
        if (n == 0) return;
        got += n;
    }
    var length = BinaryPrimitives.ReadInt32LittleEndian(header);
    if (length <= 0 || length > 900_000) {
        Log(new { evt = "reject_length", length });
        return;
    }
    var body = new byte[length];
    var offset = 0;
    while (offset < length) {
        var n = await input.ReadAsync(body, offset, length - offset);
        if (n == 0) return;
        offset += n;
    }
    var json = Encoding.UTF8.GetString(body);
    Log(new { evt = "in", pid = Environment.ProcessId, json });

    string worker = Environment.GetEnvironmentVariable("ASPACE_WORKER_URL");
    if (string.IsNullOrWhiteSpace(worker)) {
        string runtimeJsonPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), ".aspace", "dc", "run", "runtime.json");
        if (File.Exists(runtimeJsonPath)) {
            try {
                using var doc = JsonDocument.Parse(File.ReadAllText(runtimeJsonPath));
                if (doc.RootElement.TryGetProperty("worker_url", out var urlProp) && urlProp.ValueKind == JsonValueKind.String) {
                    worker = urlProp.GetString();
                } else if (doc.RootElement.TryGetProperty("worker_port", out var portProp) && portProp.ValueKind == JsonValueKind.Number) {
                    worker = $"http://127.0.0.1:{portProp.GetInt32()}/native";
                }
            } catch { }
        }
    }

    string responseText;
    if (string.IsNullOrWhiteSpace(worker)) {
        responseText = JsonSerializer.Serialize(new { ok = false, error = "RUNTIME_UNAVAILABLE", detail = "No ASPACE_WORKER_URL and ~/.aspace/dc/run/runtime.json is missing or invalid" });
    } else {
        try {
            using var content = new StringContent(json, Encoding.UTF8, "application/json");
            using var response = await http.PostAsync(worker, content);
            responseText = await response.Content.ReadAsStringAsync();
            if (!response.IsSuccessStatusCode) {
                responseText = JsonSerializer.Serialize(new { ok = false, error = "WORKER_HTTP_" + (int)response.StatusCode, detail = responseText });
            }
        } catch (Exception ex) {
            responseText = JsonSerializer.Serialize(new { ok = false, error = "WORKER_UNAVAILABLE", detail = ex.GetType().Name + ": " + ex.Message });
        }
    }
    var responseBytes = Encoding.UTF8.GetBytes(responseText);
    if (responseBytes.Length > 900_000) {
        responseText = JsonSerializer.Serialize(new { ok = false, error = "RESPONSE_TOO_LARGE" });
        responseBytes = Encoding.UTF8.GetBytes(responseText);
    }
    var outHeader = new byte[4];
    BinaryPrimitives.WriteInt32LittleEndian(outHeader, responseBytes.Length);
    await output.WriteAsync(outHeader);
    await output.WriteAsync(responseBytes);
    await output.FlushAsync();
    Log(new { evt = "out", pid = Environment.ProcessId, json = responseText });
}
Log(new { evt = "stop", pid = Environment.ProcessId });
