import subprocess
from pathlib import Path
import time
import requests
import os

def div_string(s, char_num):
  ret = []
  current = []
  current_len = 0
  for l in s.split('\n'):
    if len(current) != 0 and current_len + len(l) > char_num:
      ret.append('\n'.join(current))
      current = []
      current_len = 0
      current.append(l)
      current_len += len(l)
    else:
      current.append(l)
      current_len += len(l)
  if len(current) > 0:
    ret.append('\n'.join(current))
  return ret

def discord_Notify(message, fileName=None):
    s = f'{message}'
    n = 1980
    message_list = div_string(s, n)
    for m in message_list:
        discord_Notify_inner(f'```\n{m}\n```', fileName)


def discord_Notify_inner(message, fileName=None):
  url = os.environ['DISCORD_URL']
  if url is not None:
    if fileName is None:
        try:
            payload = {"content": f"{message}"}
            time.sleep(3)
            requests.post(url, data=payload, timeout=(30.0, 30.0))
        except:
          pass
    else:
        try:
            payload = {"content": f"{message}"}
            files = {"imageFile": open(fileName, "rb")}
            time.sleep(3)
            requests.post(url, data=payload, files=files, timeout=(30.0, 30.0))
        except:
            pass

def run_notebook(filename, timeout=-1, capture_output=False):
  return subprocess.run(['jupyter',
                          'nbconvert',
                          '--execute',
                          f'--ExecutePreprocessor.timeout={timeout}',
                          '--to=asciidoc',
                          '--stdout',
                          f'{filename}'], capture_output=capture_output, encoding='utf-8')

def ls_ipynb_files(base_dir='.'):
  p = Path(base_dir)
  return sorted([str(f) for f in p.glob('*.ipynb')])

def main():
  timeout = -1
  try:
    timeout = int(os.environ['NOTEBOOK_TIMEOUT'])
    print(f'Notebook timeout: {timeout}sec')
  except:
    pass

  for filename in ls_ipynb_files():
    result = run_notebook(filename, timeout=timeout , capture_output=True)
    if result.returncode == 0:
      print(f'OK {filename}')
      discord_Notify(f'OK {filename}')
    else:
      print(f'Error {filename}\n{result.stderr}')
      discord_Notify(f'Error {filename}\n{result.stderr}')

if __name__ == "__main__":
  main()
