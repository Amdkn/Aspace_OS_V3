import sys
sys.path.insert(0, r'C:\Users\amado\agent-os\citadel')
from pathlib import Path
import serve as s

flags_to_test = [
  ('canonic_writes', s.canonic_writes_enabled, s.ENABLE_CANONIC_FLAG),
  ('autostart', s.autostart_enabled, s.ENABLE_AUTOSTART_FLAG),
  ('watchdog', s.watchdog_enabled, s.ENABLE_WATCHDOG_FLAG),
  ('zora', s.zora_enabled, s.ENABLE_ZORA_FLAG),
]
for name, fn, flag in flags_to_test:
  flag_exists = flag.exists()
  fn_result = fn()
  twelvewy_flag = Path(s.FLAG.parent / '12WY_ON_PAUSE.flag')
  twelvewy_exists = twelvewy_flag.exists()
  twelvewy_size = twelvewy_flag.stat().st_size if twelvewy_exists else 0
  print(f'{name}: fn()={fn_result} flag_exists={flag_exists} twelvewy_exists={twelvewy_exists} twelvewy_size={twelvewy_size}')
