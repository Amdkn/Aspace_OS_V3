// ASP-951 M4 — AsyncMessages: version synchrone préservée + create() asynchrone
class AsyncMessages {
  constructor() {
    this._messages = [];
  }

  // Version synchrone PRÉSERVÉE (API existante, non modifiée)
  createSync(payload) {
    const msg = { id: this._messages.length + 1, ...payload, created_at: new Date().toISOString() };
    this._messages.push(msg);
    return msg;
  }

  // Version ASYNCHRONE — cible du monkey-patch (work 11)
  async create(payload) {
    const msg = { id: this._messages.length + 1, ...payload, created_at: new Date().toISOString() };
    this._messages.push(msg);
    return msg;
  }
}

module.exports = { AsyncMessages };
