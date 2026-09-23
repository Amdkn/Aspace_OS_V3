import http from 'node:http';
import { Client } from 'file:///C:/Users/amado/AppData/Local/npm-cache/_npx/eb66b3777b041ab8/node_modules/@modelcontextprotocol/sdk/dist/esm/client/index.js';
import { StdioClientTransport } from 'file:///C:/Users/amado/AppData/Local/npm-cache/_npx/eb66b3777b041ab8/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js';

const HOST = '127.0.0.1';
const PORT = 43118;
const SERVER = 'C:/Users/amado/AppData/Local/npm-cache/_npx/eb66b3777b041ab8/node_modules/google-jules-mcp/dist/index.js';

const client = new Client({ name: 'aspace-jules-proxy', version: '1.0.0' });
const transport = new StdioClientTransport({
  command: 'node',
  args: [SERVER],
  env: { ...process.env },
  stderr: 'pipe'
});

transport.stderr?.on('data', d => process.stderr.write(`[jules-mcp] ${d}`));
await client.connect(transport);
console.log(`Jules MCP connected (pid=${transport.pid})`);

function send(res, status, body) {
  const text = JSON.stringify(body, null, 2);
  res.writeHead(status, { 'content-type': 'application/json; charset=utf-8' });
  res.end(text);
}
async function callTool(name, args = {}) {
  const result = await client.callTool({ name, arguments: args });
  const text = result?.content?.find(x => x.type === 'text')?.text;
  if (!text) return result;
  try { return JSON.parse(text); } catch { return { text, isError: result.isError }; }
}

async function readBody(req) {
  let data = '';
  for await (const chunk of req) data += chunk;
  if (!data) return {};
  return JSON.parse(data);
}

const routes = {
  '/health': async () => ({ ok: true, mcpPid: transport.pid }),
  '/tools': async () => client.listTools(),
  '/sessions': async () => callTool('jules_list_sessions', { pageSize: 100 }),
  '/sources': async () => callTool('jules_list_sources', { pageSize: 100 })
};

const server = http.createServer(async (req, res) => {
  try {
    const url = new URL(req.url, `http://${HOST}:${PORT}`);
    if (req.method === 'GET' && routes[url.pathname]) {
      return send(res, 200, await routes[url.pathname]());
    }
    if (req.method === 'POST' && url.pathname === '/sessions') {
      const body = await readBody(req);
      return send(res, 200, await callTool('jules_create_session', body));
    }
    let m = url.pathname.match(/^\/sessions\/([^/]+)$/);
    if (req.method === 'GET' && m) {
      return send(res, 200, await callTool('jules_get_session', { sessionId: m[1] }));
    }
    m = url.pathname.match(/^\/sessions\/([^/]+)\/activities$/);
    if (req.method === 'GET' && m) {
      return send(res, 200, await callTool('jules_list_activities', { sessionId: m[1], pageSize: 100 }));
    }
    m = url.pathname.match(/^\/sessions\/([^/]+)\/message$/);
    if (req.method === 'POST' && m) {
      const body = await readBody(req);
      return send(res, 200, await callTool('jules_send_message', { sessionId: m[1], prompt: body.prompt }));
    }
    m = url.pathname.match(/^\/sessions\/([^/]+)\/approve$/);
    if (req.method === 'POST' && m) {
      return send(res, 200, await callTool('jules_approve_plan', { sessionId: m[1] }));
    }
    return send(res, 404, { error: 'not_found' });
  } catch (error) {
    return send(res, 500, { error: String(error?.message || error) });
  }
});

server.listen(PORT, HOST, () => {
  console.log(`Jules proxy listening on http://${HOST}:${PORT}`);
});
