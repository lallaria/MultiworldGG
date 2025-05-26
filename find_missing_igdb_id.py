import os

with open('base_world_inits.txt', encoding='utf-8') as f:
    files = [line.strip() for line in f if line.strip()]

missing = []
for path in files:
    try:
        if not os.path.exists(path):
            missing.append(path + ' (file not found)')
            continue
        with open(path, encoding='utf-8') as f2:
            content = f2.read()
            if 'igdb_id' not in content:
                missing.append(path)
    except Exception as e:
        missing.append(f'{path} (error: {e})')

with open('missing_igdb_id.txt', 'w', encoding='utf-8') as out:
    for m in missing:
        out.write(m + '\n')

print(f'Checked {len(files)} files. {len(missing)} missing igdb_id.') 