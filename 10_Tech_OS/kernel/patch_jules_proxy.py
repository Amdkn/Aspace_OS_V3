p=r'C:\Users\amado\ASpace_OS_V3\10_Tech_OS\kernel\jules_mcp_proxy.mjs'
s=open(p,encoding='utf-8').read()
needle="    let m = url.pathname.match(/^\\/sessions\\/([^/]+)$/);"
insert="""    if (req.method === 'POST' && url.pathname === '/sessions') {
      const body = await readBody(req);
      return send(res, 200, await callTool('jules_create_session', body));
    }
"""
assert needle in s
if "url.pathname === '/sessions'" not in s:
    s=s.replace(needle,insert+needle,1)
    open(p,'w',encoding='utf-8').write(s)
print('proxy create-session route ready')