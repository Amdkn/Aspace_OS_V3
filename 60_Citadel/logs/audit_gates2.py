import sys
sys.path.insert(0, r'C:\Users\amado\agent-os\citadel')
import serve as s
from pathlib import Path

print('DECISIONS_DIR =', s.DECISIONS_DIR)
print('exists =', s.DECISIONS_DIR.exists())
twelvewy = s.DECISIONS_DIR / '12WY_ON_PAUSE.flag'
print('12WY flag path =', twelvewy)
print('exists =', twelvewy.exists())
if twelvewy.exists():
  print('content (head) =', repr(twelvewy.read_text()[:80]))
  print('content (stripped) =', repr(twelvewy.read_text().strip()))

print()
print('canonic flag :', s.ENABLE_CANONIC_FLAG)
print('exists :', s.ENABLE_CANONIC_FLAG.exists())
print()
print('FUNCTION RETURNS:')
print('  canonic_writes_enabled =', s.canonic_writes_enabled())
print('  autostart_enabled      =', s.autostart_enabled())
print('  watchdog_enabled       =', s.watchdog_enabled())
print('  zora_enabled           =', s.zora_enabled())
