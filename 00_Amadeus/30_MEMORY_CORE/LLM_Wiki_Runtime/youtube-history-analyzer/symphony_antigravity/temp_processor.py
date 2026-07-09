import sys
import os

# Paths
affine_path = r'C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\affine_deal_drafts.md'
temp_sops_path = r'C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\symphony_antigravity\temp_alpha_sops.md'
csv_path = r'C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv'
runner_path = r'C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer'

sys.path.insert(0, runner_path)
from symphony_antigravity.gemini_handoff_runner import update_csv_status

def process_video(video_id, title, channel, deal_content):
    # 1. Inject Affine (with duplicate check)
    marker = f'## 📝 Draft SOP — {title}'
    if os.path.exists(affine_path):
        with open(affine_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if marker not in content:
            with open(affine_path, 'a', encoding='utf-8') as f:
                f.write(f'\n{marker} (Chaîne: {channel})\n*Date de capture : 2026-05-24*\n\n{deal_content}\n\n---\n')
            print(f'SOP injected into Affine for {video_id}')
        else:
            print(f'SOP already exists in Affine for {video_id}')
    
    # 2. Append Temp Alpha SOPs
    with open(temp_sops_path, 'a', encoding='utf-8') as f:
        f.write(f'# {title} ({video_id})\n\n{deal_content}\n\n---\n')
    print(f'SOP appended to temp_alpha_sops.md for {video_id}')

    # 3. Update CSV
    update_csv_status(video_id, 'CLARIFIED_PLANE')
    print(f'CSV status updated for {video_id}')

if __name__ == "__main__":
    v_id = sys.argv[1]
    v_title = sys.argv[2]
    v_channel = sys.argv[3]
    v_deal = sys.stdin.read()
    process_video(v_id, v_title, v_channel, v_deal)
