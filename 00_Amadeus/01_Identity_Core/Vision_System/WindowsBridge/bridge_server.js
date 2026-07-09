const express = require('express');
const screenshot = require('screenshot-desktop');
const app = express();
const PORT = 3000;

app.use(express.json());

// Health check endpoint
app.get('/health', (req, res) => {
    res.json({ status: 'online', service: 'A0 Windows Bridge', timestamp: new Date().toISOString() });
});

// Screenshot endpoint - supports both GET and POST
const handleScreenshot = async (req, res) => {
    try {
        console.log('[BRIDGE] Screenshot requested');
        const imgBuffer = await screenshot({ format: 'png' });

        res.set({
            'Content-Type': 'image/png',
            'Content-Length': imgBuffer.length
        });

        res.send(imgBuffer);
        console.log(`[BRIDGE] Screenshot sent successfully (${imgBuffer.length} bytes)`);
    } catch (error) {
        console.error('[BRIDGE] Screenshot error:', error);
        res.status(500).json({ error: error.message });
    }
};

app.get('/screenshot', handleScreenshot);
app.post('/screenshot', handleScreenshot);

// Start server
app.listen(PORT, '0.0.0.0', () => {
    console.log(`[BRIDGE] A0 Windows Bridge listening on port ${PORT}`);
    console.log(`[BRIDGE] Endpoints:`);
    console.log(`[BRIDGE]   GET  /health - Health check`);
    console.log(`[BRIDGE]   GET  /screenshot - Capture screenshot`);
    console.log(`[BRIDGE]   POST /screenshot - Capture screenshot`);
});

// Graceful shutdown
process.on('SIGINT', () => {
    console.log('[BRIDGE] Shutting down gracefully...');
    process.exit(0);
});
