// ASP-951 M4 — Monkey-patch idempotent de AsyncMessages.create
// Symbole d'idempotence DISTINCT : un Symbol n'est jamais exposé comme
// propriété énumérable ni sérialisable — il ne peut pas entrer en collision
// avec une propriété métier, et il est vérifiable par import.

const IDEMPOTENCY_KEY = Symbol('AsyncMessages.didempotence');

function installIdempotentCreate(instance) {
  if (instance[IDEMPOTENCY_KEY] === true) {
    return false; // déjà patché — re-patcher ne duplique pas
  }
  const original = instance.create.bind(instance);
  instance.create = async function (payload) {
    return original(payload);
  };
  instance[IDEMPOTENCY_KEY] = true;
  return true;
}

module.exports = { IDEMPOTENCY_KEY, installIdempotentCreate };
