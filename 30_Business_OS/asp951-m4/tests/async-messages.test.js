import { describe, it, expect, beforeEach } from 'vitest';
import { AsyncMessages } from '../src/async-messages.js';
import { IDEMPOTENCY_KEY, installIdempotentCreate } from '../src/monkey-patch.js';

describe('AsyncMessages — version synchrone préservée', () => {
  let m;
  beforeEach(() => { m = new AsyncMessages(); });

  it('createSync retourne un message avec id et timestamp', async () => {
    const msg = m.createSync({ body: 'hello' });
    expect(msg.id).toBe(1);
    expect(msg.body).toBe('hello');
    expect(msg.created_at).toBeTruthy();
  });
});

describe('AsyncMessages.create — version asynchrone', () => {
  let m;
  beforeEach(() => { m = new AsyncMessages(); });

  it('create retourne une promesse qui résout un message', async () => {
    const msg = await m.create({ body: 'async hello' });
    expect(msg.id).toBe(1);
    expect(msg.body).toBe('async hello');
    expect(msg.created_at).toBeTruthy();
  });
});

describe('Monkey-patch — symbole didempotence distinct', () => {
  let m;
  beforeEach(() => {
    m = new AsyncMessages();
    installIdempotentCreate(m);
  });

  it('le symbole didempotence est présent et distinct', () => {
    expect(IDEMPOTENCY_KEY).toBeTypeOf('symbol');
    expect(m[IDEMPOTENCY_KEY]).toBe(true);
    // distinct : ce n'est PAS une propriété énumérable classique
    expect(Object.keys(m)).not.toContain('didempotence');
  });

  it('create patché reste asynchrone et fonctionnel', async () => {
    const msg = await m.create({ body: 'patched' });
    expect(msg.body).toBe('patched');
  });

  it('le patch est idempotent : re-patcher ne duplique pas', () => {
    expect(installIdempotentCreate(m)).toBe(false);
    expect(m[IDEMPOTENCY_KEY]).toBe(true);
  });
});
